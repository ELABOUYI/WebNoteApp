from django.urls import path
from .views import NoteViewSet

urlpatterns = [
    path("", NoteViewSet.as_view({'get': 'list'})),
]