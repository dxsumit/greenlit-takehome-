from pydantic import BaseModel

class USER_FILM(BaseModel):
    user_email: str 
    value1: str
    film_title: str
    value2: str
    role: str

