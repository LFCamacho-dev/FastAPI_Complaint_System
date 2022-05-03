from fastapi import FastAPI, APIRouter
from resources.routes import api_router

app = FastAPI()
app.include_router(api_router)

