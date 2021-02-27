from django.db import models


class Available_Slots(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False)
    slot = models.ForeignKey("managecinema.CinemaArrangeSlot", on_delete=models.CASCADE)
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
    deck = models.ForeignKey("managecinema.CinemaDeck", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    seat = models.ForeignKey("cinema_booking.seat_manager", on_delete=models.CASCADE)
    available_slot = models.ForeignKey("cinema_booking.Available_Slots", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    book = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}-{}".format(self.seat, self.name, self.date)
