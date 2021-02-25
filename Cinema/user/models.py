from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
