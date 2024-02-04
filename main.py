from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}

# パスパラメータ 1
from fastapi import FastAPI

app = FastAPI()

@app.get("/contries/{country_name}")
async def country(contry_name: int):
    return {"contry_name": contry_name}

# パスパラメータ 2
from fastapi import FastAPI

app = FastAPI()

@app.get("/contries/japan}")
async def japan():
    return {"message": 'This is Japan!'}

@app.get("/contries/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}