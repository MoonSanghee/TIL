from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('<int:pk>/', views.detail, name='detail'),
    path('userlist/', views.userlist, name='userlist'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
]
