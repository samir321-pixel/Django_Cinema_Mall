# Generated by Django 3.1.7 on 2021-02-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_booking', '0011_auto_20210227_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='name',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]