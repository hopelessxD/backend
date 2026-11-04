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
@app.get('/')
def root():
    return {"message":"hello"}


@app.get('/users/{user_id}')
def get_user(user_id:int = Path(..., description="The ID you want to get", gt=0)):
    