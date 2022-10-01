from django.urls import path
from . import views

app_name = "todos"

urlpatterns  = [
    path("",views.index, name="index"),
    path("create/", views.create, name="create"),
    path("new/",views.new, name="new"),
    path("detail/<int:pk>",views.detail, name="detail"),
    path("update/<int:pk>", views.update, name='update'),
    path("delete/<int:pk>", views.delete, name="delete"),
    path('search/', views.search, name='search'),

]

