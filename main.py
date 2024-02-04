from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}

# パスパラメータ
from fastapi import FastAPI

app = FastAPI()

@app.get("/contries/{country_name}")
async def contry(contry_name):
    return {"contry_name": contry_name}