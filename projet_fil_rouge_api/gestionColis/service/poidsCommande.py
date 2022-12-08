from ..models import TPoids
from django.core import serializers
from fastapi import HTTPException

def getAll():
 try:    
    response =[]
    serializers.deserialize("json", TPoids.objects.all())    
    for obj in TPoids.objects.all():
        response.append(obj)
    return {"response":response}    
 except: 
     raise HTTPException(status_code=404, detail="Poids commandes non trouvées")

def create(validateObject):
 try:   
    if (TPoids.objects.filter(valmin=validateObject.valmin)) :
     raise  HTTPException(status_code=426, detail="ce poids est déjà enregistré") 
    newPoidsCommande =  TPoids.objects.create(**validateObject.dict())
    return {"nouveau poids commande ":newPoidsCommande}
 except:
    raise HTTPException(status_code=426, detail="Impossible de créer ce poids commande")

def update(valmin,validateObject):
 try:
   
   findSelectedPoidsCommande = TPoids.objects.get(valmin=valmin)
   selectedPoidsCommande = TPoids.objects.filter(valmin=valmin).update(**validateObject.dict())
   findPoidsCommande = TPoids.objects.get(valmin=valmin)
   return {"poids commande modifié avec succés" : findPoidsCommande}
 except:
    raise HTTPException(status_code=404, detail="poids commande non trouvé")

def delete(valmin):
 try:
   findSelectedPoidsCommande = TPoids.objects.get(valmin=valmin)
   selectedPoidsCommande = TPoids.objects.filter(valmin=valmin).delete()
   return {"poids commande supprimé avec succés"}
 except:
    raise HTTPException(status_code=404, detail="poids commande non trouvé")
