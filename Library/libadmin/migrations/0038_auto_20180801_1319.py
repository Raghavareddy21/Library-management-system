# Generated by Django 2.0.7 on 2018-08-01 13:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libadmin', '0037_auto_20180801_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 1, 13, 19, 8, 224201, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 1, 13, 19, 8, 223667, tzinfo=utc)),
        ),
    ]
