from unicodedata import name
import django
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='home'),
    path('user_li/', views.user_li, name='user_li'),
    path('<int:pk>/', views.detail, name='detail'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]