
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_page, name="book_list_page"),
    path('book-create/', views.book_create_page, name="book_create_page"),
    path('book-delete/<int:pk>/', views.book_delete_page, name="book_delete_page"),
]
