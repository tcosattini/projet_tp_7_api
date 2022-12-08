from gestionColis.service.utilisateur import getByUsername
from .context import pwd_context, access_token_expires
from .authentification import create_access_token
from fastapi import HTTPException

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
  try :
    user = getByUsername(username)["response"]   
    if not user:
        raise HTTPException(403, "Mauvaise combinaison utilisateur, mot de passe")
    if not verify_password(password, user.password):
        raise HTTPException(403, "Mauvaise combinaison utilisateur, mot de passe")
    return user
  except Exception as exception :
      raise HTTPException(403, "Mauvaise combinaison utilisateur, mot de passe")

def comparePassword (validateObject) :
   user = authenticate_user(validateObject.username, validateObject.password)
   return user
 
def get_access_token (validateObject) :
  try:
   user = authenticate_user(validateObject.username, validateObject.password)
   token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
   return {"token" : token }
  except Exception as exception :
    raise exception
