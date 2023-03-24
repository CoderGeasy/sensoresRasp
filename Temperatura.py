import sys
import adafruit_dht

class Temperatura:
    def __init__(self, pin):
        self.sensor = adafruit_dht.DHT11
        self.pin = pin

    def medirTemperatura(self):
        dht_sensor = self.sensor(self.pin)
        hum, temp = dht_sensor.read()
        return  hum, temp
        


