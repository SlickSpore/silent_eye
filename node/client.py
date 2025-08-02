import asyncio
from websockets.asyncio.client import connect
from common import config, encryption_utils

class Node:
    
    async def to_brain(self):
        async with connect(
            f"ws://{config.SERVER_PROPERTIES["SERVER_IP_ADDR"]}:{config.SERVER_PROPERTIES["SERVER_PORT"]}",
            ping_interval=None) as websocket:
            await websocket.send(self.payload)
            ack = await websocket.recv()
            if ack != b"0":
                print("Packet Not Accepted!")


    def __init__(self, msg):
        self.payload = encryption_utils.encrypt_message(msg)

    def gist(self):
        asyncio.run(self.to_brain())

