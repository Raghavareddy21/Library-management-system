# Generated by Django 2.0.7 on 2018-08-20 14:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libuser', '0019_auto_20180816_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placerequest',
            name='id',
        ),
        migrations.AlterField(
            model_name='placerequest',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='libadmin.books'),
        ),
        migrations.AlterField(
            model_name='placerequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 20, 14, 15, 49, 56709, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='placerequest',
            name='submition_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 19, 14, 15, 49, 56812)),
        ),
    ]
