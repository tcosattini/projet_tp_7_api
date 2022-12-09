from pydantic import BaseModel
from typing import Optional

class Client(BaseModel):
  genrecli: str
  nomcli: str
  prenomcli : str
  adresse1cli : str
  adresse2cli : Optional[str] = None
  adresse3cli : Optional[str] = None
  villecli : str
  emailcli : str
  portcli : Optional[str] = None
  newsletter : Optional[bool] = None
  id_commune_id : Optional[int] = None

class Commande(BaseModel):
  datcde: str
  codcli_id: int
  timbrecli : int
  timbrecde : int
  nbcolis : int
  cheqcli : int
  idcondit : Optional[int] = None
  cdecomt : Optional[int] = None
  barchive : Optional[int] = None
  bstock : bool
  id_dtl_commande_id : int

class DetailCommande(BaseModel):
  codcde: int
  codobj_id: int
  qte: int
  colis: int
  commentaire: Optional[str] = None

class Utilisateur(BaseModel):
  nom_utilisateur: Optional[str] = None
  prenom_utilisateur: Optional[str] = None
  couleur_fond_utilisateur: Optional[int] = None
  date_cde_utilisateur: Optional[str] = None
  is_superuser: bool
  code_role_id: Optional[int] = None
  username : str
  password : str
  role : list


class PoidsCommande(BaseModel):
  valmin: float
  valtimbre: Optional[float] = None

class PoidsVignette(BaseModel):
  valmin: float
  valtimbre: Optional[float] = None  

class Conditionnement(BaseModel):
  libcondit: str
  poidscondit: int
  prixcond: float
  ordreimp: int