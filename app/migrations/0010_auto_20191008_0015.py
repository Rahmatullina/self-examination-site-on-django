# Generated by Django 2.2.3 on 2019-10-07 21:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190918_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionmodel',
            name='day',
            field=models.CharField(default='08', max_length=2),
        ),
        migrations.AlterField(
            model_name='regionmodel',
            name='month',
            field=models.CharField(default='10', max_length=2),
        ),
        migrations.AlterField(
            model_name='regionmodel',
            name='time',
            field=models.TimeField(default=datetime.time(0, 15, 30, 924031)),
        ),
    ]
