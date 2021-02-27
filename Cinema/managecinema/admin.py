from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cinema)
admin.site.register(CinemaDeck)
admin.site.register(CinemaArrangeSlot)
admin.site.register(MovieDurationSlot)
