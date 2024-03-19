from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import VideoSerializer
from .models import Video

from rest_framework.response import Response

from rest_framework import status
# Create your views here.

# Video와 관련된 REST API
# 1.VideoList
# api/v1/video
# [GET]: 전체 비디오 목록 조회
# [POST]: 새로운 비디오 생성
# [PUT]: X
# [DELETE]: X

class VideoList(APIView):
    def get(self):
        videos = Video.objects.all() # QuerySet[video,video,video ...] 

        # 여러개 데이터일때 many=True 안하면 오류남.  
        serializer = VideoSerializer(videos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        user_data = request.data  # Json -> Object 역직렬화 (장고가 이해할수없다.)
        serializer = VideoSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2. VideoDetail
# api/v1/video/{video_id}
# [GET]: 특정 비디오 조회
# [POST]: X
# [PUT]: 특정 비디오 업데이트
# [DELETE]: 특정 비디오 삭제
    
class VideoDetail():
    def get():
        pass

    def put():
        pass

    def delete():
        pass








from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

# Create your views here.


# GET: 전체 리뷰 데이터 가져오기
class Reviews(APIView):
    def get(self, request):
        reviews = Review.objects.all() # 장고 객체

        # (Serializer) 장고 객체 -> JSON
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

# GET: 특정 리뷰 데이터 가져오기
class ReviewDetail(APIView):
    def get(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            raise NotFound

        serializer = ReviewSerializer(review)
        return Response(serializer.data)