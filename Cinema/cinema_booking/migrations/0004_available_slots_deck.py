# Generated by Django 3.1.7 on 2021-02-27 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_cinema', '0010_auto_20210227_1022'),
        ('cinema_booking', '0003_auto_20210227_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='available_slots',
            name='deck',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manage_cinema.cinema_deck'),
            preserve_default=False,
        ),
    ]
