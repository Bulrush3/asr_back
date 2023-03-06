from datetime import date
from typing import List

from pydantic import BaseModel


class OperationBase(BaseModel):
    date: date
    title: str
    minTitle: str
    backImage: str
    logoImage: str
    tags: List[str]
    category: str

class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True

class OperationCreate(OperationBase):
    pass

class OperationUpdate(OperationBase):
    pass