from ..service import poidsVignette
from fastapi import APIRouter,Depends,Security
from gestionColis.schema import *
from authentification.middleware.authentificationMiddleware import *

router = APIRouter(
    prefix="/poidsvignette",
    tags=["poidsVignette"],
    responses={404: {"description": "Not found"}},
    dependencies= [Depends (validate_token)]   
)

@router.get("/")
def getAllPoidsVignette():
   return poidsVignette.getAll()

@router.post("/",status_code=201)
def getAllPoidsVignette(validateObject: PoidsVignette):
    return poidsVignette.create(validateObject)
            
@router.put("/{val}")
def updatePoidsCommande(validateObject: PoidsVignette,val):
    return poidsVignette.update(val,validateObject)

@router.delete("/{val}")
def deletePoidsCommande(val):
    return poidsVignette.delete(val)
