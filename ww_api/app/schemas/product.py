from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    thumbnail_url: Optional[str] = None
    base_url: Optional[str] = None
    price: Optional[int] = None
    archived: Optional[bool] = False

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductInResponse(ProductBase):
    id: int