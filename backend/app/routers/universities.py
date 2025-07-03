from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

@router.get("/")
def get_universities(db: Session = Depends(database.get_db)):
    return {"message": "대학 정보 조회"}
