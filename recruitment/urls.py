from django.urls import path
from django import views
from . import views



urlpatterns = [
     path('get', views.UserProfileView.as_view()),

]