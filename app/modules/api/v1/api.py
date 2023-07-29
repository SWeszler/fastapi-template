from fastapi import APIRouter

from app.modules.items import routes

api_router = APIRouter()
api_router.include_router(routes.router, prefix="/items", tags=["items"])
