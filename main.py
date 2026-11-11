# Importation de la classe FastAPI permettant de créer une API web
from fastapi import FastAPI

# Importation de BaseModel pour définir et valider les données reçues
from pydantic import BaseModel


# Création de l'instance principale de l'application FastAPI
app = FastAPI()


# Définition d'un modèle de données nommé "decompte"
# Cette classe hérite de BaseModel (Pydantic)
# FastAPI utilise ce modèle pour :
# - valider automatiquement les données reçues ;
# - convertir les types si nécessaire ;
# - générer automatiquement la documentation de l'API.
class decompte(BaseModel):

    # Déclaration des champs attendus dans le corps de la requête
    # Tous les champs doivent être de type float
    AP: float
    IRG: float
    MC: float
    SS: float
    SIT_FAMILLIALE:bool
    ANNEE:str




# Définition d'une route HTTP POST accessible à l'URL :
# http://localhost:8000/decompte
@app.post("/decompte")
def creer_situation_decompte(decompte: decompte):
    """
    Cette fonction reçoit un objet JSON correspondant au modèle 'decompte'.

    Exemple de requête :
    {
        "AP": 1000,
        "IRG": 0.15,
        "MC": 500,
        "SS": 100,
        "SIT_FAMILLIALE":1,
        "ANNEE":2026
    }

    FastAPI convertit automatiquement ce JSON en objet 'decompte'.

    La fonction retourne le résultat du calcul :
    MC × IRG
    """

    MC=0

    match decompte.SIT_FAMILLIALE:
        
        case 1:
                MC=3000
        
        case 0:
            
        
                MC=0
       
        case _:
            return "Année non prise en charge"


    match decompte.ANNEE:
        
        case "1999":
            return {"Calcule année "+decompte.ANNEE: decompte.MC * decompte.IRG," Majoration Conjoint":MC}
        
        case "2000":
            return {"Calcule année "+decompte.ANNEE: decompte.MC * decompte.IRG," Majoration Conjoint":MC}
        
        case "2025":
            return {"Calcule année "+decompte.ANNEE: decompte.MC * decompte.IRG," Majoration Conjoint":MC}
        
        case "2026":
                    return {"Calcule année "+decompte.ANNEE: decompte.MC * decompte.IRG," Majoration Conjoint":MC}
         

        
        case _:
            return "Année non prise en charge"



    return decompte.MC * decompte.IRG