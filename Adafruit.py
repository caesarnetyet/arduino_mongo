from datetime import datetime
from uuid import uuid4

import Adafruit_DHT
import RPi.GPIO as GPIO


class Adafruit:
    def __init__(self, pin = 4, tipo="temp", id_="sensor_gen1", description="sensor"):
        self.tipo = tipo
        self.id_ = id_
        self.sensor = Adafruit_DHT.DHT11
        self.pin = pin
        self.description = description
        GPIO.setmode(GPIO.BCM)
    def get_data(self):
        return self.get_temperatura_humedad()

    def get_temperatura_humedad(self):
        temperatura, humedad = Adafruit_DHT.read(self.sensor, self.pin)

        print(temperatura, humedad)
        print(self.sensor)
        print(self.pin)

        if temperatura is not None and humedad is not None:
            datos = [temperatura, humedad]
            if self.tipo == "temp":
                return self.get_dict(datos[0])
            return self.get_dict(datos[1])

        return None

    def get_dict(self, valor):
        return {
            "tipo": self.tipo,
            "id": self.id_,
            "valor": valor,
            "detalles_sensor": {
                "pin_in": self.pin,
                "descripcion": self.description
            },
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "_id": str(uuid4())
        }