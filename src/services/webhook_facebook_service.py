from src.models.webhook_facebook_model import DataModel
from src.repositories.mongo_db import MongoDb


class WebhookFacebook():
    def __init__(self, data, repo=MongoDb(database="teste_db", collection="test_collection")):
        self.data = data
        self.model = DataModel(data=self.data)
        self.repo = repo
        self.collection = self.repo.get_collection()

    def check_data(self):
        if "test_id" not in self.data.keys():
            return {'content': 'Fail', 'status_code': 400}
        return {'content': 'ok', 'status_code': 200}

    def process_data(self):
        ...

    def save_data_db(self):
        self.collection.insert_one(self.model.model_dump())
