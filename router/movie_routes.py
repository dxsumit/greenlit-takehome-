from fastapi import APIRouter
from typing import List, Union
from models.user import USER
from models.company import COMPANY
from models.film import FILM
from __init__ import engine, query
from database.models import User, Film, Company

movie_router = APIRouter(
    prefix="/movies"
)

# get methods of tables.
@movie_router.get("/users")
async def get_users(limit: Union[int, None] = None):
    res = query.read_data(engine=engine, table=User, limit=limit)
    if res:
        return {"message": "success", "data": res}
    else:
        return {"message": "Failed", "message": "Not Found"}
    

@movie_router.get("/films")
async def get_films(limit: Union[int, None] = None):
    res = query.read_data(engine=engine, table=Film, limit=limit)
    if res:
        return {"message": "success", "data": res}
    else:
        return {"message": "Failed", "message": "Not Found"}
    

@movie_router.get("/companies")
async def get_companies(limit: Union[int, None] = None):
    res = query.read_data(engine=engine, table=Company, limit=limit)
    if res:
        return {"message": "success", "data": res}
    else:
        return {"message": "Failed", "message": "Not Found"}





# post methods of tables.
@movie_router.post("/user")
async def create_user(user: USER):
    req = {}
    for key, val in user:
        req[key] = val

    res = query.insert_data(engine=engine, table=User, data=req)
    if res == "success":
        return {"message": "success", "data": req}
    else:
        return {"message": "Failed", "message": "Failed to insert"}


@movie_router.post("/company")
async def create_company(company: COMPANY):
    req = {}
    for key, val in company:
        req[key] = val

    res = query.insert_data(engine=engine, table=Company, data=req)
    if res == "success":
        return {"message": "success", "data": req}
    else:
        return {"message": "Failed", "message": "Failed to insert"}
    





# update method of tables.
@movie_router.put("/user")
async def update_user(req: dict):
    if req.get("identifyer", 0) and req.get("value", 0) and req.get("data", 0):
        res = query.update_data(engine=engine, table=User, param=req["identifyer"], value=req["value"], data=req["data"])
    
        if res == "success":
            return {"message": "success", "data": req.get("data")}
        else:
            return {"message": "Failed", "message": "Failed to update"}

    else:
        return {"message": "Failed", "message": "request is not correct"}
    

@movie_router.put("/company")
async def update_company(req: dict):
    if req.get("identifyer", 0) and req.get("value", 0) and req.get("data", 0):
        res = query.update_data(engine=engine, table=Company, param=req["identifyer"], value=req["value"], data=req["data"])
    
        if res == "success":
            return {"message": "success", "data": req.get("data")}
        else:
            return {"message": "Failed", "message": "Failed to update"}

    else:
        return {"message": "Failed", "message": "request is not correct"}
    

@movie_router.put("/film")
async def update_film(req: dict):
    if req.get("identifyer", 0) and req.get("value", 0) and req.get("data", 0):
        res = query.update_data(engine=engine, table=Film, param=req["identifyer"], value=req["value"], data=req["data"])
    
        if res == "success":
            return {"message": "success", "data": req.get("data")}
        else:
            return {"message": "Failed", "message": "Failed to update"}

    else:
        return {"message": "Failed", "message": "request is not correct"}




# delete methods of tables
@movie_router.delete("/user")
async def delete_user(req: dict):
    if req.get("identifyer", 0) and req.get("value", 0):
        res = query.delete_data(engine=engine, table=User, param=req["identifyer"], value=req["value"])
    
        if res == "success":
            return {"message": "success", "data": {req["identifyer"], req["value"]}}
        else:
            return {"message": "Failed", "message": "Failed to delete"}
        
    else:
        return {"message": "Failed", "message": "request is not correct"}


@movie_router.delete("/company")
async def delete_company(req: dict):
    if req.get("identifyer", 0) and req.get("value", 0):
        res = query.delete_data(engine=engine, table=Company, param=req["identifyer"], value=req["value"])
    
        if res == "success":
            return {"message": "success", "data": {req["identifyer"], req["value"]}}
        else:
            return {"message": "Failed", "message": "Failed to delete"}
        
    else:
        return {"message": "Failed", "message": "request is not correct"}



@movie_router.delete("/film")
async def delete_film(req: dict):
    if req.get("identifyer", 0) and req.get("value", 0):
        res = query.delete_data(engine=engine, table=Film, param=req["identifyer"], value=req["value"])
    
        if res == "success":
            return {"message": "success", "data": {req["identifyer"], req["value"]}}
        else:
            return {"message": "Failed", "message": "Failed to delete"}
        
    else:
        return {"message": "Failed", "message": "request is not correct"}


