from ..service import conditionnement
from fastapi import APIRouter,Depends
from gestionColis.schema import *
from authentification.middleware.authentificationMiddleware import *

router = APIRouter(
    prefix="/conditionnement",
    tags=["conditionnement"],
    responses={404: {"description": "Not found"}},
    # dependencies= [Depends (validate_token)]
)

@router.get("/")
def getAllConditionnement():
   return conditionnement.getAll()

@router.post("/",status_code=201)
def createConditionnement(validateObject: Conditionnement):
    return conditionnement.create(validateObject)
            
@router.put("/{idcondit}")
def updateConditionnement(validateObject: Conditionnement,idcondit):
    return conditionnement.update(idcondit,validateObject)

@router.delete("/{idcondit}")
def deleteConditionnement(idcondit):
    return conditionnement.delete(idcondit)
