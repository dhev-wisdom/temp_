from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# def get_default_owner():
#     user, created = User.objects.get_or_create(username='superuser')
#     return user

class Trader(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    timestamp = models.DateTimeField(default=timezone.now)
    last_trade_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_trade_time = models.DateTimeField(default=timezone.now)
    total_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calculate_profit(self):
        return self.balance - 100.00

    def __str__(self):
        return self.name
