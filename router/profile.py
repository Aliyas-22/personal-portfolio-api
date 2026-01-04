from fastapi import APIRouter
from services.profile_service import get_profile_details

profile_router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)

@profile_router.get("")
def get_profile():
    return get_profile_details()
