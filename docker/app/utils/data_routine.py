import pickle
from sklearn.preprocessing import StandardScaler
import torch
import numpy as np


def preprocess(
    batch: list[dict] | dict, preprocessor: StandardScaler, device: torch.device
) -> torch.Tensor:
    if isinstance(batch, dict):
        batch = [batch]

    batch_values = [sample.values() for sample in batch]
    preprocessed_values = preprocessor.transform(np.array(batch_values))

    return torch.from_numpy(preprocessed_values).to(device)


def postprecess(batch: torch.Tensor, postprocessor: StandardScaler) -> list[dict]:
    postprecessed = postprocessor.inverse_transform(batch.detach().cpu().numpy())

    return [
        {f"bin_{i}": item for i, item in enumerate(row, 1)} for row in postprecessed
    ]
