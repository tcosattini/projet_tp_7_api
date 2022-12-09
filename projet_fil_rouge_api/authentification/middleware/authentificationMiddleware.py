from fastapi import HTTPException, Request
from jose import jwt
from authentification.service.context import *



def validate_token(request : Request):
   token = request.headers.get('authorization','Bearer')
   tokenSanitized = token.replace("Bearer ", "")
   try :
      payload = jwt.decode(tokenSanitized, SECRET_KEY, algorithms=[ALGORITHM])
   except :
      raise HTTPException(403, "Accès non autorisé")

