from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class UserBase(BaseModel):
    id: int
    name: str


class UserOut(BaseModel):
    id: int
    name: str
    followers: List[UserBase] = []
    followings: List[UserBase] = []

    class Config:
        from_attributes = True
        populate_by_name = True
