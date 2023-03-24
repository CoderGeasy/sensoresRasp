import sys
import adafruit_dht
from pulseio import PulseIn

class Temperatura:
    def __init__(self, pin):
        self.sensor = adafruit_dht.DHT11(use_pulseio=False)
        self.pin = pin

    def medirTemperatura(self):
        dht_sensor = self.sensor(self.pin)
        dht_sensor.measure()
        hum = dht_sensor.humidity
        temp = dht_sensor.temperature
        return  hum, temp
        


