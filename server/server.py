import asyncio
from websockets.asyncio.server import serve
import logging
from common import config
from server import decryptor

logging.basicConfig (
    format="%(asctime)s %(message)s",
    level=logging.DEBUG
)

logger = logging.getLogger("websockets")
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler())

brain = decryptor.Brain(config.SERVER_PROPERTIES["DATA_PATH"])

async def acknowledge(websocket):
    async for data in websocket:
        brain.sense(data)
        if brain.dump_node_data(): websocket.send(b"1")
        brain.read_data()
        brain.write_data()
        await websocket.send(b"0")

async def server():
    async with serve(
        acknowledge, 
        config.SERVER_PROPERTIES["SERVER_IP_ADDR"], 
        config.SERVER_PROPERTIES["SERVER_PORT"]
    ) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(server())