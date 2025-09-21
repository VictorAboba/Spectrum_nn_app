from pydantic import BaseModel, Field
from datetime import datetime
from .constants import *


class PastSample(BaseModel):
    date: datetime = Field(le=DATE_FORK)
    BRBG: float = Field(ge=0)
    THUL: float = Field(ge=0)
    TXBY: float = Field(ge=0)
    APTY: float = Field(ge=0)
    OULU: float = Field(ge=0)
    KERG: float = Field(ge=0)
    YKTK: float = Field(ge=0)
    MOSC: float = Field(ge=0)
    NVBK: float = Field(ge=0)
    LMKS: float = Field(ge=0)
    JUNG: float = Field(ge=0)
    AATB: float = Field(ge=0)
    MXCO: float = Field(ge=0)
    ATHN: float = Field(ge=0)
    Ap: float = Field(ge=0)
    SSN: float = Field(ge=0)
    A: float = Field(ge=-1, le=1)


class FutureSample(BaseModel):
    date: datetime = Field(gt=DATE_FORK)
    BRBG: float = Field(ge=0)
    MRNY: float = Field(ge=0)
    SOPO: float = Field(ge=0)
    THUL: float = Field(ge=0)
    TXBY: float = Field(ge=0)
    APTY: float = Field(ge=0)
    OULU: float = Field(ge=0)
    KERG: float = Field(ge=0)
    YKTK: float = Field(ge=0)
    MOSC: float = Field(ge=0)
    NVBK: float = Field(ge=0)
    LMKS: float = Field(ge=0)
    JUNG: float = Field(ge=0)
    AATB: float = Field(ge=0)
    MXCO: float = Field(ge=0)
    ATHN: float = Field(ge=0)
    PSNM: float = Field(ge=0)
    Ap: float = Field(ge=0)
    SSN: float = Field(ge=0)
    A: float = Field(ge=-1, le=1)
