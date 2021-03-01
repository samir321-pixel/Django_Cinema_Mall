# Generated by Django 3.1.7 on 2021-03-01 07:27

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_booking', '0010_auto_20210301_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookseat',
            name='booking_price',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0'), default_currency='INR', max_digits=11, null=True),
        ),
    ]