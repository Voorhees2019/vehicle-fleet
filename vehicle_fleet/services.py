from typing import Union

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError

from .models import Driver, Vehicle


def vehicle_set_driver(vehicle_pk: int, driver_pk: Union[int, str]) -> tuple[int, str]:
    try:
        driver_pk = int(driver_pk)
    except ValueError:
        raise ValidationError(f'Invalid driver_id "{driver_pk}" - id must be numeric.')

    try:
        Driver.objects.get(pk=driver_pk)
    except Driver.DoesNotExist:
        raise ValidationError(
            f'Invalid driver_id "{driver_pk}" - object does not exist.'
        )

    vehicle = get_object_or_404(Vehicle, pk=vehicle_pk)

    # set driver to vehicle if no driver has been set before
    if not vehicle.driver:
        vehicle.driver_id = driver_pk
        vehicle.save()
        return status.HTTP_200_OK, "driver has been set."
    # reset driver
    if vehicle.driver_id == driver_pk:
        vehicle.driver = None
        vehicle.save()
        return status.HTTP_200_OK, "driver has been reset."
    return (
        status.HTTP_403_FORBIDDEN,
        "another driver has already been set to this vehicle.",
    )
