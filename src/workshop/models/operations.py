from datetime import date
from enum import Enum
from typing import List

from pydantic import BaseModel

class OperationKind(str, Enum):
    INCOME = 'game'
    OUTCOME = 'not game'

class OperationBase(BaseModel):
    date: date
    kind: OperationKind
    title: str
    minTitle: str
    backImage: str
    logoImage: str
    tags: List[str]

class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True

class OperationCreate(OperationBase):
    pass

class OperationUpdate(OperationBase):
    pass