# services.py
from sqlalchemy.orm import Session
from models import RawNews, FilteredNews, BatchJobRawNews
from filters import convert_hanja_to_hangul
from typing import List, Optional

class NewsProcessingService:
    
    @staticmethod
    def get_raw_news_by_job_id(db: Session, job_id: int) -> List[RawNews]:
        """JobID로 해당 원본 뉴스를 조회한다."""
        return db.query(RawNews).join(BatchJobRawNews).filter(
            BatchJobRawNews.batch_job_id == job_id
        ).all()
    
    @staticmethod
    def process_raw_news_to_filtered(db: Session, raw_news: RawNews) -> Optional[FilteredNews]:
        """원본 뉴스를 가공하여 FilteredNews로 변환한다."""
        
        # 이미 처리된 뉴스인지 확인
        existing_filtered = db.query(FilteredNews).filter(
            FilteredNews.raw_news_id == raw_news.id
        ).first()
        
        if existing_filtered:
            return existing_filtered
        
        # tms_raw_stream 데이터를 한자에서 한글로 변환
        processed_tms_raw_stream = convert_hanja_to_hangul(raw_news.tms_raw_stream)
        
        # FilteredNews 생성
        filtered_news = FilteredNews(
            title=raw_news.title,
            tms_raw_stream=processed_tms_raw_stream,
            raw_news_id=raw_news.id
        )
        
        return filtered_news
    
    @staticmethod
    def process_job_news(db: Session, job_id: int) -> dict:
        """JobID로 원본 뉴스를 조회하여 가공 후 FilteredNews에 저장한다."""
        
        # JobID로 원본 뉴스 조회
        raw_news_list = NewsProcessingService.get_raw_news_by_job_id(db, job_id)
        
        if not raw_news_list:
            return {
                "success": False,
                "message": f"Job ID {job_id}에 해당하는 원본 뉴스가 없습니다.",
                "processed_count": 0
            }
        
        processed_count = 0
        errors = []
        
        for raw_news in raw_news_list:
            try:
                # 뉴스 가공
                filtered_news = NewsProcessingService.process_raw_news_to_filtered(db, raw_news)
                
                if filtered_news:
                    # 이미 존재하지 않는 경우에만 저장
                    if not db.query(FilteredNews).filter(
                        FilteredNews.raw_news_id == raw_news.id
                    ).first():
                        db.add(filtered_news)
                        processed_count += 1
                
            except Exception as e:
                errors.append(f"뉴스 ID {raw_news.news_id} 처리 중 오류: {str(e)}")
        
        # 변경사항 저장
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            return {
                "success": False,
                "message": f"데이터베이스 저장 중 오류: {str(e)}",
                "processed_count": 0
            }
        
        return {
            "success": True,
            "message": f"Job ID {job_id}의 뉴스 처리 완료",
            "processed_count": processed_count,
            "total_count": len(raw_news_list),
            "errors": errors
        } 