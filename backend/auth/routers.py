from fastapi import APIRouter, Depends, status

from .services import AuthService
from .dependencies import get_auth_service


auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)

@auth_router.post('/registration', status_code=status.HTTP_201_CREATED)
async def registration_user(auth_service: AuthService = Depends(get_auth_service)):
    pass