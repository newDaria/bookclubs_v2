from rest_framework import serializers
from .models import UserProfile, Club

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ('id', 'email', 'username','password')
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer

class UserProfileSerializer(DjoserUserCreateSerializer):
    class Meta(DjoserUserCreateSerializer.Meta):
        # Add any additional fields you want to include during registration here
        fields = ('email', 'username', 'password')


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'description', 'owner', 'members')

