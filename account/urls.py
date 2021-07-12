from django.urls import path
from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import (change_password,  go_in)
urlpatterns = [
    path('login', go_in, name='login'),
    path('change_password', change_password, name='change_password'),
]
