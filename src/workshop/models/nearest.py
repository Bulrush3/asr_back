
from typing import List

from pydantic import BaseModel


class NearestBase(BaseModel):
    date: int
    tags: List[str]

class Nearest(NearestBase):
    id: int

    class Config:
        orm_mode = True

class NearestCreate(NearestBase):
    pass

class NearestUpdate(NearestBase):
    pass