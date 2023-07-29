from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.modules.items.schemas import Item
from app.modules.items import deps
from app.modules.items.service import ItemService

router = APIRouter()


@router.get("/", response_model=List[Item])
def read_items(db: Session = Depends(deps.get_db)) -> Any:
    """ Returns a list of items.
    Using Inversion of Control (IoC) to inject the database session.
    Passing the database session to the service layer.

    Args:
        db (Session, optional): _description_. Defaults to Depends(deps.get_db).

    Returns:
        Any: _description_
    """

    service = ItemService(db)

    return service.get_items()
