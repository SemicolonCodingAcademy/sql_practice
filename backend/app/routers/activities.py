from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

@router.get("/")
def get_activities(db: Session = Depends(database.get_db)):
    return {"message": "활동 조회"}
