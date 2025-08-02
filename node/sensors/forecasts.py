import requests
from urllib.request import urlopen
from common.config import SERVER_PROPERTIES
from node.sensors import base
from bs4 import BeautifulSoup
import re
import time

"""
    Example node that scraps values for milan
"""

url = f"http://www.meteosystem.com/wlip/milano/dati.php"

class Sensor:       # Sensor Brain Object, implement your code to gather data
    def __init__(self):
        self.payload = {}
        self.node_id = "FORECASTS_MI_001_"

        self.return_payloads = [] 

    def __wait__(self):
        t = 0
        while t < 60*SERVER_PROPERTIES["REFRESH_DELAY_MINUTES"]:
            print("Enlapsed: "+str(t)+"s", end='\r')
            t+=1
            time.sleep(1)
        print()

    def iterate(self):
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        print("Retrieving Data")

        soup = BeautifulSoup(html, "lxml")

        params = []

        for i in soup.findAll("td"):
            param = str(i.find("strong"))
            if param != 'None': 
                try:
                    params.append(
                    float(
                        param.replace("<strong>","")
                        .replace("</strong>","")
                        .replace("°C","")
                        .replace("hPa","")
                        .replace("Km/h","")
                        .replace("mm/h","")
                        .replace("mm","")
                        .replace("%","")
                        )
                    )
                except:
                    pass

        self.payload["t_now"] = params[0]
        self.payload["t_low"] = params[1]
        self.payload["t_high"] = params[2]

        self.payload["h_now"] = params[3]
        self.payload["h_low"] = params[4]
        self.payload["h_high"] = params[5]

        self.payload["p_now"] = params[11]
        self.payload["p_low"] = params[12]
        self.payload["p_high"] = params[13]

        self.payload["w_now"] = params[16]
        self.payload["w_avrg"] = params[17]
        self.payload["w_high"] = params[18]

        print("Got Payload")

if __name__ == "__main__":
    s_brain = Sensor()

    while KeyboardInterrupt:
        s_brain.iterate()
        base.Pack_Payload(s_brain.node_id, s_brain.payload)

