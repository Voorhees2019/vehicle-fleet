from django.db import models
from django.utils.translation import ugettext_lazy as _


class Driver(models.Model):
    first_name = models.CharField(_("First Name"), max_length=127)
    last_name = models.CharField(_("Last Name"), max_length=127)
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date updated"), auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Vehicle(models.Model):
    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        related_name="driver_vehicles",
        blank=True,
        null=True,
    )
    make = models.CharField(_("Make"), max_length=127)
    model = models.CharField(_("Model"), max_length=127)
    plate_number = models.CharField(_("Plate number"), max_length=127)
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date updated"), auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.make} {self.model}"
