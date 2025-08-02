import requests
import re
import node.sensors.base
from common.config import SERVER_PROPERTIES
import time

"""
    Example node that scraps a temperature value for milan
"""

url = f""

class Sensor:       # Sensor Brain Object, implement your code to gather data
    def __init__(self):
        self.payload = {}
        self.node_id = "TEMP_001_MI"

    def __wait__(self):
        time.sleep(60*SERVER_PROPERTIES["REFRESH_DELAY_MINUTES"])

    def iterate(self):
        response = requests.get(url)
        
        for i in response.text.split('\n'):
            if "air-temp" in i.lower():
                temp = re.findall(r'-?\d{1,3}°', i)
                self.payload["temperature"] = str(temp)[2::][:2]
        
        self.__wait__()
    
if __name__ == "__main__":
    s_brain = Sensor()

    while KeyboardInterrupt:
        s_brain.iterate()
        node.base.Pack_Payload(s_brain.node_id, s_brain.payload)

