from typing import List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import json
from fastapi import APIRouter 
import os

router= APIRouter()

class Team(BaseModel):
    nom_joueur:str
    type_joueur:str
    num_joueur:int

def chargeJson(pathJson: str) -> List[Team]:
    if not os.path.exists(pathJson):
        raise HTTPException(status_code=404, detail="Le fichier JSON n'existe pas.")
    
    with open(pathJson, 'r') as fichier:
        # Charger les données JSON depuis le fichier
        donnees = json.load(fichier)
        teams = [Team(**team) for team in donnees]
    return teams

file_path = '/data/data_teams.json'
teams = chargeJson(file_path)

app = FastAPI()

# Route pour obtenir tous les éléments
@router.get("/teams/", response_model=List[Team])
async def read_taems():
    return teams