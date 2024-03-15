#  Python 3.11이 설치된 Alpine Linux 3.19
# Alpine Linux는 경량화된 리눅스 배포판으로, 컨테이너 환경에 적합
FROM python:3.11-alpine3.19

# LABEL 명령어는 이미지에 메타데이터를 추가합니다. 여기서는 이미지의 유지 관리자를 "seopftware"로 지정하고 있습니다.
LABEL maintainer="seopftware"

# 환경 변수 PYTHONUNBUFFERED를 1로 설정합니다. 
# 이는 Python이 표준 입출력 버퍼링을 비활성화하게 하여, 로그가 즉시 콘솔에 출력되게 합니다. 
# 이는 Docker 컨테이너에서 로그를 더 쉽게 볼 수 있게 합니다.
ENV PYTHONUNBUFFERED 1

# 로컬 파일 시스템의 requirements.txt 파일을 컨테이너의 /tmp/requirements.txt로 복사합니다. 
# 이 파일은 필요한 Python 패키지들을 명시합니다.
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

# 리눅스 -> venv 
RUN python -m venv /py && \ 
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    # no-cache 캐시 부분을 사용안함.  
    apk add --update --no-cache postgresql-client && \
    # --virtual .tmp-build-deps 가상의 패키지 생성 명령어  
    apk add --update --no-cache --virtual .tmp-build-deps \
    # build-base 컴파일 도구
        build-base postgresql-dev musl-dev && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    # 설치하고 지우기 
    apk del .tmp-build-deps && \
    adduser \
        # 학습중이므로 페스워드는 패스..
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user