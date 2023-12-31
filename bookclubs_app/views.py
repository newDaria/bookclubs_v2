# Create your views here.
from rest_framework import viewsets
from .models import Club
from .serializers import ClubSerializer
from djoser.views import UserViewSet
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.pagination import LimitOffsetPagination

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class CustomUserViewSet(UserViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileCreateAPIView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileListAPIView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination


class UserProfileUpdateAPIView(UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UserProfileDestroyAPIView(DestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# Forgot the password

# views.py
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')



