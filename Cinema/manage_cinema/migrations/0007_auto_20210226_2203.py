# Generated by Django 3.1.7 on 2021-02-26 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_cinema', '0006_auto_20210226_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemaarrangeslot',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_cinema.cinema'),
        ),
    ]
