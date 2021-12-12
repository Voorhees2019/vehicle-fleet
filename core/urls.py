from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/vehicle_fleet/", include("vehicle_fleet.urls")),
]
