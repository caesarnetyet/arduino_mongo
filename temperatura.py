import Adafruit_DHT
import RPi.GPIO as GPIO


class Temperatura:
    def __init__(self, pin = 4):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = pin
        GPIO.setmode(GPIO.BCM)

    def get_temperatura_humedad(self):
        temperatura, humedad = Adafruit_DHT.read(self.sensor, self.pin)

        if temperatura is not None and humedad is not None:
            datos = [temperatura, humedad]
            return datos
        else:
            return [0, 0]
