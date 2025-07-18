from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import hanja

from database import get_db, create_tables
from services import NewsProcessingService
from schemas import ProcessingResponse

app = FastAPI(title="뉴스 데이터 가공 API", description="원본 뉴스를 조회하여 데이터를 전처리 후 가공 뉴스를 저장하는 API")

# 애플리케이션 시작 시 테이블 생성
@app.on_event("startup")
async def startup_event():
    create_tables()

@app.get("/")
async def root():
    text = "한글 테스트"
    result = hanja.translate(text, 'substitution')
    return {"message": "Hello World!!", "value": result}

@app.post("/api/filter/{job_id}", response_model=ProcessingResponse)
async def filter_news_by_job_id(job_id: int, db: Session = Depends(get_db)):
    """
    JobID로 해당 원본 뉴스를 조회하여 데이터를 전처리 후 가공 뉴스를 저장한다.
    
    - **job_id**: 처리할 배치 작업 ID
    """
    try:
        result = NewsProcessingService.process_job_news(db, job_id)
        return ProcessingResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"서버 오류: {str(e)}")

@app.get("/api/raw-news/{job_id}")
async def get_raw_news_by_job_id(job_id: int, db: Session = Depends(get_db)):
    """
    JobID로 해당 원본 뉴스를 조회한다.
    """
    try:
        raw_news_list = NewsProcessingService.get_raw_news_by_job_id(db, job_id)
        return {
            "job_id": job_id,
            "count": len(raw_news_list),
            "raw_news": [
                {
                    "id": news.id,
                    "news_id": news.news_id,
                    "title": news.title,
                    "provider": news.provider,
                    "category": news.category
                }
                for news in raw_news_list
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"서버 오류: {str(e)}")