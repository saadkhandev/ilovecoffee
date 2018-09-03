from rest_framework import serializers
from . import models


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Order