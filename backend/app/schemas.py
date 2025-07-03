from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

class StudentBase(BaseModel):
    username: str
    name: str
    grade: Optional[int] = None
    school: Optional[str] = None

class StudentCreate(StudentBase):
    password: str

class Student(StudentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class AcademicRecordBase(BaseModel):
    semester: str
    subject: str
    score: float
    grade: str
    credit: int
    notes: Optional[str] = None

class AcademicRecordCreate(AcademicRecordBase):
    student_id: int

class AcademicRecord(AcademicRecordBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ActivityBase(BaseModel):
    activity_type: str
    title: str
    description: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    achievement: Optional[str] = None
    proof_document: Optional[str] = None

class ActivityCreate(ActivityBase):
    student_id: int

class Activity(ActivityBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
