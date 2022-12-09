from ..models import TConditionnement
from django.core import serializers
from fastapi import HTTPException

def getAll():
 try:    
    response =[]
    serializers.deserialize("json", TConditionnement.objects.all())    
    for obj in TConditionnement.objects.all():
        response.append(obj)
    return {"response":response}
 except: 
     raise HTTPException(status_code=404, detail="Conditionement non trouvés")

def create(validateObject):
 try:   
    newDetailCommande =  TConditionnement.objects.create(**validateObject.dict())
    return {"nouveau conditionnement":newDetailCommande}
 except:
       raise HTTPException(status_code=500, detail="Impossible de créer ce conditionement")

def update(idcondit,validateObject):
 try:
   findSelectedConditionnement = TConditionnement.objects.get(idcondit=idcondit)
   selectedConditionnement = TConditionnement.objects.filter(idcondit=idcondit).update(**validateObject.dict())
   findUpdatedConditionnement = TConditionnement.objects.get(idcondit=idcondit)
   return {"Conditionement modifié avec succés" : findUpdatedConditionnement}
 except:
    raise HTTPException(status_code=404, detail="Conditionement non trouvé")

def delete(idcondit):
 try:
   findSelectedDetailCommande = TConditionnement.objects.get(idcondit=idcondit)
   selectedCommande = TConditionnement.objects.filter(idcondit=idcondit).delete()
   return {"Conditionement supprimé avec succés"}
 except:
    raise HTTPException(status_code=404, detail="Conditionement non trouvé")
