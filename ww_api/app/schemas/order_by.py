from enum import Enum

class OrderByCase(str, Enum):
    name = "name"
    description = "description"
    price = "price"