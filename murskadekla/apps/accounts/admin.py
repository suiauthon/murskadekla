from django.contrib import admin

from .models import UserProfile, UserInterest

admin.site.register(UserProfile)
admin.site.register(UserInterest)
