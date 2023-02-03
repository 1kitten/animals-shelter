from django.contrib import admin
from .models import (
    Animal,
)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'arrival_date']
    list_filter = ['arrival_date']
    search_fields = ['name', 'additional_information']
