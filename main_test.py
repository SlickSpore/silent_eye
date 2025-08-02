import serial
from node.client import Node
from common import encryption_utils
from node.sensors import base, forecasts, arduino

payloads = [
"""
{
    "id": "NODE_001",
    "timestamp": "2025-07-29T12:00:00Z",
    "data": {
        "temperature": 24.5,
        "sound_level": 32.1
    }
}
""",
"""
{
    "id": "NODE_001",
    "timestamp": "2025-07-29T12:30:00Z",
    "data": {
        "temperature": 25.1,
        "sound_level": 45.2
    }
}
""",
"""
{
    "id": "NODE_001",
    "timestamp": "2025-07-29T13:00:00Z",
    "data": {
        "temperature": 27.8,
        "sound_level": 53.4
    }
}
""",
"""
{
    "id": "NODE_002",
    "timestamp": "2025-07-29T13:00:00Z",
    "data": {
        "noise_level": 45,
        "traffic_density": 89
    }
}
"""
]


"""
for payload in payloads:
    sensor = Node(payload)
    sensor.gist()
"""

s_brain = arduino.Sensor()

while KeyboardInterrupt:
    s_brain.iterate()
    payload = base.Pack_Payload(s_brain.node_id, s_brain.payload)
    sensor = Node(payload).gist()
    print("Gist Done!")
    s_brain.__wait__()
    print("Waiting for next sequence.")
