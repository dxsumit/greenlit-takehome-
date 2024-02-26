from pydantic import BaseModel
from typing import Optional

class COMPANY(BaseModel):
    name: str
    contact_email: str
    phone_number: str

