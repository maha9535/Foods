from pydantic import BaseModel

class Foods_schema(BaseModel):
    food_name: str
    price: int
    qty: int
    availability: bool