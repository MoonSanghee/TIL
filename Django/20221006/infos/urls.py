from django.urls import path
from . import views


app_name ='infos'

urlpatterns = [
    path('movies/', views.index, name="index"),
    path('movies/create/', views.create, name='create'),
    path('movies/<int:pk>/', views.detail, name='detail'),
    path('movies/<int:pk>/delete/', views.delete, name='delete'),
    path('movies/<int:pk>/update/', views.update, name='update'),
]