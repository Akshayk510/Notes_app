from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('register/', views.register, name='register'),
    path('note/new/', views.note_create, name='note_create'),
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
]