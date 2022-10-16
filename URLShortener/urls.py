from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('example/<slug:name>', example_view),
    path('shorten/', shorten_url)
]
