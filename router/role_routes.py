from fastapi import APIRouter
from models.user import USER
from models.company import COMPANY
from models.film import FILM
from models.user_film import USER_FILM
from models.user_company import USER_COMP
from __init__ import engine, query
from database.models import User, Film, Company, user_film_table, user_company_table

role_router = APIRouter(
    prefix="/roles"
)


# CRU on role..
# user and film.. Create

'''
{
    "user_email": "email",
    "value1": "post1@gmail.com",
    "film_title": "title",
    "value2": "Movie1",
    "role": "Director"
}
'''

@role_router.post("/user")
async def create_user(data: USER_FILM):
    req = {}
    for key, val in data:
        req[key] = val

    roles = {
        "writer": 1,
        "producer": 1,
        "director": 1,
    }

    if roles.get(req["role"],0):
        res = query.create_role_user_film(engine=engine,
                            table1=User, param1=req["user_email"], value1=req["value1"],
                            table2=Film, param2=req["film_title"], value2=req["value2"],
                            final_table=user_film_table, role=req["role"]
                            )

        if res == "success":
            return {"message": "success", "data": {"role": req["role"]}}
        else:
            return {"message": "Failed", "message": "Failed to insert"}
    
    else:
        return {"message": "Failed", "message": "Invalid role", "data": {"role": req["role"]}}
        

# user and film.. update

'''
{
    "value": 1,
    "data": {
        "role": "producer"
    }
}
'''
@role_router.put("/user")
async def update_user(req: dict):
    res = query.update_data(engine=engine, table=user_film_table, param='id', value=req.get("value"), data=req.get("data"))

    if res == "success":
        return {"message": "success", "data": {"role": req["data"]}}
    else:
        return {"message": "Failed", "message": "Failed to update"}    
    


# user and film.. print
@role_router.get("/user/{id}")
async def get_user(id: int):
    res = query.read_filtered_role(engine=engine, table=user_film_table, param='user_id', value=id)

    if res:
        return {"message": "success", "data": res}
    else:
        return {"message": "Failed", "message": "Failed to get"}    
    

# user and company.. Create
              
'''
{
    "user_email": "email",
    "value1": "post1@gmail.com",
    "company_email": "contact_email",
    "value2": "cmp99@gmail.com",
    "role": "Owner"
}
'''           
@role_router.post("/company")
async def create_company_user(data: USER_COMP):
    print(data)
    req = {}
    for key, val in data:
        req[key] = val

    roles = {
        "owner": 1,
        "member": 1
    }

    if roles.get(req["role"],0):
        res = query.create_role_user_company(engine=engine,
                            table1=User, param1=req["user_email"], value1=req["value1"],
                            table2=Company, param2=req["company_email"], value2=req["value2"],
                            final_table=user_company_table, role=req["role"]
                            )

        if res == "success":
            return {"message": "success", "data": {"role": req["role"]}}
        else:
            return {"message": "Failed", "message": "Failed to create"}
    
    else:
        return {"message": "Failed", "message": "Invalid role", "data": {"role": req["role"]}}
    


# user and film.. update

'''
{
    "value": 1,
    "data": {
        "role": "producer"
    }
}
'''
@role_router.put("/company")
async def update_company_user(req: dict):
    res = query.update_data(engine=engine, table=user_company_table, param='id', value=req.get("value"), data=req.get("data"))

    if res == "success":
        return {"message": "success", "data": {"role": req["data"]}}
    else:
        return {"message": "Failed", "message": "Failed to update"}    
    


# user and film.. print
@role_router.get("/company/{id}")
async def get_company_user(id: int):
    res = query.read_filtered_role(engine=engine, table=user_company_table, param='user_id', value=id)

    if res:
        return {"message": "success", "data": res}
    else:
        return {"message": "Failed", "message": "Failed to get"}    
    
