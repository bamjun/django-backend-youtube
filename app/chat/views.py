from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

def chat_html(request):
    return render(request, 'index.html')

class ChatRoomList(APIView):
    def get(self, request):
        chatrooms = ChatRoom.objects.all()  # objs -> json (직렬화)
        serializer = ChatRoomSerializer(chatrooms, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        user_data = request.data # 유저가 보내준 데이터 저장하기  
        serializer = ChatRoomSerializer(data=user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChatMessageList(APIView):
    def get(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom)
        serializer = ChatMessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, room_id):
        user_data = request.data
        chatroom = get_object_or_404(ChatRoom, id=room_id)

        serializer = ChatMessageSerializer(data=user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(room=chatroom, sender=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ChatRomm
## api/v1/chat
## ChatRoomList
### [GET] : 전체 채팅방 조회  // AUTH - request.user
### [POST] : 채팅방 생성


# ChatRoomDetail
## api/v1/chat/{int:room_id}
### [PUT] : 채팅방 관련 수정 ex) 채팅방 제목 수정, 인원수 제한 등
### [DELETE] : 해당 채팅방 삭제


# ChatMessage
## ChatMessageList
### [GET] : 채팅 내역 조회
### [POST] : 채팅 메세지 생성