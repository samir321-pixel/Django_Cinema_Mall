from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    movie = models.ForeignKey("managecinema.Cinema", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return "{}-{}".format(self.user, self.movie)
