# Generated by Django 3.1.7 on 2021-02-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_booking', '0008_seat_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='date',
            field=models.DateField(),
        ),
    ]