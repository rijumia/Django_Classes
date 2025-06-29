from django.contrib import admin
from django.urls import path
from task_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('register/', signupPage, name='signupPage'),
]
