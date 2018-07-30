from rest_framework import serializers
from . import models

class ImageSerializer(serializers.Serializer):

    class Meta:
        model = models.Image # iamge 모델 로드
        field = '__all__' #모든 필드를 

class CommentSerializer(serializers.Serializer):

    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.Serializer):

    class Meta:
        model = models.Like
        fields = '__all__'        