from rest_framework.test import APITestCase
from users.models import User
from django.urls import reverse
from rest_framework import status
from .models import Subscription
from rest_framework import status



class SubscriptionTestCase(APITestCase):
    # 테스트코드 실행시 가장먼저 실행되는 함수.  
    # 데이터 생성.  
    # 2명의 유저 데이터 생성, 1명의 유저 로그인
    def setUp(self):
        self.user1 = User.objects.create_user(email='test1', password='password123')
        self.user2 = User.objects.create_user(email='test2', password='password123')

        self.client.login(email='test1', password='password123')
        

    # 구독 버튼 테스트
    # [POST] api/v1/sub
    def test_sub_list_post(self):
        url = reverse('sub-list')

        # Subscription 모델 데이터
        data = {
            'subscriber' : self.user1.pk,
            'subscribed_to' : self.user2.pk,
        }

        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.get().subscribed_to, self.user2)
        self.assertEqual(Subscription.objects.count(), 1)



    
    # 특정 유저의 구독자 리스트  
    # [GET] api/v1/sub/{user_id}
    def test_sub_detail_get(self):
        Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)
        url = reverse('sub-detail', kwargs={'pk': self.user2.pk})

        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['subscribed_to'], self.user2.id)
        



    # 구독 취소 
    # [DELETE] api/v1/sub/{user_id}
    def test_sub_detail_delete(self):
        sub = Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)

        url = reverse('sub-detail', kwargs={'pk': sub.id})

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.count(), 0)


        
