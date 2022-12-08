from ..service import client
from fastapi import APIRouter,Depends
from gestionColis.schema import *
from authentification.middleware.authentificationMiddleware import *

router = APIRouter(
    prefix="/client",
    tags=["client"],
    responses={404: {"description": "Not found"}},
    dependencies= [Depends (validate_token)]
)

@router.get("/")
def getAllClient():
   return client.getAll()

@router.post("/",status_code=201)
def createClient(validateObject: Client):
    return client.create(validateObject)
            
@router.put("/{codcli}")
def updateClient(validateObject: Client,codcli):
    return client.update(codcli,validateObject)

@router.delete("/{codecli}")
def deleteClient(codecli):
    return client.delete(codecli)
