from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'date_time', 'weather_rating', 'mood_rating', 'description'] 