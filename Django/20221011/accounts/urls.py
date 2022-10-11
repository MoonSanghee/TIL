from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('<int:pk>/', views.detail, name='detail'),
    path('userlist/', views.userlist, name='userlist'),
]
