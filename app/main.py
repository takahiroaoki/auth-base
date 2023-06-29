from fastapi import FastAPI

from router.auth import login
from router.crud import read

app = FastAPI()

app.include_router(login.router)
app.include_router(read.router)