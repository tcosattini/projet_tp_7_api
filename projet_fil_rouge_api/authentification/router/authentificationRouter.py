from ..service import login
from fastapi import APIRouter
from ..schema import *

router = APIRouter(
    prefix="/login",
    tags=["authentification"],
    responses={404: {"description": "Not found"}},
)

@router.post("/",status_code=200)

def loginCheck(validateObject: User):    
    return login.get_access_token(validateObject)