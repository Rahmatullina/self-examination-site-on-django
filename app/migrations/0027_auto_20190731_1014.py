# Generated by Django 2.2.3 on 2019-07-31 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20190726_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regionmodel',
            name='has_troubles',
        ),
        migrations.AlterField(
            model_name='regionmodel',
            name='time',
            field=models.TimeField(default=datetime.time(10, 14, 23, 787166)),
        ),
    ]
