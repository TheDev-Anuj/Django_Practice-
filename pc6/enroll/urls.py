from django.urls import path
from . import views
urlpatterns = [
    path('', views.ShowUserData, name='register'),
]