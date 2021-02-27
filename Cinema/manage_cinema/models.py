import datetime

from django.db import models
from djmoney.models.fields import MoneyField


# Create your models here.
from cinema_booking.models import Available_Slots


class Cinema(models.Model):
    id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=200, unique=True)
    release_date = models.DateField(auto_now=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}{}".format(self.movie_name, self.release_date)


class Cinema_Deck(models.Model):
    id = models.AutoField(primary_key=True)
    deck_name = models.CharField(max_length=200, unique=True)
    price = MoneyField(default=0, default_currency='INR', max_digits=11)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}{}".format(self.deck_name, self.price)


class MovieDurationSlot(models.Model):
    id = models.AutoField(primary_key=True)
    duration = models.DurationField(unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}-{}".format(self.duration, self.active)


class CinemaArrangeSlot(models.Model):
    id = models.AutoField(primary_key=True)
    cinema = models.ForeignKey("manage_cinema.Cinema", on_delete=models.CASCADE)
    start_time = models.TimeField(unique=True)
    duration_slot = models.ForeignKey("manage_cinema.MovieDurationSlot", on_delete=models.CASCADE)
    end_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}-{}".format(self.cinema, self.start_time)

    def slot_maker(self):
        query = CinemaArrangeSlot.objects.all()
        dates = datetime.date.today()
        for i in query:
            if not Available_Slots.objects.filter(slot=i, date=datetime.date.today()):
                Available_Slots.objects.create(slot=i, date=datetime.datetime.today())
            for j in range(0, 3):
                dates += datetime.timedelta(days=1)
                if not Available_Slots.objects.filter(slot=i, date=dates):
                    Available_Slots.objects.create(slot=i, date=dates)
                elif Available_Slots.objects.filter(slot=i, date=dates):
                    pass

