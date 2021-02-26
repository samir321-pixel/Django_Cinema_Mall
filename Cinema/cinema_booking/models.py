from django.db import models


# Create your models here.

class Available_Slots(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False)
    slot = models.ForeignKey("manage_cinema.CinemaArrangeSlot", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.date)
