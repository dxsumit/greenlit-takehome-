from pydantic import BaseModel
from typing import Optional, List

class FILM(BaseModel):
    title: str
    description: Optional[str] = None
    budget: int
    release_year: int
    genres: List[str]
    company_email: str

