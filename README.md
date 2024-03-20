[교제 링크](https://visioneer.notion.site/Project1_Youtube-988b009559144545aa7e2ab4eb354d6c)  
[깃링크](https://github.com/Seopftware/django-backend-youtube2)  

# instruction  
1. 폴더생성  
2. 깃허브 레포지토리 생성 연결  
   - 프로젝트 폴더 생성 전  
     - 깃허브 홈페이지에서 프로젝트 생성 후 
     - 로컬로 와서 git clone [프로젝트 주소]
   - 프로젝트 폴더 생성 후 
     - 깃허브 홈페이지에서 프로젝트 생성 후  
     - 로컬로 와서 깃연결 커멘드 입력  
     `bash shell`
     ```bash  
     git init  
     git add .  
     git commit -m 'first'  
     git branch -M 'main'  
     git remote add orign [깃주소]  
     git push -u origin main  
     ```

3. 도커 허브 설치  
   - 나의 컴퓨터어 가상환경 구축 (윈도우, 맥 > 리눅스 환경 구축(MySQL, Python, Redis))
   - 도커 허브 가입해서, 시크릿키 설정  
   ![alt text](images/markdown-image-1.png)  
   ![alt text](images/markdown-image-2.png)  
   ![alt text](images/markdown-image-3.png)  
   ![alt text](images/markdown-image-4.png)  

4. 장고 프로젝트 생성  
   - requirments.txt => 실제 배포할 때 사용  
   - requirments.dev.txt => 개발하고 연습할 때 사용 (파이썬 패키지관리)  
     - flake8 (Python 프로그래밍 언어로 작성된 코드의 스타일 가이드 준수 여부, 문법적 오류, 복잡성 등을 검사하는 도구)  
   - 실전 : 패키지 의존성 관리 중요 => 버전관리, 패키지들 간의관계 관리  
     - 장고 5.0 -> drf 3.0  설치를 원할때 서로 충돌하면 안됨..  

5. 도커 빌드  

# cicd 깃허브 설정하기 .  
![alt text](images/markdown-image-5.png)  
- 깃허브에 푸쉬 후  
![alt text](images/markdown-image-6.png)  


6. POSTGREsql  
   - 주요 특징 MVCC  
   ![alt text](images/markdown-image-7.png)  

   -마리아db와 포스트그래sql 차이  
     - 마리아 db는 쓰기가 강함  
   ![alt text](images/markdown-image-8.png)  
   - 포스트그래는 읽기에 강함  
   ![alt text](images/markdown-image-9.png)  

   - 프라이머리와 세컨더리 인덱스: 프라이머리 인덱스는 데이터베이스에서 각 레코드를 고유하게 식별하는 주요 수단입니다. 세컨더리 인덱스는 추가적인 검색 조건을 빠르게 처리할 수 있도록 도와주지만, 동시에 쓰기 작업 시 성능 저하의 원인이 될 수도 있습니다.  
   
   - 장고에 다른 데이터 베이스 적용시 공식문서 확인하기 [링크](https://docs.djangoproject.com/en/5.0/ref/databases/)  
   ![alt text](images/markdown-image-10.png)  

   - 도커 허브에서 다운로드  
   ![alt text](images/markdown-image-11.png)  
   - 리눅스 알파인 버전을 사용중이므로 해당 버전 다운  
   ![alt text](images/markdown-image-12.png)  

   docker-compose.yml

7. 코어 앱생성  
   - docker-compose run --rm app sh -c "python manage.py startapp core"

8. 장고 명령어 커스텀 [공식페이지](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/)  
   - 
   

9. 장고모델 만들기  
    users, videos, reactions, comments, subscriptions, common
    - docker-compose run --rm app sh -c 'python manage.py startapp users'
    - docker-compose run --rm app sh -c 'python manage.py startapp videos'
    - docker-compose run --rm app sh -c 'python manage.py startapp reactions'
    - docker-compose run --rm app sh -c 'python manage.py startapp comments'
    - docker-compose run --rm app sh -c 'python manage.py startapp subscriptions'
    - docker-compose run --rm app sh -c 'python manage.py startapp common'

10. custom user model create  
    - TTD 방식 개발 및 디버깅 시간을 엄청나게 줄일 수 있습니다. PDB(python debugger)  

11. DjangoRestframework, drf-spectacular [공식페이지](https://pypi.org/project/drf-spectacular/) 설치하기
- 
- docker-compose

12. 깃허브 엑션연결  
![alt text](images/markdown-image-13.png)  
  
![alt text](images/markdown-image-15.png)  
  
![alt text](images/markdown-image-14.png)  

13. 비디오 뷰 만들기  
  - Video와 관련된 REST API  
  - 1.VideoList  
  - api/v1/video  
  - [GET]: 전체 비디오 목록 조회  
  - [POST]: 새로운 비디오 생성  
  - [PUT]: X  
  - [DELETE]: X  

<br>  

  - 2. VideoDetail  
  - api/v1/video/{video_id}  
  - [GET]: 특정 비디오 조회  
  - [POST]: X  
  - [PUT]: 특정 비디오 업데이트  
  - [DELETE]: 특정 비디오 삭제  

14. 비디오 테스트 코드 작성.  


15. pdb 
- import pdb # python debugger  
![alt text](images/markdown-image-16.png)  


16. dbshell
- $ docker-compose run --rm app sh -c 'python manage.py dbshell'  
  ![alt text](images/markdown-image-17.png)  
  
17. 유저 시리얼 라이저 적용..  
    ![alt text](images/markdown-image-18.png)  




- docker-compose run --rm app sh -c 'python manage.py showmigrations users'


- docker-compose up


주말 공부
- 도커 배운 것 정리
- 유튜브 데이터베이스 모델 구조 고민해오기
- u 구독은 어떻게 하지? 좋아요는? 싫어요는? 어디에 담지? 비디오는? 댓글은?


공군 사보시고 강의도 1번 해보시고 . aws 보다 나았다면 다행입니다 . 고생하셨고요 . 어 너무 삽질 많이 하시고 잘 안되시면 저한테 연락 주시면 제가 바로 돈 드릴게요 여러분 . 아 예 저 오전에 고생하셨습니다 . 



----  

`ARG DEV=false` 명령어는 Dockerfile 내에서 빌드 시간에 사용되는 인자(argument)를 정의합니다. 이 구문은 `DEV`라는 인자에 기본값으로 `false`를 할당합니다. Docker 이미지를 빌드할 때 `--build-arg` 옵션을 사용하여 이 값을 오버라이드할 수 있습니다. 이를 통해 동일한 Dockerfile을 사용하여 다양한 설정의 이미지를 생성할 수 있습니다.

예를 들어, 개발 환경에 필요한 추가적인 Python 패키지들이 `requirements.dev.txt` 파일에 명시되어 있고, 이 패키지들을 이미지에 포함시키고 싶은 경우, `DEV` 인자를 `true`로 설정하여 이미지를 빌드할 수 있습니다. 그렇게 하면 Dockerfile 내의 조건문이 이 값을 검사하고, `true`일 경우 `requirements.dev.txt`에 명시된 개발용 의존성을 설치하는 명령어가 실행됩니다.

Docker 이미지를 빌드할 때 `DEV` 인자를 `true`로 설정하는 예제 명령어는 다음과 같습니다:
```bash
docker build --build-arg DEV=true -t my_image_name .
```
이 명령어는 `DEV` 인자를 `true`로 설정하여 Docker 이미지를 빌드하며, 이로 인해 개발 의존성이 포함된 이미지가 생성됩니다. 반면, `--build-arg DEV=false`를 지정하거나 `--build-arg`를 생략하면 `DEV`의 기본값인 `false`가 사용되어, 개발 의존성 없이 이미지가 빌드됩니다.  

---  

1. .flake8 [공식 페이지](https://peps.python.org/pep-0008/)  
   - 파이썬 코드 스타일 강제 & 디버깅 도움  





### CI CD  
![alt text](images/markdown-image.png)  


프로젝트

1. Youtube REST API
● db 설계 (모델 구조)
• 유튜브 데이터 크롤링 → DB 넣가

· DB: Postgre SQL

• 기능:

○ 유튜브 REST API ⇒ DRF
○ 소켓 연결을 통한 실시간 채팅 기능 구현 (방 기능까지)
o 영상 스트리밍

○ 영상을 시청 ⇒ 시청 데이터 ⇒ 추천 알고리즘 (모델링) - FastAPI

2. Youtube Dashboard
● ELK(Elasticsearch, Logstash, Kibana) Stack을 활용한 로그 데이터 시각화

3. Youtube Creator Support
· OpenAI API -> FastAPI
• 유튜브 컨텐츠를 만들 수 있도록 도와주는
• OpenAIl API를 활용해서 썸네일 및 스크립트 제작


# to ask
airbrige


# 질문
디비에서 1;N  N;N 으로 변경할경우..