from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
