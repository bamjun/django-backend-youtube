from django.db import models
from common.models import CommonModel
from django.db.models import Q, Count
#
#  Create your models here.

# - User: FK
# - Video: FK
# - reactions (like, dislike, cancel) => choice

class Reaction(CommonModel):
    # circular import error 방지하기위해서 직접 모델 import 대신에 문자로 불러오기  
    # from users.models import User
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 위에꺼 대신에 아래로, ForeignKey에 문자열로 모델 지정가능.  
    # user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction')
    )

    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION
    )

    @staticmethod  # ORM depth2
    def get_video_reaction(video):
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk', filter=Q(reaction=Reaction.LIKE)),
            dislikes_count = Count('pk', filter=Q(reaction=Reaction.DISLIKE))
        )
        return reactions



