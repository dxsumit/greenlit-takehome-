from pydantic import BaseModel

class USER(BaseModel):
    first_name: str
    last_name: str
    email: str
    minimum_fee: int

