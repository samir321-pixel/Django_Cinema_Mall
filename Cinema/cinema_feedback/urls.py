from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ReviewViewsets.as_view()),
]
