from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {
    1:{
        "name": "ram",
        "age" : 28
    }
}

#base pydantic models
class User(BaseModel):
    name:str
    website:str
    age:int
    role:str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None
    age: Optional[int] = None
    role: Optional[str] = None
    
    
@app.get('/')
def root():
    return {"message":"hello"}


@app.get('/users/{user_id}')
def get_user(user_id:int = Path(..., description="The ID you want to get", gt=0)):
    if user_id not in users:
        raise HTTPException(status_code = 404, detail = "User not found")
    return users[user_id]

@app.post("/users/{user_id}", status_code = status.HTTP_201_CREATED)
def create_user(user_id:int,user:User):
    if user_id in users:
        raise HTTPException(status_code = 404, detail = "User already exists")
    
    users[user_id] = user.dict()
    return user


@app.put("/users/{user_id}")
def update_user(user_id:int,user:UpdateUser):
    if user_id not in users:
        raise HTTPException(status_code = 404, detail = "User not found")
    
    current_user = users[user_id]
    
    update_data = user.model_dump(exclude_unset = True)
    
    for key,value in update_data.items():
        current_user[key] = value
    
    return current_user