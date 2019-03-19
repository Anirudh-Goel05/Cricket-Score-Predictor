from django.contrib import admin
from django.urls import path
from .views import HomePageView

app_name = 'myapp'

urlpatterns = [
    path('',HomePageView,name='homepage'),
]
