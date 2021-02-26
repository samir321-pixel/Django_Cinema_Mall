from django.db import models


# Create your models here.
class cinema(models.Model):
    id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=200)
    release_date = models.DateTimeField(auto_now=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
