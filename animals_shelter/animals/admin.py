from django.contrib import admin
from .models import (
    Animal,
)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'arrival_date', 'is_deleted']
    list_filter = ['arrival_date', 'is_deleted']
    search_fields = ['name', 'additional_information']
    actions = ['mark_as_deleted', 'unmark_as_deleted']

    @admin.action(description='Mark Animal as Deleted (Soft Delete)')
    def mark_as_deleted(self, request, queryset):
        queryset.update(is_deleted=True)

    @admin.action(description='Unmark Animal as Deleted')
    def unmark_as_deleted(self, request, queryset):
        queryset.update(is_deleted=False)
