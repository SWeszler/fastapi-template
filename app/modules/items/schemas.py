from typing import Optional
from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    title: str

    class Config:
        from_attributes = True


# Properties to return to client
class Item(ItemInDBBase):
    pass
