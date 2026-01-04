from fastapi import APIRouter
from services.projects_service import get_projects

projects_router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@projects_router.get("")
def get_projects_endpoint():
    return get_projects()
