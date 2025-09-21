from pydantic import BaseModel, Field
from datetime import datetime
from .constants import *


class PastSample(BaseModel):
    date: datetime = Field(le=DATE_FORK)
    nm_0: float = Field(ge=0)
    nm_4: float = Field(ge=0)
    nm_5: float = Field(ge=0)
    nm_6: float = Field(ge=0)
    nm_8: float = Field(ge=0)
    nm_9: float = Field(ge=0)
    nm_10: float = Field(ge=0)
    nm_12: float = Field(ge=0)
    nm_13: float = Field(ge=0)
    nm_16: float = Field(ge=0)
    nm_17: float = Field(ge=0)
    nm_19: float = Field(ge=0)
    nm_22: float = Field(ge=0)
    nm_23: float = Field(ge=0)
    Ap: float = Field(ge=0)
    SSN: float = Field(ge=0)
    A: float = Field(ge=-1, le=1)


class FutureSample(BaseModel):
    date: datetime = Field(gt=DATE_FORK)
    nm_0: float = Field(ge=0)
    nm_2: float = Field(ge=0)
    nm_3: float = Field(ge=0)
    nm_4: float = Field(ge=0)
    nm_5: float = Field(ge=0)
    nm_6: float = Field(ge=0)
    nm_8: float = Field(ge=0)
    nm_9: float = Field(ge=0)
    nm_10: float = Field(ge=0)
    nm_12: float = Field(ge=0)
    nm_13: float = Field(ge=0)
    nm_16: float = Field(ge=0)
    nm_17: float = Field(ge=0)
    nm_19: float = Field(ge=0)
    nm_22: float = Field(ge=0)
    nm_23: float = Field(ge=0)
    nm_26: float = Field(ge=0)
    Ap: float = Field(ge=0)
    SSN: float = Field(ge=0)
    A: float = Field(ge=-1, le=1)
