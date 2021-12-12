import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Driver, Vehicle


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ("id", "first_name", "last_name", "created_at", "updated_at")

    def create(self, validated_data):
        driver = Driver.objects.filter(
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
        ).first()
        # Create a new driver if not exist yet
        if not driver:
            driver = super().create(validated_data=validated_data)
        return driver


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            "id",
            "driver",
            "make",
            "model",
            "plate_number",
            "created_at",
            "updated_at",
        )

    def validate_plate_number(self, value):
        r = re.compile(r"^[A-Z]{2} [0-9]{4} [A-Z]{2}$")
        if r.match(value.upper()):
            # valid plane_nUmber
            return value.upper()
        else:
            raise ValidationError("Invalid plate_number. Template: 'AA 1234 OO'")

    def create(self, validated_data):
        vehicle = Vehicle.objects.filter(**validated_data).first()
        # Create a new vehicle if not exist yet
        if not vehicle:
            vehicle = super().create(validated_data=validated_data)
        return vehicle
