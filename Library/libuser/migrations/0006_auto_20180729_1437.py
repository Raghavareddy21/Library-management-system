# Generated by Django 2.0.7 on 2018-07-29 14:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libuser', '0005_auto_20180729_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placerequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 29, 14, 37, 32, 503800, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='placerequest',
            name='submition_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 28, 14, 37, 32, 503828)),
        ),
    ]
