FROM python:3.12-slim

# 기본 패키지 설치
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

# 가상환경 기본 경로 지정 (devcontainer 호환)
ENV VIRTUAL_ENV=/workspace/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 작업 디렉토리
WORKDIR /workspace

# pip 최신화 및 wheel 설치
RUN pip install --upgrade pip wheel

# 설치
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

CMD ["bash"]