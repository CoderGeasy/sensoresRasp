import sys
import adafruit_dht

pin=4

sensor = adafruit_dht.DHT11(pin)
class Temperatura:
    def __init__(self, pin):
        self.sensor = adafruit_dht.DHT11
        self.pin = pin

    def medirTemperatura(self):
        hum = sensor.humidity
        temp = sensor.temperature

        # Imprime en la consola las variables temperatura y humedad con un decimal
        print('Temperatura={0:0.1f} C  Humedad={1:0.1f}%'.format(temp, hum))
        


