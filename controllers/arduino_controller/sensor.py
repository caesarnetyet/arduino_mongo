import time
from datetime import datetime
from uuid import uuid4
import Adafruit_DHT
import RPi.GPIO as GPIO

class Sensor:
    def __init__(self, pin_in=0, pin_out=0, tipo="son", id_="Sensor", description=""):
        self.adafruit = Adafruit_DHT.DHT11
        self.id_ = id_
        self.type = tipo
        self.pin_in = pin_in
        self.pin_out = pin_out
        self.description = description
        self.pulse_start = 0.0
        self.pulse_end = 0.0
        GPIO.setmode(GPIO.BCM)
        if tipo is not "hum" or tipo is not "temp":
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
        elif self.type == "hum":
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
            return self.get_dict("Sonido no detectado")

    def on(self):
        GPIO.output(self.pin_out, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin_out, GPIO.LOW)

    def blink(self):
        self.toggle = not self.toggle
        if self.toggle:
            self.on()
            return self.get_dict(self.toggle)
        else:
            self.off()
            return None

    def get_dict(self, valor):
        return {
            "tipo": self.type,
            "id": self.id_,
            "valor": valor,
            "detalles_sensor": {
                "pin_in": self.pin_in,
                "pin_out": self.pin_out,
                "descripcion": self.description
            },
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "_id": str(uuid4())
        }

    def get_temperatura_humedad(self):
        temperatura, humedad = Adafruit_DHT.read(self.adafruit, self.pin_in)
        print(temperatura, humedad, self.adafruit, self.pin_in)
        if temperatura is not None and humedad is not None:
            datos = [temperatura, humedad]
            if self.type == 'temp':
                return self.get_dict(datos[0])
            if self.type == 'hum':
                return self.get_dict(datos[1])
        else:
            return None

    def medir(self):
        time.sleep(1)
        GPIO.output(self.pin_out, False)
        time.sleep(0.00001)
        GPIO.output(self.pin_out, True)
        while not GPIO.input(self.pin_in):
            self.pulse_start = time.time()
        while GPIO.input(self.pin_in):
            self.pulse_end = time.time()
        sig_time = self.pulse_end - self.pulse_start
        distance = sig_time / 0.000058
        return self.get_dict(distance)

    def __del__(self):
        GPIO.cleanup()
