from ..models import TEntcde,TDtlcode,TObjet
from fastapi import HTTPException
from django.core.paginator import Paginator

def getById(codcde):
 try:    
    response =[]
    dtlCommandes = []
    commandesList = []
    dtlObjet = []
    command = TEntcde.objects.get(codcde=codcde)
   
    relatedDetailCommandes = TDtlcode.objects.filter(codcde=command.codcde)
    for relatedDetailCommande in relatedDetailCommandes :
        dtlCommandes.append(relatedDetailCommande)
        setattr(command,"details",dtlCommandes)
        relatedProduits = TObjet.objects.filter(codobj= getattr(relatedDetailCommande,"codobj_id"))
        for relatedProduit in relatedProduits:
          dtlObjet.append(relatedProduit)
          setattr(relatedDetailCommande,"produit",relatedProduit)
        dtlObjet = []
    dtlCommandes =[]           
    commandesList.append(command) 

    return {"response":command}
 except:
    raise HTTPException(status_code=404, detail="Commandes non trouvées")


def getAll(page):
 try:    
    response =[]
    commandesFound = TEntcde.objects.all()
    c = Paginator(commandesFound, 10)
    for obj in c.page(page):
        response.append(obj)
    return {"response":response}
 except:
    raise HTTPException(status_code=404, detail="Commandes non trouvées")

def getRelatedCommandeClient(codcli):
 try:
    commandesList = []
    dtlCommandes = []
    dtlObjet = []
    commandes = TEntcde.objects.filter(codcli=codcli)
    for command in commandes :
      relatedDetailCommandes = TDtlcode.objects.filter(codcde=command.codcde)
      for relatedDetailCommande in relatedDetailCommandes :
        dtlCommandes.append(relatedDetailCommande)
        setattr(command,"details",dtlCommandes)
        relatedProduits = TObjet.objects.filter(codobj= getattr(relatedDetailCommande,"codobj_id"))
        for relatedProduit in relatedProduits:
          dtlObjet.append(relatedProduit)
          setattr(relatedDetailCommande,"produit",relatedProduit)
        dtlObjet = []
      dtlCommandes =[]           
      commandesList.append(command) 
    return {"response":commandesList}  
 except:
    raise HTTPException(status_code=404, detail="Client non trouvé")


def create(validateObject):
 try:   
    newCommande =  TEntcde.objects.create(**validateObject.dict())
    return {"nouvelle commande":newCommande}
 except:
    raise HTTPException(status_code=404, detail="Commandes non trouvées")
    
def delete(codcde):
 try:
   findSelectedDetailCommande = TEntcde.objects.get(codcde=codcde)
   selectedCommande = TEntcde.objects.filter(codcde=codcde).delete()
   return {"commande supprimée avec succés"}
 except:
    raise HTTPException(status_code=404, detail="Commande non trouvée")


def update(codcde,validateObject):
 try:
   findSelectedCommande = TEntcde.objects.get(codcde=codcde)
   selectedCommande = TEntcde.objects.filter(codcde=codcde).update(**validateObject.dict())
   findUpdatedCommande = TEntcde.objects.get(codcde=codcde)
   return {"commande modifiée avec succés":findUpdatedCommande}
 except:
    raise HTTPException(status_code=404, detail="Commande non trouvée")

