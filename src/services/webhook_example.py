from src.repositories.mongo_db import MongoDb


class WebhookExample():
    def __init__(self, repo=MongoDb(database="example_db", collection="example_collection")):
        self.repo = repo

    def save_data_db(self):
        ...

    def process_data(self):
        ...

    def update_date_db(self):
        ...

    def proces_webhook(self):
        self.save_data_db()
        self.process_data()
        self.update_date_db()

    ...
