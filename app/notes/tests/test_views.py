import json
from rest_framework import status
from rest_framework.test import APITestCase

from django.test import TestCase, Client
from django.urls import reverse

from ..models import Note
from ..serializers import NoteSerializer

class NoteListTestCase(APITestCase):
    url = reverse('list')

    def test_create_note(self):
        """
        Ensure we can create a new note object
        """
        data = {
            "date_time": "2020-01-23T20:49:00Z",
            "weather_rating": 4,
            "mood_rating": 5,
            "description": "Some text"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)

class NoteDetailViewTestCase(APITestCase):

    def setUp(self):
        self.note = Note.objects.create(
            date_time = "2020-01-23T20:49:00Z",
            weather_rating = 2,
            mood_rating = 2,
            description = "Some text description"
        )
        self.url = reverse('detail', kwargs={"pk": self.note.pk})

    def test_note_object_update(self):
        note_json = {
            "id": 1,
            "date_time": "2019-01-23T20:49:00Z",
            "weather_rating": 1,
            "mood_rating": 1,
            "description": "New title"
        }
        response = self.client.put(self.url, note_json)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_note_object_partial_update(self):
        response = self.client.patch(self.url, {"description": "New description"})
        response_data = json.loads(response.content)

        note = Note.objects.get(id=self.note.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.get("description"), note.description)
    
    def test_note_delete(self):
        self.assertEqual(Note.objects.count(), 1)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 0)