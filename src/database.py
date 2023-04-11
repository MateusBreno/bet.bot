from pymongo.database import Database
from pymongo.collection import Collection
from pymongo import MongoClient
import time
import hashlib

users_schema = {
    "username": "",
    "password": "",
    "license": {
        "from_date": 0,
        "to_date": 0,
        "original_value": -1,
        "actual_value": 0.0,
    },
    "settings": {"stopWin": 0, "stopLoss": 0, "maxBet": 1},
    "filters": {"golsFilter": [False, [0, 0]], "maxTime": 90, "minOdd": 0.0},
    "search": [],
}


def criptografa(password: str):
    return hashlib.md5(password.encode("utf-8")).hexdigest()


class Mongo:
    def __init__(self, database: Database, users_collection: Collection):
        self.database = database
        self.Users_collection = users_collection

    # Resto do código omitido para brevidade


# Conexão banco de dados
client = MongoClient('autenticacao')
db = client['betbot']
collection = db['users'] 

MongoDB = Mongo(db, collection)

# Nome do usuário da conta da Bet e sua senha
# MongoDB.cadastrar("devbreno", "Palmeiras@2021")