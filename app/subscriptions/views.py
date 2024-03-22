from rest_framework.views import APIView
from .serializers import SubSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription
from django.shortcuts import get_object_or_404

# 구독 관련 rest api

# subscriptionList
# api/v1/subscription
# [POST] : 구독하기
class SubscriptionList(APIView):
    # ToDo: 유저가 구독하고 있는 유튜버의 리스트는 따로 해야 하나요? (현민)
    # - 내가 구독하고 있는 유튜버들 리스트 (내가 구독한)
    def get(self, request):
        subs = Subscription.objects.filter(subscriber=request.user)
        # objects -> json
        serializer = SubSerializer(subs, many=True)
        return Response(serializer.data)


    def post(self, request):
        user_data = request.data # json
        serializer = SubSerializer(data=user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)
        
        return Response(serializer.data, status.HTTP_201_CREATED)
    

# subscriptionDetail
# api/v1/subscription/{user_id}
# [GET] : 전체 구독자 조회
# [DELETE] : 구독취소
    
class SubscriptionDetail(APIView):
    def get(self, request, pk):
        subs = Subscription.objects.filter(subscribed_to=pk)

        serializer = SubSerializer(subs, many=True)

        return Response(serializer.data)

    def delete(self, request, pk):
        subs = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        subs.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)       
