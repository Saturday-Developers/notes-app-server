# Generated by Django 3.0.5 on 2020-04-28 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200428_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
