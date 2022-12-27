from django.contrib import admin
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio),
    path("curso/", curso),
]