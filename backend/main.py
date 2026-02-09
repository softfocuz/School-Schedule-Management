from scheduler import schedule
from fastapi import FastAPI
from routers.root import router as root_router

app = FastAPI()

app.include_router(root_router)
