"""
URL configuration for bookclubs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from bookclubs_app.views import ClubViewSet, CustomUserViewSet, home_view
from bookclubs_app.views import UserProfileCreateAPIView, UserProfileListAPIView, UserProfileUpdateAPIView, \
    UserProfileDestroyAPIView
from django.contrib.auth import views as auth_views

# Create a router for the ClubViewSet
router = DefaultRouter()
router.register(r'clubs', ClubViewSet)
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # Club Model URLs using ModelViewSet
    path('', include(router.urls)),

    path("__debug__/", include("debug_toolbar.urls")),

    path('api/userprofiles/create/', UserProfileCreateAPIView.as_view(), name='userprofile-create'),
    path('api/userprofiles/list/', UserProfileListAPIView.as_view(), name='userprofile-list'),
    path('api/userprofiles/update/<int:pk>/', UserProfileUpdateAPIView.as_view(), name='userprofile-update'),
    path('api/userprofiles/destroy/<int:pk>/', UserProfileDestroyAPIView.as_view(), name='userprofile-destroy'),

    # forgot the password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name='password_reset_complete'),

    path('home/', home_view, name='home'),

]
