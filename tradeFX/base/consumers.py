import asyncio
from asgiref.sync import async_to_sync, sync_to_async
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Trader
# import logging

# logger = logging.getLogger(__name__)

class TraderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send_initial_trader_data()
        await self.start_periodic_updates()

    async def disconnect(self, close_code):
        print(f"WebSocket disconnected with close code: {close_code}")

    async def send_initial_trader_data(self):
        trader_data = await self.fetch_trader_data()
        # logger.info('Sending initial trader data')
        await self.send(json.dumps({
            'type': 'trader_data',
            'data': trader_data,
        }))

    async def send_trader_data(self, event):
        trader_data = event['trader_data']
        # logger.info('Sending trader data')
        await self.send(json.dumps({
            'type': 'trader_data',
            'data': trader_data,
        }))

    async def start_periodic_updates(self):
        while True:
            trader_data = await self.fetch_trader_data()
            # logger.info("Sending trader data from periodic")
            await self.send_trader_data({"trader_data": trader_data})
            await asyncio.sleep(60)

    @sync_to_async
    def fetch_trader_data(self):
        traders = Trader.objects.all()
        trader_data = [
            {
                'id': trader.id, 
                'name': trader.name, 
                'total_profit': str(trader.total_profit), 
                'timestamp': trader.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                'last_trade_time': trader.last_trade_time.strftime("%Y-%m-%d %H:%M:%S"),
                'last_trade_profit': str(trader.last_trade_profit), 
                'balance': str(trader.balance)
            } 
            for trader in traders]
        return trader_data

    async def websocket_receive(self, event):
        message_type = event.get("type")

        if message_type == "websocket.receive":
            message_text = event.get("text", "")
            try:
                message_data = json.loads(message_text)
                if message_data.get("type") == "get_trader_data":
                    trader_data = await self.fetch_trader_data()
                    await self.send_trader_data({"trader_data": trader_data})
            except json.JSONDecodeError:
                print("Invalid JSON message received")
