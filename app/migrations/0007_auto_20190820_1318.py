# Generated by Django 2.2.3 on 2019-08-20 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190820_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionmodel',
            name='time',
            field=models.TimeField(default=datetime.time(13, 18, 42, 298014)),
        ),
    ]
