from django.urls import path
from .views import AnimalsAPIList

urlpatterns = [
    path('', AnimalsAPIList.as_view())
]
