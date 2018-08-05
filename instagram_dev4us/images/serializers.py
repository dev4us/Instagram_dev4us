from rest_framework import serializers
from . import models
from instagram_dev4us.users import models as user_models

class SmallImageSerializer(serializers.ModelSerializer):
    """ Used for the notifications """
    class Meta:
        model = models.Image
        fields = (
            'file',
        )

class CountImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count',
        )

class FeedUserSerialize(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image',
        )

class CommentSerializer(serializers.ModelSerializer):
    creator = FeedUserSerialize(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator',
        )

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__'        

class ImageSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    creator = FeedUserSerialize()

    class Meta:
        model = models.Image # iamge 모델 로드
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'like_count',
            'creator',
        )

