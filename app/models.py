# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class RawNews(Base):
    __tablename__ = "batch_biz_raw_news"
    id = Column(Integer, primary_key=True)
    news_id = Column(String)
    title = Column(String)
    tms_raw_stream = Column(String)
    # ... (필요한 컬럼 추가)
    filtered_news = relationship("FilteredNews", uselist=False, back_populates="raw_news")

class FilteredNews(Base):
    __tablename__ = "batch_biz_filtered_news"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    tms_raw_stream = Column(String)
    raw_news_id = Column(Integer, ForeignKey("batch_biz_raw_news.id"), unique=True)
    raw_news = relationship("RawNews", back_populates="filtered_news")

class BatchJobRawNews(Base):
    __tablename__ = "batch_biz_batch_job_raw_news"
    id = Column(Integer, primary_key=True)
    batch_job_id = Column(Integer)
    raw_news_id = Column(Integer, ForeignKey("batch_biz_raw_news.id"))
    raw_news = relationship("RawNews")