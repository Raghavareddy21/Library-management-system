# Generated by Django 2.0.7 on 2018-07-21 07:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libadmin', '0010_auto_20180721_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 21, 7, 59, 4, 559190, tzinfo=utc)),
        ),
    ]
