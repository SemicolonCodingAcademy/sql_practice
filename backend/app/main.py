from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from pathlib import Path 
from sqlalchemy.orm import Session
from . import models, schemas, database
from .routers import grades, activities, universities, profile

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 정적 파일과 템플릿 설정
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

# 라우터 등록
app.include_router(grades.router, prefix="/api/grades", tags=["grades"])
app.include_router(activities.router, prefix="/api/activities", tags=["activities"])
app.include_router(universities.router, prefix="/api/universities", tags=["universities"])
app.include_router(profile.router, prefix="/api/profile", tags=["profile"])

# 데이터베이스 의존성
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/dashboard")
async def get_dashboard(db: Session = Depends(get_db)):
    # 대시보드 데이터 조회 로직
    return {
        "overall_gpa": 4.2,
        "target_gpa": 4.3,
        "recent_activities": [],
        "todos": []
    }

@app.get("/api/recent-activities")
async def get_recent_activities(db: Session = Depends(get_db)):
    # 최근 활동 조회 로직
    return []

@app.get("/api/todos")
async def get_todos(db: Session = Depends(get_db)):
    # 할 일 목록 조회 로직
    return []

@app.get("/api/application-status")
async def get_application_status(db: Session = Depends(get_db)):
    # 지원 현황 조회 로직
    return {
        "progress": 60,
        "completed": 3,
        "planned": 2,
        "interested": 5
    }

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
