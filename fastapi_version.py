from fastapi import FastAPI
from pydantic import BaseModel

class UserData(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get('/')
async def root():
    return 'GET Request Succeed!'

@app.get('/users')
async def get_users(page: int = 1, limit: int = 10):
    return {
        'users': ['Saka', 'Rice', 'Saliba', 'Timber'],
        'page': page,
        'limit': limit
    }

@app.post('/echo')
async def post_echo(data: UserData):
    return f'You send {data}'