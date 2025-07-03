from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

@router.get("/")
def get_grades(db: Session = Depends(database.get_db)):
    return {"message": "성적 조회"}
