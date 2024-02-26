from pydantic import BaseModel

class USER_COMP(BaseModel):
    user_email: str 
    value1: str
    company_email: str
    value2: str
    role: str

