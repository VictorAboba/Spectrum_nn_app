import os
from typing import Literal
from datetime import datetime

import streamlit as st
import polars as pl

from utils import FOLDER_TO_SAVE_RESULT, model_inference


@st.cache_data
def load_dataframe_from_file(file: bytes, ext) -> pl.DataFrame:
    if ext == ".csv":
        df = pl.read_csv(file)
    elif ext == ".xlsx":
        df = pl.read_excel(file)
    else:
        df = pl.read_parquet(file)

    return df


def save_dataframe(dataframe: pl.DataFrame, filename, ext):
    if ext == ".csv":
        dataframe.write_csv(os.path.join(FOLDER_TO_SAVE_RESULT, filename))
    elif ext == ".xlsx":
        dataframe.write_excel(
            os.path.join(FOLDER_TO_SAVE_RESULT, filename), autofit=True
        )
    else:
        dataframe.write_parquet(os.path.join(FOLDER_TO_SAVE_RESULT, filename))


files = st.file_uploader(
    "Upload datasets", accept_multiple_files=True, type=["csv", "xlsx", "parquet"]
)
particle_type: Literal["p", "he"] = st.selectbox(
    "Choose a particle to predict", ["p", "he"]
)
model_type: Literal["mlp", "cnn"] = st.selectbox(
    "Choose a model for forecasting", ["mlp", "cnn"]
)
st.divider()

result_message = []

if files:
    if st.button("Make predictions"):
        for file in files:
            try:
                with st.spinner(f"{file.name} is loading..."):
                    dataset = load_dataframe_from_file(
                        file.getvalue(), os.path.splitext(file.name)[-1]
                    )
                    dataset = dataset.with_columns(pl.col("date").cast(pl.Datetime))
                st.success(f"{file.name} has been uploaded!")
            except Exception as e:
                result_message.append(
                    f"File: {file.name} | Status: :red[Error] | Error info: Error when load: {e}"
                )
                continue

            try:
                pbar = st.progress(0.0, f"{file.name} is processing...")
                processed_dataset, timestamp = model_inference(
                    dataset, particle_type, model_type, pbar
                )
                pbar.empty()
                st.success(f"{file.name} have been processed!")
            except Exception as e:
                result_message.append(
                    f"File: {file.name} | Status: :red[Error] | Error info: Error during process: {e}"
                )
                continue

            try:
                base_name, ext = os.path.splitext(file.name)
                new_name = (
                    base_name
                    + f"_processed_using_{model_type}_to_predict_{particle_type}_at_{datetime.now().strftime('%Y-%m-%d %H:%M')}"
                    + ext
                )
                with st.spinner("Result is saving..."):
                    save_dataframe(processed_dataset, new_name, ext)  # type: ignore
            except Exception as e:
                result_message.append(
                    f"File: {file.name} | Status: :red[Error] | Error info: Error during save: {e}"
                )
                continue

            result_message.append(
                f"File: {file.name} | Status: :green[Success] | Processed in: {timestamp}, s | Saved to: {os.path.join(FOLDER_TO_SAVE_RESULT.removeprefix('/app'), new_name)}"
            )

        st.markdown("<br>".join(result_message))
