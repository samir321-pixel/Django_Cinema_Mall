from django.db import models
from djmoney.models.fields import MoneyField
from phone_field import PhoneField

# Create your models here.

gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)


class Employee(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.PROTECT)
    first_Name = models.CharField(max_length=200, default="")
    middle_Name = models.CharField(max_length=200, default="", null=True, blank=True)
    last_Name = models.CharField(max_length=200, default="", null=True, blank=True)
    DOB = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    active = models.BooleanField(default=True)
    phone = PhoneField()
    Address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.CharField(("pin code"), max_length=7, default="00000")
    joining_date = models.DateField()
    salary = MoneyField(default=0, default_currency='INR', max_digits=11)
    salary_due_date = models.DateField(auto_now=False)
    releasing_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.user, self.first_Name)
