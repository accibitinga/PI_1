from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.login_page, name='login'),
]
