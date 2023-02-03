from django.urls import path
from .views import (
    AnimalsAPIList,
    AnimalsDetailAPI
)

urlpatterns = [
    path('', AnimalsAPIList.as_view()),
    path('<int:pk>', AnimalsDetailAPI.as_view()),
]
