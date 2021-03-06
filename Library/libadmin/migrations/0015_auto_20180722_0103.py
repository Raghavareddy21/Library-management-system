# Generated by Django 2.0.7 on 2018-07-22 01:03

import datetime
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libadmin', '0014_auto_20180721_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='pictures/')),
                ('book', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='files/'), upload_to='')),
                ('date', models.DateField()),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2018, 7, 22, 1, 3, 9, 816807, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=250)),
                ('img', models.FileField(upload_to='pictures/')),
                ('date', models.DateField()),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2018, 7, 22, 1, 3, 9, 816217, tzinfo=utc))),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='booklist',
        ),
        migrations.AddField(
            model_name='books',
            name='book_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libadmin.category'),
        ),
    ]
