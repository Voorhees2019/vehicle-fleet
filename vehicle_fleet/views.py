from django_filters import rest_framework as filters
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .filters import DriverFilter, VehicleFilter
from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer
from .services import vehicle_set_driver


class DriverListCreate(generics.ListCreateAPIView):
    serializer_class = DriverSerializer
    pagination_class = PageNumberPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DriverFilter

    def get_queryset(self):
        return Driver.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = DriverSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DriverRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer

    def get_queryset(self):
        return Driver.objects.all()


class VehicleListCreate(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer
    pagination_class = PageNumberPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VehicleFilter

    def get_queryset(self):
        return Vehicle.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = VehicleSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VehicleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        return Vehicle.objects.all()


class VehicleSetDriver(generics.CreateAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        return Vehicle.objects.all()

    def post(self, request, *args, **kwargs):
        driver_pk = request.data.get("driver_id")
        set_driver_status, msg = vehicle_set_driver(
            vehicle_pk=self.kwargs.get("vehicle_pk"), driver_pk=driver_pk
        )
        return Response({"detail": msg}, status=set_driver_status)
