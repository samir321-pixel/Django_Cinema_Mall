# Generated by Django 3.1.7 on 2021-02-28 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210228_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='past_booking',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]