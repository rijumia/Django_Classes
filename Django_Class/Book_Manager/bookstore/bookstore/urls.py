from django.contrib import admin
from django.urls import path
from books.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('bookList', bookList, name='bookList'),
    path('book_add', bookForm, name='bookAdd'),
    path('book_update/<str:id>/', bookUpdate, name='bookUpdate'),
    path('bookList/<str:id>/', bookDelete, name='bookDelete'),
]
