from ..models import TObjet
from django.core.paginator import Paginator


def getAll(page):
 try: 
    response =[]
    productsFound = TObjet.objects.all()
    p = Paginator(productsFound, 10)
    for obj in p.page(page):
        response.append(obj)
    return {"response":response}
 except: 
    return {'produits non trouvés'}   

def create(validateObject): 
 try:       
   newProduit =  TObjet.objects.create(**validateObject.dict())
   return {"nouveau produit":newProduit}
 except:
    return {'impossible de créer ce produit'}  

def update(codobj,validateObject):
 try:
    # Lever exception si produit non trouvé
   selectedProduit = TObjet.objects.filter(codobj=codobj).update(**validateObject.dict())
   return {"produit modifié avec succés":selectedProduit}
 except:
    return {'impossible de modifier ce produit'}

def delete(codobj):
 try:
    # Lever exception si produit non trouvé
   selectedProduit = TObjet.objects.filter(codobj=codobj).delete()
   return {"produit supprimé avec succés":selectedProduit}
 except:
    return {'impossible de supprimer ce produit'}

