from asgiref.sync import async_to_sync
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@receiver(post_save, sender=Product)
def send_product_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'products_group',
            {
                'type': 'send_product_notification',
                'product': instance.name
            }
        )


class PurchasesViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer