from django.urls import path
from .views import book_list, book_detail, book_edit
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list, name='book_list'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('book/<int:pk>/edit/', book_edit, name='book_edit'),
]