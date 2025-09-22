from sklearn.preprocessing import StandardScaler
import torch
import numpy as np
from typing import Literal


def preprocess(
    batch: list[dict] | dict, preprocessor: StandardScaler, device: torch.device
) -> torch.Tensor:
    if isinstance(batch, dict):
        batch = [batch]

    batch_values = [list(sample.values()) for sample in batch]
    preprocessed_values = preprocessor.transform(np.array(batch_values))

    return torch.from_numpy(preprocessed_values).to(device)


def postprocess(
    batch: torch.Tensor, postprocessor: StandardScaler, prefix: Literal["p", "he"]
) -> list[dict]:
    postprocessed = postprocessor.inverse_transform(batch.detach().cpu().numpy())

    return [
        {f"{prefix}_bin_{i}": item for i, item in enumerate(row, 1)}
        for row in postprocessed
    ]
