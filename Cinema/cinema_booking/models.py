from django.db import models

# Create your models here.
from manage_cinema.models import *


class Available_Slots(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False)
    slot = models.ForeignKey("manage_cinema.CinemaArrangeSlot", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.date)


class seat_manager(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.IntegerField()
    deck = models.ForeignKey("manage_cinema.Cinema_Deck", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    seat = models.ForeignKey("cinema_booking.seat_manager", on_delete=models.CASCADE)
    available_slot = models.ForeignKey("cinema_booking.Available_Slots", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    book = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}-{}".format(self.seat, self.name, self.date)

    def seat_maker(self):
        available_slot_query = Available_Slots.objects.all()
        cinema_deck_query = Cinema_Deck.objects.all()
        seat_query = Seat.objects.all()

        for i in cinema_arrange_slot_query:
            pass
