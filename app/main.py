from fastapi import FastAPI
from router.auth import login

app = FastAPI()

app.include_router(login.router)