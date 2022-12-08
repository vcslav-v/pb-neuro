from fastapi import APIRouter
from pb_neuro.api.local_routes import api

routes = APIRouter()

routes.include_router(api.router, prefix='/api')
