import requests
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


API_ENDPOINT = "http://localhost:8888/createconv"
API_KEY = "XXXXXXXXXXXXXXXXX"


data={
    "topic":"newtopic",
}

r = requests.post(url = API_ENDPOINT, data = json.dumps(data))
print(r.content)
print(r.text)
rj = json.loads(r.text)
print(rj)
print(rj["uid"])
print("http://app.immersmedia.in/join/"+rj["uid"])
# print(r.text["uid"])
