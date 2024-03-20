from rest_framework.test import APITestCase

from users.models import User

from .models import Video
from rest_framework import status

from django.urls import reverse

from django.core.files.uploadedfile import SimpleUploadedFile

import pdb # python debugger

class VideoAPITestCase(APITestCase):
    # 테스트 코드가 실행되기 전 동작하는 함수
    # - 데이터를 만들어줘야한다. (1) 유저 생성/로그인 -> (2) 비디오 생성

    def setUp(self):
        self.user = User.objects.create_user(email='user1@example.com', password='test123')
        
        self.client.login(email='user1@example.com', password='test123')

        self.video = Video.objects.create(title='test video', link='http://www.test.com/', user = self.user)


    # 127.0.0.1:8000/api/v1/video [GET]
    def test_video_list_get(self):
        url = reverse('video-list')
        res = self.client.get(url)  # 전체 비디오 조회 데이터  

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.headers['Content-Type'], 'application/json')
        self.assertEqual(len(res.data) > 0, True)
        
        # title 컬럼이 응답 데이터에 잘 들어가 있는지 확인. 
        for video in res.data:
            self.assertIn('title', video)

        

    def test_video_list_post(self):
        url = reverse('video-list') # api/v1/video

        data = {
            'title': 'test video2',
            'link': 'http://test.com',
            'category': 'test category',
            'thumbnail': 'http://test.com',
            # 'video_uploaded_url': 'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4', b'file_content', 'video/mp4'),
            'user': self.user.pk,
        }

        res = self.client.post(url, data)

        # pdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'test video2')



    # 특정 비디오 조회
    def test_video_detail_get(self):
        url = reverse('video-detail', kwargs={'pk': self.video.pk}) # api/vi/video/<int:pk>/
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        

    def test_video_detail_put(self):
        url = reverse('video-detail', kwargs={'pk': self.video.pk})

        data = {
            'title': 'updated video',
            'link': 'http://test.com',
            'category': 'test category',
            'thumbnail': 'http://test.com',
            # 'video_uploaded_url': 'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4', b'file_content', 'video/mp4'),
            'user': self.user.pk,
        }
        res = self.client.put(url, data)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'], 'updated video')

    def test_video_detail_delete(self):
        url = reverse('video-detail', kwargs={'pk': self.video.pk})

        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)