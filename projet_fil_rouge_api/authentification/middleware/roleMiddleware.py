from fastapi import HTTPException, Request
from jose import jwt
from authentification.service.context import *
from .authentificationMiddleware import validate_token
from gestionColis.service.utilisateur import getByUsername


def check_role():
  try :
    toto = validate_token()
    print(toto.get("sub"))
  except :
      raise HTTPException(403, "Accès non autorisé")


