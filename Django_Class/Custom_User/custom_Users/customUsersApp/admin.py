from django.contrib import admin
from customUsersApp.models import customUser
from django.contrib.auth.admin import UserAdmin

class userModel(UserAdmin):
    list_display=['username','email','user_type']

admin.site.register(customUser,userModel)
