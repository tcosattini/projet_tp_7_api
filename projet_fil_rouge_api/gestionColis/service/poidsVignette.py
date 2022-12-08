from ..models import TPoidsV
from django.core import serializers
from fastapi import HTTPException

def getAll():
 try:    
    response =[]
    serializers.deserialize("json", TPoidsV.objects.all())    
    for obj in TPoidsV.objects.all():
        response.append(obj)
    return {"response":response}    
 except: 
     raise HTTPException(status_code=404, detail="Poids vignette non trouvées")

def create(validateObject):
 try:   
    if (TPoidsV.objects.filter(valmin=validateObject.valmin)) :
     raise  HTTPException(status_code=426, detail="ce poids est déjà enregistré") 
    newPoidsCommande =  TPoidsV.objects.create(**validateObject.dict())
    return {"nouveau poids vignette ":newPoidsCommande}
 except:
    raise HTTPException(status_code=426, detail="Impossible de créer ce poids vignette")

def update(valmin,validateObject):
 try:
   
   findSelectedPoidsCommande = TPoidsV.objects.get(valmin=valmin)
   selectedPoidsCommande = TPoidsV.objects.filter(valmin=valmin).update(**validateObject.dict())
   findPoidsCommande = TPoidsV.objects.get(valmin=valmin)
   return {"poids vignette modifié avec succés" : findPoidsCommande}
 except:
    raise HTTPException(status_code=404, detail="poids vignette non trouvé")

def delete(valmin):
 try:
   findSelectedPoidsCommande = TPoidsV.objects.get(valmin=valmin)
   selectedPoidsCommande = TPoidsV.objects.filter(valmin=valmin).delete()
   return {"poids vignette supprimé avec succés"}
 except:
    raise HTTPException(status_code=404, detail="poids vignette non trouvé")
