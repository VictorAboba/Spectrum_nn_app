from typing import Literal

import pickle
import torch
import polars as pl
from pydantic import ValidationError

from .data_schemes import PastSample, FutureSample
from .data_routine import postprocess, preprocess
from .constants import *


def timer(func):
    from time import time

    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()

        return result, end - start

    return wrapper


@timer
def model_inference(
    dataset: pl.DataFrame,
    particle_type: Literal["p", "he"],
    model_type: Literal["mlp", "cnn"],
    pbar=None,
) -> pl.DataFrame:
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    if particle_type == "p":
        if model_type == "mlp":
            PAST_MODEL_PATH = P_PAST_MLP_MODEL_PATH
            FUTURE_MODEL_PATH = P_FUTURE_MLP_MODEL_PATH
        else:
            PAST_MODEL_PATH = P_PAST_CNN_MODEL_PATH
            FUTURE_MODEL_PATH = P_FUTURE_CNN_MODEL_PATH
        PAST_PROCESSOR_PATH = P_PAST_PROCESSORS_PATH
        FUTURE_PROCESSOR_PATH = P_FUTURE_PROCESSORS_PATH
    else:
        if model_type == "mlp":
            PAST_MODEL_PATH = HE_PAST_MLP_MODEL_PATH
            FUTURE_MODEL_PATH = HE_FUTURE_MLP_MODEL_PATH
        else:
            PAST_MODEL_PATH = HE_PAST_CNN_MODEL_PATH
            FUTURE_MODEL_PATH = HE_FUTURE_CNN_MODEL_PATH
        PAST_PROCESSOR_PATH = HE_PAST_PROCESSORS_PATH
        FUTURE_PROCESSOR_PATH = HE_FUTURE_PROCESSORS_PATH

    # ****************************************past
    past_model = torch.jit.load(PAST_MODEL_PATH).to(device)
    past_model.eval()
    with open(PAST_PROCESSOR_PATH, "rb") as file:
        processors = pickle.load(file)
    past_preprocessor = processors[0]
    past_postprocessor = processors[1]
    # ****************************************future
    future_model = torch.jit.load(FUTURE_MODEL_PATH).to(device).eval()
    future_model.eval()
    with open(FUTURE_PROCESSOR_PATH, "rb") as file:
        processors = pickle.load(file)
    future_preprocessor = processors[0]
    future_postprocessor = processors[1]
    # ***********************************model usage
    result = []
    for i, sample in enumerate(dataset.iter_rows(named=True)):
        if pbar:
            pbar.progress((i + 1) / len(dataset))
        if isinstance(sample, dict):
            sample = [sample]
        try:
            valid_sample = [
                FutureSample.model_validate(item).model_dump() for item in sample
            ]
            preprocessed_data = preprocess(valid_sample, future_preprocessor, device)
            prediction = future_model(preprocessed_data)
            postprocessed_data = postprocess(
                prediction, future_postprocessor, particle_type
            )
        except ValidationError:
            valid_sample = [
                PastSample.model_validate(item).model_dump() for item in sample
            ]
            preprocessed_data = preprocess(valid_sample, past_preprocessor, device)
            prediction = past_model(preprocessed_data)
            postprocessed_data = postprocess(
                prediction, past_postprocessor, particle_type
            )
        except Exception as e:
            raise Exception(f"Error during process row({sample}): {e}") from e

        for x, y in zip(sample, postprocessed_data):
            x.update(y)

        result += sample

    return pl.DataFrame(result)
