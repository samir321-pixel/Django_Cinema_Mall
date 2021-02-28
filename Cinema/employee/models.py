from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.

gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)


class Employee(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.PROTECT, null=True, blank=True)
    first_Name = models.CharField(max_length=200, default="")
    middle_Name = models.CharField(max_length=200, default="", null=True, blank=True)
    last_Name = models.CharField(max_length=200, default="", null=True, blank=True)
    DOB = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    active = models.BooleanField(default=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.PositiveIntegerField(default=0)
    joining_date = models.DateField()
    salary = MoneyField(default=0, default_currency='INR', max_digits=11)
    salary_due_date = models.DateField()
    releasing_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + " " + self.first_Name + " " + self.last_Name
