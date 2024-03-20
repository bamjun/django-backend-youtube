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
    def get(self, request):
        videos = Video.objects.all() # QuerySet[video,video,video ...] 

        # 여러개 데이터일때 many=True 안하면 오류남.  
        serializer = VideoSerializer(videos, many=True)

        print(serializer)

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
        
from rest_framework.exceptions import NotFound
    
class VideoDetail(APIView):
    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise NotFound
        
        serializer = VideoSerializer(video)
        
        return Response(serializer.data)


    def put(self, request, pk):
        video_obj = Video.objects.get(pk=pk)
        user_data = request.data
        serializer = VideoSerializer(video_obj, user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)  #save 하려면 is_valid를 해야함.  
        return Response(serializer.data)
    

    def delete(self, request, pk):
        Video_obj = Video.objects.get(pk=pk)
        Video_obj.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
