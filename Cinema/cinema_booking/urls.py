from rest_framework import routers
from django.urls import path, include

from .views import *

router = routers.DefaultRouter()
router.register('cinema', AvailableSlotsViewsets, 'cinema')
router.register('seat', SeatsViewsets, 'seat')
router.register('book_seat', BookSeatsViewsets, 'book_seat')
router.register('seat_manager', SeatManagerViewsets, 'seat_manager')

urlpatterns = [
    path(r'', include(router.urls)),
]
