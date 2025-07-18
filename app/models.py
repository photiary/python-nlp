# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class RawNews(Base):
    __tablename__ = "batch_biz_raw_news"
    id = Column(Integer, primary_key=True)
    news_id = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False)
    content = Column(String)
    published_at = Column(DateTime)
    enveloped_at = Column(DateTime)
    dateline = Column(String)
    provider = Column(String)
    category = Column(String)
    category_incident = Column(String)
    hilight = Column(String)
    byline = Column(String)
    images = Column(String)
    images_caption = Column(String)
    provider_subject = Column(String)
    subject_info = Column(String)
    subject_info1 = Column(String)
    subject_info2 = Column(String)
    subject_info3 = Column(String)
    subject_info4 = Column(String)
    provider_news_id = Column(String)
    publisher_code = Column(String)
    provider_link_page = Column(String)
    printing_page = Column(String)
    tms_raw_stream = Column(Text)
    
    # Relationships
    batch_job_raw_news = relationship("BatchJobRawNews", back_populates="raw_news", cascade="all, delete-orphan")
    filtered_news = relationship("FilteredNews", back_populates="raw_news", uselist=False, cascade="all, delete-orphan")

class FilteredNews(Base):
    __tablename__ = "batch_biz_filtered_news"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    tms_raw_stream = Column(Text)
    raw_news_id = Column(Integer, ForeignKey("batch_biz_raw_news.id"), unique=True)
    raw_news = relationship("RawNews", back_populates="filtered_news")

class BatchJobRawNews(Base):
    __tablename__ = "batch_biz_batch_job_raw_news"
    id = Column(Integer, primary_key=True)
    batch_job_id = Column(Integer, nullable=False)
    raw_news_id = Column(Integer, ForeignKey("batch_biz_raw_news.id"), nullable=False)
    raw_news = relationship("RawNews", back_populates="batch_job_raw_news")