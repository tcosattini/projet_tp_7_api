from fastapi import FastAPI
from gestionStock.schema import *
from gestionStock.router import produitRouter
from gestionColis.router import clientRouter, commandeRouter, utilisateurRouter,poidsCommandeRouter,poidsVignetteRouter, conditionnementRouter
from authentification.router import authentificationRouter

app = FastAPI()

app.include_router(produitRouter.router)
app.include_router(clientRouter.router)
app.include_router(commandeRouter.router)
app.include_router(utilisateurRouter.router)
app.include_router(poidsCommandeRouter.router)
app.include_router(poidsVignetteRouter.router)
app.include_router(conditionnementRouter.router)
app.include_router(authentificationRouter.router)
