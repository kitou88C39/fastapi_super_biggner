from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}

# パスパラメータ
from fastapi import FastAPI

app = FastAPI()

@app.get("/contries")
async def contry():
    return {"contry_name": contry_name}