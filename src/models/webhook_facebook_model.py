from pydantic import BaseModel
from datetime import datetime


class DataModel(BaseModel):
    created_at: datetime = datetime.today()
    updated_at: datetime | None = None
    data: dict | list
    history: list[str] = []
    status: str = "Pending"

    def update_status(self, status: str, history: str):
        self.status = status
        self.add_history(history)

    def add_history(self, msg):
        self.history.append(msg)
