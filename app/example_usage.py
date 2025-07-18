#!/usr/bin/env python3
"""
뉴스 데이터 가공 REST API 사용 예제
"""

import requests
import json

def example_usage():
    base_url = "http://localhost:8001"
    
    print("=== 뉴스 데이터 가공 REST API 사용 예제 ===\n")
    
    # 1. 서버 상태 확인
    print("1. 서버 상태 확인")
    try:
        response = requests.get(f"{base_url}/")
        print(f"   상태 코드: {response.status_code}")
        print(f"   응답: {response.json()}")
    except requests.exceptions.ConnectionError:
        print("   오류: 서버에 연결할 수 없습니다. 서버가 실행 중인지 확인하세요.")
        return
    print()
    
    # 2. 원본 뉴스 조회
    print("2. Job ID 1의 원본 뉴스 조회")
    try:
        response = requests.get(f"{base_url}/api/raw-news/1")
        print(f"   상태 코드: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   조회된 뉴스 수: {data['count']}")
            if data['raw_news']:
                print(f"   첫 번째 뉴스: {data['raw_news'][0]['title']}")
            else:
                print("   조회된 뉴스가 없습니다.")
        else:
            print(f"   오류: {response.text}")
    except Exception as e:
        print(f"   오류: {str(e)}")
    print()
    
    # 3. 뉴스 데이터 가공
    print("3. Job ID 1의 뉴스 데이터 가공")
    try:
        response = requests.post(f"{base_url}/api/filter/1")
        print(f"   상태 코드: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   성공: {data['success']}")
            print(f"   메시지: {data['message']}")
            print(f"   처리된 뉴스 수: {data['processed_count']}")
            if data.get('total_count'):
                print(f"   전체 뉴스 수: {data['total_count']}")
            if data.get('errors'):
                print(f"   오류: {data['errors']}")
        else:
            print(f"   오류: {response.text}")
    except Exception as e:
        print(f"   오류: {str(e)}")
    print()
    
    print("=== API 문서 ===")
    print(f"Swagger UI: {base_url}/docs")
    print(f"ReDoc: {base_url}/redoc")

if __name__ == "__main__":
    example_usage() 