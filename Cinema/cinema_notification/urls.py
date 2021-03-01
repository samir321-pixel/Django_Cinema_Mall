from rest_framework import routers
from django.urls import path, include
from .views import *


urlpatterns = [
    path('notification/', NotificationListView.as_view()),
]