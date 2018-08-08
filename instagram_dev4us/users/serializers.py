from rest_framework import serializers
from . import models
from instagram_dev4us.images import serializers as image_serializers

class UserProfileSerializer(serializers.ModelSerializer):

    images = image_serializers.CountImageSerializer(many=True)
    post_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    
    class Meta:
        model = models.User
        fields = (
            'profile_image',
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'follwing_count',
            'images',
        )

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name',
        )
