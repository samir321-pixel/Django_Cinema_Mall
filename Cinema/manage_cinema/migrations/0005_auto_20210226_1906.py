# Generated by Django 3.1.7 on 2021-02-26 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_cinema', '0004_delete_cinemaslot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemaarrangeslot',
            old_name='duration',
            new_name='duration_slot',
        ),
    ]
