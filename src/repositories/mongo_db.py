# Repository related code in here
from pymongo import MongoClient


class MongoDb():
    def __init__(
            self, database: str, collection: str, client_params: str | None = None) -> MongoClient:
        self.client = MongoClient(**client_params)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def get_db(self):
        return self.db

    def get_collection(self):
        return self.collection
