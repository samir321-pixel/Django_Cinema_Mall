from rest_framework import routers
from django.urls import path, include
from .views import *

urlpatterns = [
    path('notification/', NotificationListView.as_view()),
    path('unread_notification_count/', UnreadNotificationCount.as_view(), name='unread_notification_count'),
]
