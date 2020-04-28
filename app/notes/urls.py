from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from notes import views

router = routers.DefaultRouter()
router.register(r'notes', views.NoteViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('notes/', views.NoteList.as_view()),
    path('notes/<int:pk>/', views.NoteDetailView.as_view())
]
