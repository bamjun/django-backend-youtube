[교제 링크](https://visioneer.notion.site/Project1_Youtube-988b009559144545aa7e2ab4eb354d6c)  

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