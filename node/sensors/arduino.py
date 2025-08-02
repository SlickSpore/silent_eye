import serial
import time
from common.config import SERVER_PROPERTIES


class Sensor:
    def __init__(self):
        self.payload = {}
        self.node_id = "DHT_11_TEMP-HYGRO_"
    
    def __wait__(self):
        t = 0
        while t < 60*SERVER_PROPERTIES["REFRESH_DELAY_MINUTES"]:
            print("Enlapsed: "+str(t)+"s", end='\r')
            t+=1
            time.sleep(1)
        print()

    def iterate(self):
        sensor = serial.Serial('/dev/cu.usbmodem1401')
        
        data = list(
            map(
                int,
                    str(
                        sensor.readline()
                    ).removeprefix("b'").
                    removesuffix("\\r\\n'").
                    split(":")
                )
            )
        
        self.payload["t_now"] = data[0]
        self.payload["h_now"] = data[1]