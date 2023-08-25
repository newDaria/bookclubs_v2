from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Club
from .serializers import ClubSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    # You can add authentication and permission settings here if needed
