# Gudieline

- Python 서버 어플리케이션 개발에서 많이 사용하는 프로젝트 구조를 따른다.
- Module로 리소스를 분리하여 관리한다.
- Rest API를 제공하여 Database의 데이터를 조회하여 가공 후 등록하는 서버 어플리케이션이다.
- 한글을 사용할 수 있도록 UTF-8를 이용한다.

# Database

- `./entity-prompt.md`

# Feature

## 원본 뉴스를 조회하여 데이터를 전처리 후 가공 뉴스를 저장한다.

- API 

method: POST
URL: /api/filter/{jobId}

- JobID로 해당 해당 원로 뉴스를 조회한다.
- `tms_raw_stream`의 데이터를 `convert_hanja_to_hangul`를 이용하여 데이터를 가공한다.
- FilteredNews에 가공한 데이터를 등록한다.


