import requests
import json
import codecs
def get_location(address):
    url = "http://restapi.amap.com/v3/geocode/geo"
    data = {
        'key': 'e3745346ba319d6fc4e7b3f40a909b61',
        'address': address
    }
    r = requests.post(url, data=data).json()
    GPS = r['geocodes'][0]['location'].split(",")
    print(GPS[0])
    print(GPS[1])

f = codecs.open("D:\highpython\Python-master\learn\9.txt", "r", "utf-8")
while True:
    line = f.readline()
    if not line:
        f.close()
        break
    get_location(line)
        

