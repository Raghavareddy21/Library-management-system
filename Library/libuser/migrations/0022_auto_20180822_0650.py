# Generated by Django 2.0.7 on 2018-08-22 06:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libuser', '0021_auto_20180822_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placerequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 22, 6, 50, 19, 929342, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='placerequest',
            name='submition_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 21, 6, 50, 19, 929372)),
        ),
    ]
