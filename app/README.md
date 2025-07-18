# 뉴스 데이터 가공 REST API

원본 뉴스를 조회하여 데이터를 전처리 후 가공 뉴스를 저장하는 REST API 서버입니다.

## 기능

- JobID로 해당 원본 뉴스를 조회
- `tms_raw_stream`의 데이터를 `convert_hanja_to_hangul`를 이용하여 데이터를 가공
- FilteredNews에 가공한 데이터를 등록

## 데이터베이스 설정

- PostgreSQL
- Port: 54320
- Database: mydatabase
- User: myuser
- Password: secret

## API 엔드포인트

### 1. 뉴스 데이터 가공 API

**POST** `/api/filter/{job_id}`

JobID로 해당 원본 뉴스를 조회하여 데이터를 전처리 후 가공 뉴스를 저장합니다.

**요청:**
- `job_id` (path parameter): 처리할 배치 작업 ID

**응답:**
```json
{
  "success": true,
  "message": "Job ID 1의 뉴스 처리 완료",
  "processed_count": 5,
  "total_count": 10,
  "errors": []
}
```

### 2. 원본 뉴스 조회 API

**GET** `/api/raw-news/{job_id}`

JobID로 해당 원본 뉴스를 조회합니다.

**요청:**
- `job_id` (path parameter): 조회할 배치 작업 ID

**응답:**
```json
{
  "job_id": 1,
  "count": 10,
  "raw_news": [
    {
      "id": 1,
      "news_id": "NEWS001",
      "title": "뉴스 제목",
      "provider": "뉴스 제공자",
      "category": "카테고리"
    }
  ]
}
```

## 설치 및 실행

1. 의존성 설치:
```bash
pip install -r requirements.txt
```

2. 서버 실행:
```bash
python run_server.py
```

3. API 문서 확인:
- Swagger UI: http://localhost:8001/docs
- ReDoc: http://localhost:8001/redoc

## 데이터베이스 테이블

### RawNews (batch_biz_raw_news)
원본 뉴스 데이터를 저장하는 테이블

### FilteredNews (batch_biz_filtered_news)
가공된 뉴스 데이터를 저장하는 테이블

### BatchJobRawNews (batch_biz_batch_job_raw_news)
배치 작업과 원본 뉴스의 관계를 저장하는 테이블

## 데이터 처리 과정

1. JobID로 `BatchJobRawNews` 테이블을 통해 관련된 원본 뉴스를 조회
2. 각 원본 뉴스의 `tms_raw_stream` 필드를 한자에서 한글로 변환
3. 변환된 데이터를 `FilteredNews` 테이블에 저장
4. 처리 결과를 JSON 형태로 반환

## 에러 처리

- 데이터베이스 연결 오류
- JobID에 해당하는 뉴스가 없는 경우
- 데이터 처리 중 발생하는 오류
- 중복 처리 방지 (이미 처리된 뉴스는 건너뜀) 