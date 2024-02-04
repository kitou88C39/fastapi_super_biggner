from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}

# パスパラメータ 1
from fastapi import FastAPI

app = FastAPI()

@app.get("/contries/{country_name}")
async def contry(contry_name: int):
    return {"contry_name": contry_name}

# パスパラメータ 2
from fastapi import FastAPI

app = FastAPI()

@app.get("/contries/japan}")
async def contry(contry_name: str):
    return {"message": 'This is Japan!'}

@app.get("/contries/{country_name}")
async def contry(contry_name: str):
    return {"contry_name": contry_name}