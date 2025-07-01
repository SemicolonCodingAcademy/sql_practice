from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from ..config import settings

router = APIRouter()
client = OpenAI(api_key=settings.OPENAI_API_KEY)

class StudentInfo(BaseModel):
    gpa: float
    activities: str
    achievements: str
    target_universities: str

class AdvisorResponse(BaseModel):
    analysis: str
    recommendations: str

@router.post("/api/analyze", response_model=AdvisorResponse)
async def analyze_profile(student_info: StudentInfo):
    try:
        prompt = f"""
        학생 프로필:
        - GPA: {student_info.gpa}
        - 활동: {student_info.activities}
        - 수상실적: {student_info.achievements}
        - 지원 희망 대학: {student_info.target_universities}

        위 학생의 프로필을 분석하고, 다음 사항을 한국어로 상세히 설명해주세요:
        1. 각 대학별 합격 가능성 분석
        2. 프로필의 강점과 약점
        3. 개선이 필요한 부분과 구체적인 조언
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 전문적인 대학 입학 상담가입니다."},
                {"role": "user", "content": prompt}
            ]
        )

        analysis = response.choices[0].message.content
        
        return AdvisorResponse(
            analysis=analysis,
            recommendations="개선 필요 사항: " + analysis.split("개선이 필요한 부분")[1] if "개선이 필요한 부분" in analysis else ""
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
