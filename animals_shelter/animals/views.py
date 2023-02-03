from rest_framework import generics, status
from rest_framework.response import Response

from .permissions import IsAdminOrReadOnly
from .serializers import AnimalSerializer
from .models import Animal


class AnimalsAPIList(generics.ListCreateAPIView):
    """
    API List View.
    Returns all the values in Animals table from DataBase.
    Returned format is Json.
    Admin Allowed to create new Animal on page.
    """
    serializer_class = AnimalSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Animal.objects.filter(is_deleted=False).all()


class AnimalsDetailAPI(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    API Detail View.
    Returns all the data of requested animal by his Primary Key.
    Returned format is Json.
    Admin Allowed to SOFT delete animal or update his information.
    """
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_200_OK)
