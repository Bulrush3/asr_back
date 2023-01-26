from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel

class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'

class OperationBase(BaseModel):
    date: date
    kind: OperationKind
    amount: Decimal
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