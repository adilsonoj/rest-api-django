from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.userById, name='userById'),
    path('', views.users, name='users')
]