from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommoentSerializer

class VideoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comment_set = CommoentSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = "__all__"

        depth = 1