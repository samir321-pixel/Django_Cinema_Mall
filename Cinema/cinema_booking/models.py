from django.db import models


# Create your models here.

class Available_Slots(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False)
    slot = models.ForeignKey("manage_cinema.CinemaArrangeSlot", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.date)


class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    deck = models.ForeignKey("manage_cinema.Cinema_Deck", on_delete=models.CASCADE)
    date=models.DateField(auto_now=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    book = models.BooleanField(default=False)

    def __str__(self):
        return self.deck
