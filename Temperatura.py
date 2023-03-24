import sys
import adafruit_dht

class Temperatura:
    def __init__(self, pin):
        self.sensor = adafruit_dht.DHT11
        self.pin = pin

    def medirTemperatura(self):
        hum, temp = self.sensor.read(self.pin)
        return  hum, temp
        


