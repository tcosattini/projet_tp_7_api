from ..models import TUtilisateur
from django.core import serializers
from fastapi import HTTPException
from authentification.service.authentification import get_password_hash


def getAll():
 try:    
    response =[]
    serializers.deserialize("json", TUtilisateur.objects.all())
    for obj in TUtilisateur.objects.all():
       response.append(obj)
    return {"response":response}    
 except: 
    return {'utilisateurs non trouvés'}  

def getByUsername(username):
 try:      
    selectedUser = TUtilisateur.objects.get(username=username)
    return {"response": selectedUser}
 except: 
    return {'utilisateur non trouvé'}      


def create(validateObject):
 try:
   if TUtilisateur.objects.filter(username=validateObject.username):
      raise HTTPException(status_code=426, detail="cet utilisateur est déjà enregistré") 
   validateObject.password = get_password_hash(validateObject.password)
   newUtilisateur =  TUtilisateur.objects.create(**validateObject.dict())
   return {"nouvel utilisateur":newUtilisateur}
 except Exception as exception:
   raise HTTPException(exception.status_code, exception.detail)

def update(code_utilisateur,validateObject):
 try:
   findSelectedUtilisateur = TUtilisateur.objects.get(code_utilisateur=code_utilisateur)
   selectedDetailUtilisateur = TUtilisateur.objects.filter(code_utilisateur=code_utilisateur).update(**validateObject.dict())
   findUpdatedUtilisateur = TUtilisateur.objects.get(code_utilisateur=code_utilisateur)
   return {"utilisateur modifié avec succés" : findUpdatedUtilisateur}
 except:
    raise HTTPException(status_code=404, detail="utilisateur non trouvé")

def delete(code_utilisateur):
 try:
   findSelectedUtilisateur = TUtilisateur.objects.get(code_utilisateur=code_utilisateur)
   selectedDetailUtilisateur = TUtilisateur.objects.filter(code_utilisateur=code_utilisateur).delete()
   return {"utilisateur supprimé avec succés"}
 except:
    raise HTTPException(status_code=404, detail="utilisateur non trouvé")