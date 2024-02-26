from sqlalchemy import text, select
from sqlalchemy.orm import Session
from database.models import Base, User, Film, Company, user_film_table, user_company_table
from __init__ import engine, query



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.movie_routes import movie_router
from router.role_routes import role_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(movie_router)
app.include_router(role_router)

@app.get("/")
async def root():

    return {"message": "Hello World!????"}


