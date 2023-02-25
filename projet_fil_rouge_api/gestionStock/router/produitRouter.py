from ..service import produit
from fastapi import APIRouter,Depends
from gestionStock.schema import *
from authentification.middleware.authentificationMiddleware import *



router = APIRouter(
    prefix="/produit",
    tags=["produit"],
    responses={404: {"description": "Not found"}},
    # dependencies= [Depends (validate_token)]    
)

@router.get("/")
# Paginate with 10 items per pages
def getAllProduit(page):
   return produit.getAll(page)

@router.post("/")
def createProduit(validateObject: Produit):
    return produit.create(validateObject)
            
@router.put("/{codobj}")
def updateProduit(validateObject: Produit,codobj):
    return produit.update(codobj,validateObject)

@router.delete("/{codobj}")
def deleteProduit(codobj):
    return produit.delete(codobj)
