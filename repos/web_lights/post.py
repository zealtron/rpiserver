import requests, json, time

for x in xrange(256):
    payload = {
            "lights": [

                {"lightId": 3, "red":255,"green":x,"blue":0, "intensity": 0.3},
                {"lightId": 10, "red":x,"green":0,"blue":255, "intensity": 0.5},
                {"lightId": 15, "red":255,"green":x,"blue":255, "intensity": 0.5},
                {"lightId": 20, "red":0,"green":255,"blue":x, "intensity": 0.7}],

            "propagate":False
            }
    url = "http://172.27.98.227:80/rpi"

    r = requests.post(url, data = json.dumps(payload))
    print x
    time.sleep(.1)

print r.text
