from django.contrib import admin
from superapp.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','bio','profile_picture']

    