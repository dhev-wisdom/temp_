from background_task import background
from .models import Trader
from decimal import Decimal
from django.utils import timezone, timesince
import random

def simulate_profit_loss():
    traders = Trader.objects.all()

    for trader in traders:
        profit_or_loss = Decimal(str(random.uniform(-10, 10)))
        trader.balance += profit_or_loss
        trader.last_trade_profit = profit_or_loss
        trader.last_trade_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        trader.total_profit = trader.balance - 100
        trader.save()