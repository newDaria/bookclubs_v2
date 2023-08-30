from rest_framework import serializers
from .models import UserProfile, Club
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer


class UserProfileSerializer(DjoserUserCreateSerializer):
    age = serializers.IntegerField(required=True)
    job = serializers.CharField(max_length=255, required=True)
    phone_number = serializers.CharField(max_length=15, required=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        return value


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'description', 'owner', 'members')
