from django.db import models

# Create your models here.
STATUS = (
    ("Booked", "Booked"),
    ("Cancel_Book", "Cancel_Book")
)


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=100)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    seat = models.OneToOneField("cinema_booking.BookSeat", on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=STATUS, default="Booked")

    def __str__(self):
        return "{}-{}-{}".format(self.user, self.type, self.seat)

    def notification_read(self, user):
        for i in Notification.objects.filter(user=user):
            i.read = True
            i.save()
