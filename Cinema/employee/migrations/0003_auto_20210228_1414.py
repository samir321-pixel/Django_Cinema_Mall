# Generated by Django 3.1.7 on 2021-02-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210228_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(default='2021-02-28T05:36:42.170087Z'),
            preserve_default=False,
        ),
    ]