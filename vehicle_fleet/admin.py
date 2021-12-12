from django.contrib import admin

from .models import Driver, Vehicle


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "created_at", "updated_at")
    list_display_links = ("id", "first_name", "last_name")
    list_filter = ("created_at", "updated_at")
    search_fields = ("first_name", "last_name")
    list_per_page = 25


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "make",
        "model",
        "driver",
        "plate_number",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "make")
    list_filter = ("make", "model", "driver", "created_at", "updated_at")
    search_fields = (
        "make",
        "model",
        "driver__first_name",
        "driver__last_name",
        "plate_number",
    )
    list_per_page = 25
