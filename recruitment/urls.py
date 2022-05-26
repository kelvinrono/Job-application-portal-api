from django.urls import path
from . import views
from django import views


urlpatterns = [
     path('', views.UserProfileView.as_view()),

]