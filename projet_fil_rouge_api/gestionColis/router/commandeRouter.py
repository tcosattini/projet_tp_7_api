from ..service import commande, detailCommande
from fastapi import APIRouter,Depends
from gestionColis.schema import *
from authentification.middleware.authentificationMiddleware import *

router = APIRouter(
    prefix="/commande",
    tags=["commande"],
    responses={404: {"description": "Not found"}},
    dependencies= [Depends (validate_token)]
)

@router.get("/")
def getAllCommande():
   return commande.getAll()

@router.post("/",status_code=201)
def createCommande(validateObject: Commande):
    return commande.create(validateObject)

@router.get("/client/{codecli}")
def getRelatedCommandeClient(codecli):
    return commande.getRelatedCommandeClient(codecli)    
            
@router.put("/{codcde}")
def updateCommande(validateObject: Commande,codcde):
    return commande.update(codcde,validateObject)

@router.delete("/{codcde}")
def deleteCommande(codcde):
    return commande.delete(codcde)

@router.get("/detail")
def getAllCommande():
   return detailCommande.getAll()

@router.post("/detail",status_code=201)
def createCommande(validateObject: DetailCommande):
    return detailCommande.create(validateObject)
            
@router.put("/detail/{id_dtl_commande}")
def updateCommande(validateObject: DetailCommande,id_dtl_commande):
    return detailCommande.update(id_dtl_commande,validateObject)

@router.delete("/detail/{id_dtl_commande}")
def deleteCommande(id_dtl_commande):
    return detailCommande.delete(id_dtl_commande)
