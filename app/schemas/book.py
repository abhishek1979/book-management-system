from typing import Optional
from fastapi import Path, Query
from pydantic import BaseModel, Field

class Book(BaseModel):
    book_id: str = Field(..., description="Book Unique ID Number", examples=["B001"])
    title: str = Field(..., description="The full title of the book", examples=["Hands-On Large Language Model"])
    author: str = Field(..., description="Tha Author of the book", examples=["Jay Alamar"])
    price: float = Field(..., description="The Price of the book", examples=[1000])
    count: int = Field(..., description="No of Book Available in Library", examples=[5])
    is_available: bool = Field(..., description="Is Book Available in Library or Not", examples=[True, False])