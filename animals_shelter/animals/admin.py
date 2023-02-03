from django.contrib import admin
from .models import (
    Animal,
)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'arrival_date', 'is_deleted']
    list_filter = ['arrival_date', 'is_deleted']
    search_fields = ['name', 'additional_information']
