from fastapi import FastAPI
from src.routers import login

app = FastAPI()
app.include_router(login.router)

@app.get("/hello")
async def hello():
    return {"message": "hello world!"}