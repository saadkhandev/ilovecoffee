from django.db import models
from django.contrib.auth.models import User
from main import settings
import datetime

now =  datetime.datetime.now()

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='orders')
    number_of_cups = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    order_type = models.BooleanField(default=1)
    order_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def update_or_cancel(self):
        if now - self.order_time <= 15:
            self.order_type = 0
