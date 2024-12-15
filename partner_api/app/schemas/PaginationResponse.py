from pydantic import BaseModel
from typing import List

class PaginatedResponse(BaseModel):
    total: int
    page: int
    size: int
    items: List[dict]