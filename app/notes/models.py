from django.db import models
# Create your models here.

class Note(models.Model):
    date_time = models.DateTimeField(verbose_name='creation date')
    weather_rating = models.IntegerField(verbose_name='weather rating')
    mood_rating = models.IntegerField(verbose_name='mood rating')
    description = models.TextField(verbose_name='description')