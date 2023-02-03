from rest_framework import generics
from .serializers import AnimalSerializer
from .models import Animal


class AnimalsAPIList(generics.ListAPIView):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
