from rest_framework import generics
from .permissions import IsAdminOrReadOnly
from .serializers import AnimalSerializer
from .models import Animal


class AnimalsAPIList(generics.ListCreateAPIView):
    """
    API List View.
    Returns all the values in Animals table from DataBase.
    Returned format is Json.
    User Allowed to create new Animal on page.
    """
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    permission_classes = [IsAdminOrReadOnly]
