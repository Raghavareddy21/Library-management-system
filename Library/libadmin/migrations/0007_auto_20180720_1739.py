# Generated by Django 2.0.7 on 2018-07-20 17:39

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libadmin', '0006_auto_20180719_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklist',
            name='Category',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booklist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 20, 17, 38, 45, 985052, tzinfo=utc)),
        ),
    ]
