from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField
from django.contrib.auth.models import User
from main import settings
import datetime
from rest_framework import permissions

now = datetime.datetime.now()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='orders')
    number_of_cups = models.IntegerField()
    location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
    objects = models.GeoManager()
    order_status = models.BooleanField(default=1)
    order_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username






