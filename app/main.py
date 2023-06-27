from fastapi import FastAPI
from router import login

app = FastAPI()

app.include_router(login.router)