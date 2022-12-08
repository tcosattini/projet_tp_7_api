from ..service import utilisateur
from fastapi import APIRouter,Depends
from authentification.middleware.authentificationMiddleware import *
from gestionColis.schema import *


router = APIRouter(
    prefix="/utilisateur",
    tags=["utilisateur"],
    responses={404: {"description": "Not found"}},
    dependencies= [Depends (validate_token)]
)

@router.get("/")
def getAllUtilisateur():    
   return utilisateur.getAll()

@router.get("/{username}")
def getByIdUtilisateur(username):
    return utilisateur.getByUsername(username)    

@router.post("/",status_code=201)
def createUtilisateur(validateObject: Utilisateur):
    return utilisateur.create(validateObject)
            
@router.put("/{code_utilisateur}")
def updateUtilisateur(validateObject: Utilisateur,code_utilisateur):
    return utilisateur.update(code_utilisateur,validateObject)

@router.delete("/{code_utilisateur}")
def deleteUtilisateur(code_utilisateur):
    return utilisateur.delete(code_utilisateur)
