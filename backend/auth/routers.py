from fastapi import APIRouter, Depends, status

from .dependencies import get_auth_service
from .services import AuthService


auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)

@auth_router.post('/registration', status_code=status.HTTP_201_CREATED)
async def registration_user(auth_service: AuthService = Depends(get_auth_service)):
    pass