#!/usr/bin/env python3
"""
뉴스 데이터 가공 REST API 서버 실행 스크립트
"""

import uvicorn
import sys
import os

# app 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

if __name__ == "__main__":
    print("뉴스 데이터 가공 REST API 서버를 시작합니다...")
    print("API 문서: http://localhost:8001/docs")
    print("서버 중지: Ctrl+C")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_level="info"
    ) 