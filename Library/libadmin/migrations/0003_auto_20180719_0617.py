# Generated by Django 2.0.7 on 2018-07-19 06:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libadmin', '0002_auto_20180719_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 19, 6, 17, 29, 745272, tzinfo=utc)),
        ),
    ]
