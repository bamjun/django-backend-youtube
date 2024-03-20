from django.urls import path
from .views import *

urlpatterns = [
    path('', VideoList.as_view(), name='video-list'),
    path('<int:pk>/', VideoDetail.as_view(),name='video-detail'),
]

