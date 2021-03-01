from rest_framework import routers
from django.urls import path, include

from .views import *

router = routers.DefaultRouter()
router.register('book_seat', BookSeatsViewsets, 'book_seat')
router.register('seat_manager', SeatManagerViewsets, 'seat_manager')

urlpatterns = [
    path(r'', include(router.urls)),
    path('available_seat/', SeatsList.as_view()),
    path('available_slot/', AvailableSlotsViewsets.as_view()),
]
