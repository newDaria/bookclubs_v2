from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import UserProfile, Club


admin.site.register(UserProfile)
admin.site.register(Club)
