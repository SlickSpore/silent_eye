import datetime
import json

def Pack_Payload(id, data) -> dict:
    payload = {}
    payload["id"] = id + str(datetime.datetime.now())[:10]
    payload["timestamp"] = str(datetime.datetime.now())[:19][11:]
    payload["data"] = data
    return json.dumps(payload)
