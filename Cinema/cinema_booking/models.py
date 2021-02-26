from django.db import models


# Create your models here.

class Available_Slots(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False)

    def __str__(self):
        return "{}".format(self.date)
