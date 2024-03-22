from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

class Comment(CommonModel):
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    
    ## 대댓글
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    # - 이 필드가 null인 경우, 댓글은 '루트 댓글'이 됩니다. 
    # 만약 parent 필드가 다른 Comment 인스턴스를 가리킨다면, 해당 댓글은 대댓글이 됩니다.