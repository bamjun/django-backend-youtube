from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import CommonModel
from users.models import User

class Video(CommonModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=50)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField() # S3 버킷에 저장하고, url 불러옴.  
    video_file = models.FileField(upload_to='storage/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # video_uploaded_url = models.URLField()
