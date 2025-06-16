# backend/api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/<int:pk>/", views.NoteDetail.as_view(), name="note-detail"),
    path("user/me/", views.MeView.as_view(), name="me"),
]
