from pathlib import Path
import os
from datetime import datetime

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import polars as pl

from utils import FOLDER_TO_SAVE_RESULT, model_inference

cli_app = FastAPI()

ALLOWED_EXTENSIONS = {".csv", ".xlsx", ".parquet"}


async def load_dataframe_from_file(file, ext) -> pl.DataFrame:
    content = await file.read()
    if ext == ".csv":
        df = pl.read_csv(content)
    elif ext == ".xlsx":
        df = pl.read_excel(content)
    else:
        df = pl.read_parquet(content)

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


def validate_file_extension(filename: str):
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file extension: {ext}. Valid: {', '.join(ALLOWED_EXTENSIONS)}",
        )
    if not Path(filename).suffix:
        raise HTTPException(400, "File should have extension")


def validate_particle_type(particle_type: str):
    if particle_type.lower() not in ["p", "he"]:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid  particle type: {particle_type}. Valid: p, he",
        )


def validate_model_type(model_type: str):
    if model_type.lower() not in ["mlp", "cnn"]:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid  model type: {model_type}. Valid: mlp, cnn",
        )


@cli_app.post("/run_cli")
async def run_cli(
    file: UploadFile = File(
        ...,
        title="File",
        description="Dataset file with extension (.csv, .xlsx, .parquet)",
    ),
    particle_type: str = Form(
        ..., title="Particle to predict", description="Should be p or he"
    ),
    model_type: str = Form(
        ..., title="Model for forecasting", description="Should be mlp or cnn"
    ),
):
    if file is None:
        raise HTTPException(400, "File is None type")

    validate_file_extension(file.filename)
    validate_particle_type(particle_type)
    validate_model_type(model_type)

    try:
        dataset = await load_dataframe_from_file(
            file, os.path.splitext(file.filename)[-1]
        )
        dataset = dataset.with_columns(pl.col("date").cast(pl.Datetime))
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"File: {file.filename} | Status: Error | Error info: Error when load: {e}",
        )

    try:
        processed_dataset, timestamp = model_inference(
            dataset, particle_type, model_type
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"File: {file.filename} | Status: Error | Error info: Error during process: {e}",
        )

    try:
        base_name, ext = os.path.splitext(file.filename)
        new_name = (
            base_name
            + f"_processed_using_{model_type}_to_predict_{particle_type}_at_{datetime.now().strftime('%Y-%m-%d %H:%M')}"
            + ext
        )
        save_dataframe(processed_dataset, new_name, ext)  # type: ignore
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"File: {file.filename} | Status: Error | Error info: Error during save: {e}",
        )

    return {
        "File": file.filename,
        "Status": "Success",
        "Processed in, s": timestamp,
        "Saved to": os.path.join(FOLDER_TO_SAVE_RESULT.removeprefix("/app"), new_name),
    }
