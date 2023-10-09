from asgiref.sync import async_to_sync
# import channels.layers
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Trader


# channel_layer = channels.layers.get_channel_layer()

class TraderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        print(f"WebSocket disconnected with close code: {close_code}")

    async def send_trader_data(self, event):
        trader_data = event['trader_data']
        print('Sending trader data:', trader_data)
        await self.send(json.dumps({
            'type': 'trader_data',
            'data': trader_data,
        }))

    @staticmethod
    def fetch_trader_data():
        traders = Trader.objects.all()
        trader_data = [
            {
                'id': trader.id, 
                'name': trader.name, 
                'total_profit': trader.total_profit, 
                'timestamp': trader.timestamp,  # Format timestamp .strftime("%Y-%m-%d %H:%M:%S")
                'last_trade_time': trader.last_trade_time,  # Format last_trade_time .strftime("%Y-%m-%d %H:%M:%S")
                'last_trade_profit': trader.last_trade_profit, 
                'balance': str(trader.balance)
            } 
            for trader in traders]
        print("fetch_trader_data end")
        return trader_data

    async def websocket_receive(self, event):
        message_type = event.get("type")

        if message_type == "get_trader_data":
            trader_data = await async_to_sync(self.fetch_trader_data)()
            await self.send_trader_data({"trader_data": trader_data})
