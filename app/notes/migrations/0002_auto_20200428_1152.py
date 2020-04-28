# Generated by Django 3.0.5 on 2020-04-28 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='description',
            field=models.TextField(default='test', verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='date_time',
            field=models.DateTimeField(verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='note',
            name='mood_rating',
            field=models.IntegerField(verbose_name='mood rating'),
        ),
        migrations.AlterField(
            model_name='note',
            name='weather_rating',
            field=models.IntegerField(verbose_name='weather rating'),
        ),
    ]