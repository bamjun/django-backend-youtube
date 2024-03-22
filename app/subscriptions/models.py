from django.db import models
from common.models import CommonModel
from users.models import User

# User: FK => subscriber (내가 구독한 사람) 100명  (잇섭이 채널을 삭제했어) -> 99명
# User: FK => subscribed_to (나를 구독한 사람) 1만명 -> 999명

# User:Subscription => User(subscriber) => subscriber, subscriber,


class Subscription(CommonModel):
    subscriber = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)
    subscribed_to = models.ForeignKey(User, related_name='subscribers', on_delete=models.CASCADE)

