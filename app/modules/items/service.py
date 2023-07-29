from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.modules.items import deps


class ItemService:

    def __init__(self, db: Session = Depends(deps.get_db)):
        self.db = db

    def get_items(self):
        return self.db.execute(text("SELECT * FROM items"))
