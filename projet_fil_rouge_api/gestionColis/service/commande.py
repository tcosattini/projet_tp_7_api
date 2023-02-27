from ..models import TEntcde
from fastapi import HTTPException
from django.core.paginator import Paginator
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
    response =[]
    commandes = TEntcde.objects.filter(codcli=codcli)

    for command in commandes :
      response.append(command)
    return {"response":response}  
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

