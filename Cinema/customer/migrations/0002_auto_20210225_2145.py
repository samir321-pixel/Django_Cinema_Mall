# Generated by Django 3.1.7 on 2021-02-25 16:15

from django.db import migrations, models
import localflavor.in_.models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='pincode',
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=localflavor.in_.models.INStateField(blank=True, max_length=2, null=True),
        ),
    ]
