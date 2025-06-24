
from django.contrib import admin
from django.urls import path
from customUsersApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loginPage, name='loginPage'),
    path('signup/', signupPage, name='signupPage'),
    path('homePage/', homePage, name='homePage')
]
