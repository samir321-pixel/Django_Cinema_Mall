import datetime
from django.db import models
from djmoney.models.fields import MoneyField
from cinema_booking.models import Available_Slots, seat_manager, Seat


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


class CinemaDeck(models.Model):
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
    cinema = models.ForeignKey("managecinema.Cinema", on_delete=models.CASCADE)
    start_time = models.TimeField(unique=True)
    duration_slot = models.ForeignKey("managecinema.MovieDurationSlot", on_delete=models.CASCADE)
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
                Available_Slots.objects.create(slot=i, date=datetime.datetime.today(), active=True)
            for j in range(0, 2):
                dates += datetime.timedelta(days=1)
                if not Available_Slots.objects.filter(slot=i, date=dates):
                    Available_Slots.objects.create(slot=i, date=dates, active=True)
                elif Available_Slots.objects.filter(slot=i, date=dates):
                    pass

    def seat_maker(self):
        for i in CinemaDeck.objects.filter(active=True):
            for j in seat_manager.objects.all():
                for k in Available_Slots.objects.filter(active=True):
                    for l in range(0, 2):
                        if not Seat.objects.filter(name=l, deck=i, date=k.date, seat=j, available_slot=k):
                            Seat.objects.create(name=l, deck=i, date=k.date, seat=j,
                                                available_slot=k)
                        if Seat.objects.filter(name=l, deck=i, date=k.date, seat=j, available_slot=k):
                            pass

    def slot_updater(self):
        for i in Available_Slots.objects.all():
            try:
                if datetime.datetime.now() > datetime.datetime.combine(i.date, datetime.time(0, 0)):
                    i.active = False
                    i.save()
            except Exception as e:
                pass
