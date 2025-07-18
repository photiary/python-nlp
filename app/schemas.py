# schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ProcessingResponse(BaseModel):
    success: bool
    message: str
    processed_count: int
    total_count: Optional[int] = None
    errors: Optional[List[str]] = None

class RawNewsResponse(BaseModel):
    id: int
    news_id: str
    title: str
    content: Optional[str] = None
    published_at: Optional[datetime] = None
    provider: Optional[str] = None
    category: Optional[str] = None
    tms_raw_stream: Optional[str] = None

class FilteredNewsResponse(BaseModel):
    id: int
    title: str
    tms_raw_stream: Optional[str] = None
    raw_news_id: int 