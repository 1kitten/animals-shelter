from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Animal
from .permissions import IsAdminOrAuthenticatedOrReadOnly, IsAdminOrReadOnly
from .serializers import AnimalSerializer


class AnimalAPIListPagination(PageNumberPagination):
    """
    Pagination Class For Animal List API View.
    Returns only <= 4 rows from DataBase.
    """
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100


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
    pagination_class = AnimalAPIListPagination

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
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            instance = self.get_object()
            instance.is_deleted = True
            instance.save()
            return Response(status=status.HTTP_200_OK)
        return Response({"You are not an administrator."}, 400)

    def put(self, request, *args, **kwargs):
        if request.user.is_staff:
            return self.update(request, *args, **kwargs)
        if request.user.pk == self.get_object().user.pk:
            return self.update(request, *args, **kwargs)
        return Response({"You are not a shelter for this animal."}, 400)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        shelter = instance.user
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = shelter
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
