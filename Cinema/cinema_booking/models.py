import datetime
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.db import models
from djmoney.models.fields import MoneyField


class Available_Slots(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False)
    slot = models.ForeignKey("managecinema.CinemaArrangeSlot", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.date)


class seat_manager(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.IntegerField()
    deck = models.ForeignKey("managecinema.CinemaDeck", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    seat = models.ForeignKey("cinema_booking.seat_manager", on_delete=models.CASCADE)
    available_slot = models.ForeignKey("cinema_booking.Available_Slots", on_delete=models.CASCADE)
    book_by = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    book = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.seat, self.name, self.date, self.deck)

    def seat_book(self, seat, user):
        query = Seat.objects.get(id=seat)
        query.book = True
        query.book_by = user
        query.updated_at = datetime.datetime.now()
        query.save()

    def seat_updater(self):
        for i in Seat.objects.all():
            try:
                if datetime.datetime.now() > datetime.datetime.combine(i.date, datetime.time(0, 0)):
                    i.active = False
                    i.save()
            except Exception as e:
                pass


class BookSeat(models.Model):
    id = models.AutoField(primary_key=True)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE, unique=True)
    booking_price = MoneyField(default=0, default_currency='INR', max_digits=11, null=True, blank=True)
    name_on_card = models.CharField(max_length=150)
    cc_number = CardNumberField('card number')
    cc_expiry = CardExpiryField('expiration date')
    cc_code = SecurityCodeField('security code')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.seat, self.user)
