# Generated by Django 3.1.7 on 2021-02-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_booking', '0003_auto_20210228_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='available_slots',
            name='updated_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='bookseat',
            name='updated_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='seat_manager',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
