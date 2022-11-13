from django.urls import path, include
from appcoder.views import *

urlpatterns = [
    path('', inicio),
    path('familiares/', familiares),
]

