from rest_framework import generics
from orders.models import Order
from orders.serializers import OrderSerializer
import datetime

now = datetime.datetime.now()


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def update_or_cancel(self,):
    #     time_diff = now - self.order_time
    #     total_seconds = time_diff.total_seconds()
    #     if total_seconds <= 900:
    #         self.order_type = 0

