from typing import Optional


from typing import Optional
from pydantic import BaseModel
from pydantic.types import PositiveInt

class Car(BaseModel):
    id: Optional[PositiveInt] = None
    maker: str
    model: str
    model_year: PositiveInt
