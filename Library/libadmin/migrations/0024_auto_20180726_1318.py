# Generated by Django 2.0.7 on 2018-07-26 13:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libadmin', '0023_auto_20180726_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 26, 13, 18, 18, 350965, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 26, 13, 18, 18, 350478, tzinfo=utc)),
        ),
    ]
