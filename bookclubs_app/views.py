from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Club
from .serializers import ClubSerializer
from djoser.views import UserViewSet
from .models import UserProfile
from .serializers import UserProfileSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class CustomUserViewSet(UserViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # You can add authentication and permission settings here if needed
