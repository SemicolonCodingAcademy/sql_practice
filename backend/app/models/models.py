from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, Date, Text, TIMESTAMP
from sqlalchemy.sql import func
from .database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password_hash = Column(String(255))
    name = Column(String(100))
    grade = Column(Integer)
    school = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

class AcademicRecord(Base):
    __tablename__ = "academic_records"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    semester = Column(String(20))
    subject = Column(String(50))
    score = Column(Float)
    grade = Column(String(2))
    credit = Column(Integer)
    notes = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    activity_type = Column(Enum('교내활동', '교외활동', '수상실적', '봉사활동', '자격증', '어학성적'))
    title = Column(String(200))
    description = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    achievement = Column(Text)
    proof_document = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())
