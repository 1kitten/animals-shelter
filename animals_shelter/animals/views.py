from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Animal
from .permissions import IsAdminOrAuthenticatedOrReadOnly
from .serializers import AnimalSerializer


class AnimalsAPIList(generics.ListCreateAPIView):
    """
    API List View.
    Returns all the values in Animals table from DataBase.
    Returned format is Json.
    Admin Allowed to create new Animal on page.
    Authenticated user can see only his animals.
    Non authenticated user can see all animals.
    """
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated and not self.request.user.is_staff:
            return Animal.objects.filter(is_deleted=False).filter(user=self.request.user.pk)
        return Animal.objects.filter(is_deleted=False)


class AnimalsDetailAPI(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    API Detail View.
    Returns all the data of requested animal by his Primary Key.
    Returned format is Json.
    Admin Allowed to SOFT delete animal or update his information.
    """
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    permission_classes = [IsAdminOrAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_200_OK)
