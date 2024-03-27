from django.urls import path
from .views import *

urlpatterns = [
    path('room/', ChatRoomList.as_view(), name='romm-list'),
    path('<int:room_id>/messages/', ChatMessageList.as_view(), name='message-list'),
    path('chatting/', chat_html, name='chatting'),
]