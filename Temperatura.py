import sys
import adafruit_dht

class Temperatura:
    def __init__(self, pin):
        self.sensor = adafruit_dht.DHT11
        self.pin = pin

    def medirTemperatura(self):
        hum, temp = adafruit_dht.DHT11.read(self.sensor, self.pin)
        return  hum, temp
        


