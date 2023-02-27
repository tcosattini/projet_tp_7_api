from ..service import poidsCommande
from fastapi import APIRouter,Depends
from gestionColis.schema import *
from authentification.middleware.authentificationMiddleware import *


router = APIRouter(
    prefix="/poidscommande",
    tags=["poidsCommande"],
    responses={404: {"description": "Not found"}},
    # dependencies= [Depends (validate_token)]
    
)

@router.get("/")
def getAllPoidsCommande():
   return poidsCommande.getAll()

@router.post("/",status_code=201)
def createPoidsCommande(validateObject: PoidsCommande):
    return poidsCommande.create(validateObject)
            
@router.put("/{val}")
def updatePoidsCommande(validateObject: PoidsCommande,val):
    return poidsCommande.update(val,validateObject)

@router.delete("/{val}")
def deletePoidsCommande(val):
    return poidsCommande.delete(val)
