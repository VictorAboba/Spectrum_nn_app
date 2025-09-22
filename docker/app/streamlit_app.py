import os
from datetime import datetime

import streamlit as st
import polars as pl
from typing import Literal

from .utils import model_inference
from .utils.constants import FOLDER_TO_SAVE_RESULT


def load_dataframe_from_file(file, ext) -> pl.DataFrame:
    if ext == "csv":
        df = pl.read_csv(file)
    elif ext == "xlsx":
        df = pl.read_excel(file)
    else:
        df = pl.read_parquet(file)

    return df


def save_dataframe(dataframe: pl.DataFrame, filename, ext):
    if ext == "csv":
        dataframe.write_csv(os.path.join(FOLDER_TO_SAVE_RESULT, filename))
    elif ext == "xlsx":
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

for file in files:
    try:
        dataset = load_dataframe_from_file(file, os.path.splitext(file.name)[-1])
    except Exception as e:
        result_message.append(
            f"File: {file.name}\n__Status: :red[Error]\n__Error info: Error when load: {e}"
        )
        continue

    try:
        processed_dataset, timestamp = model_inference(
            dataset, particle_type, model_type
        )
    except Exception as e:
        result_message.append(
            f"File: {file.name}\n__Status: :red[Error]\n__Error info: Error during process: {e}"
        )
        continue

    try:
        base_name, ext = os.path.splitext(file.name)
        new_name = (
            base_name
            + f"_processed_using_{model_type}_to_predict_{particle_type}_at_{datetime.now().strftime('%Y-%m-%d %H:%M')}"
            + ext
        )
        save_dataframe(processed_dataset, new_name, ext)
    except Exception as e:
        result_message.append(
            f"File: {file.name}\n__Status: :red[Error]\n__Error info: Error during save: {e}"
        )
        continue

    result_message.append(
        f"File: {file.name}\n__Status: :green[Success]\n__Processed in: {timestamp}, s\n__Saved to: {os.path.join(FOLDER_TO_SAVE_RESULT, new_name)}"
    )

st.markdown("\n".join(result_message))
