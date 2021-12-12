# Vehicle Fleet REST API
## Overview
Here is the [Django](https://www.djangoproject.com/) implementation of backend part for Vehicle Fleet Project. In particular this is the [test assignment](https://docs.google.com/document/d/1sAqFWAIO1gIZbajQzFgW1f72qmfI8bdE-FE-JDCc5zU/edit) for Yalantis Python School 2.<br>
All endpoints are opened (no need for authentication).<br>
Admin panel is also provided after setup and running project server (http://127.0.0.1:8000/admin/) <br>
Date format: %d/%m/%Y.<br>
Datatime format: %d/%m/%Y %H:%M:%S.

## API endpoints
Driver:
+ GET /drivers/driver/ - get the list of drivers
+ GET /drivers/driver/?created_at__gte=05-12-2021 - get the list of drivers who were created after 05-12-2021
+ GET /drivers/driver/?created_at__lte=05-12-2021 - get the list of drivers who were created before 05-12-2021

+ GET /drivers/driver/<driver_id>/ - get the driver information by his id
+ POST /drivers/driver/ - create a new driver
+ PUT /drivers/driver/<driver_id>/ - entire update of the driver's information
+ PATCH /drivers/driver/<driver_id>/ - partial update of the driver's information
+ DELETE /drivers/driver/<driver_id>/ - delete the driver

Vehicle:
+ GET /vehicles/vehicle/ - get the list of vehicles
+ GET /vehicles/vehicle/?with_drivers=yes - get the list of vehicles with the driver set
+ GET /vehicles/vehicle/?with_drivers=no - get the list of vehicles with no driver

+ GET /vehicles/vehicle/<vehicle_id> - get the vehicle information by its id
+ POST /vehicles/vehicle/ - create a new vehicle
+ PUT /vehicles/vehicle/<vehicle_id>/ - entire update of the vehicle's information
+ PATCH /vehicles/vehicle/<vehicle_id>/ - partial update of the vehicle's information
+ POST /vehicles/set_driver/<vehicle_id>/ - set vehicle's driver / reset vehicle's driver (by providing body parameter: `driver_id`)
+ DELETE /vehicles/vehicle/<vehicle_id>/ - delete the vehicle
