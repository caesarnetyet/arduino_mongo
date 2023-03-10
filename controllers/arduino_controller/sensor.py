import time
from datetime import datetime

import Adafruit_DHT
import RPi.GPIO as GPIO


class Sensor:
    def __init__(self, pin_in=0, pin_out=0, tipo="son"):
        self.adafruit = Adafruit_DHT.DHT11
        self.type = tipo
        self.pin_in = pin_in
        self.pin_out = pin_out
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_in, GPIO.IN)
        GPIO.setup(pin_out, GPIO.OUT)
        self.toggle = False

    def get_data(self):
        if self.type == "son":
            return self.get_sound()
        elif self.type == "dis":
            return self.medir()
        elif self.type == "temp":
            return self.get_temperatura_humedad()
        elif self.type == "led":
            return self.blink()
        else:
            return self.get_dict(self.read())

    def read(self):
        return GPIO.input(self.pin_in)

    def get_sound(self):
        data = self.read()
        if data == 1:
            return self.get_dict("Sonido detectado")
        else:
            return self.get_dict( "Sonido no detectado")

    def on(self):
        GPIO.output(self.pin_out, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin_out, GPIO.LOW)

    def blink(self):
        self.toggle = not self.toggle
        if self.toggle:
            self.on()
        else:
            self.off()
        return self.get_dict(self.toggle)

    def get_dict(self,  valor):
        return {
            "valor": valor,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

    def get_temperatura_humedad(self):
        humedad, temperatura = Adafruit_DHT.read(self.adafruit, self.pin_in)

        if temperatura is not None and humedad is not None:
            datos = [temperatura, humedad]
            return {"temp": datos[0], "hum": datos[1], "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
        else:
            return {"temp": 0, "hum": 0, "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

    def medir(self):
        time.sleep(1)
        GPIO.output(self.pin_out, False)
        time.sleep(0.00001)
        GPIO.output(self.pin_out, True)
        while GPIO.input(self.pin_in) == False:
            pulse_start = time.time()
        while GPIO.input(self.pin_in) == True:
            pulse_end = time.time()
        sig_time = pulse_end - pulse_start
        distance = sig_time / 0.000058
        return self.get_dict( distance)

    def __del__(self):
        GPIO.cleanup()
