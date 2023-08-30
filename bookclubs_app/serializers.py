from rest_framework import serializers
from .models import UserProfile, Club

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ('id', 'email', 'username','password')
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer

class UserProfileSerializer(DjoserUserCreateSerializer):
    age = serializers.IntegerField(required=True)
    job = serializers.CharField(max_length=255, required=True)
    phone_number = serializers.CharField(max_length=15, required=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'description', 'owner', 'members')

