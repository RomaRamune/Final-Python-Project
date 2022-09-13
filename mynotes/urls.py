from django.urls import path
from .views import index, categories, category, notes, search, register, addCategory, updateCategory, deleteCategory, addNote, updateNote, deleteNote

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('categories/<int:category_id>', category, name='category'),
    path('notes/', notes, name='notes'),
    path('search/', search, name='search'),
    path('register/', register, name='register'),
    path('create_category/', addCategory, name='create_category'),
    path('update_category/<str:pk>', updateCategory, name='update_category'),
    path('delete_category/<str:pk>', deleteCategory, name='delete_category'),
    path('create_note/', addNote, name='create_note'),
    path('update_note/<str:pk>', updateNote, name='update_note'),
    path('delete_note/<str:pk>', deleteNote, name='delete_note'),
]