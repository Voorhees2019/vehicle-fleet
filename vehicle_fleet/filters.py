from django_filters import rest_framework as filters

from .models import Driver, Vehicle


class DriverFilter(filters.FilterSet):
    created_at__gte = filters.DateFilter(field_name="created_at", lookup_expr="gte")
    created_at__lte = filters.DateFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = Driver
        fields = ["created_at__gte", "created_at__lte"]


class VehicleFilter(filters.FilterSet):
    CHOICES = (("yes", "Yes"), ("no", "No"))
    with_drivers = filters.ChoiceFilter(
        choices=CHOICES, method="filter_by_driver_presence"
    )

    class Meta:
        model = Vehicle
        fields = ["with_drivers"]

    def filter_by_driver_presence(self, queryset, name, value):
        without_driver = True if value == "no" else False
        return queryset.filter(driver__isnull=without_driver)
