from django.urls import path

from . import views

app_name = "vehicle_fleet"

urlpatterns = [
    path("drivers/driver/", views.DriverListCreate.as_view(), name="driver_list"),
    path(
        "drivers/driver/<int:pk>/",
        views.DriverRetrieveUpdateDestroy.as_view(),
        name="driver",
    ),
    path("vehicles/vehicle/", views.VehicleListCreate.as_view(), name="vehicle_list"),
    path(
        "vehicles/vehicle/<int:pk>/",
        views.VehicleRetrieveUpdateDestroy.as_view(),
        name="vehicle",
    ),
    path(
        "vehicles/set_driver/<int:vehicle_pk>/",
        views.VehicleSetDriver.as_view(),
        name="vehicle_set_driver",
    ),
]
