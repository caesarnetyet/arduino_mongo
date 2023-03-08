from datetime import datetime
from uuid import uuid4

import serial


class Sensor:
    def __init__(self,type, port, baudrate: int = 9600):
        self.port: str = port
        self.type: str = type
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            self.ser.flush()
        except serial.SerialException:
            raise Exception("No se pudo conectar al puerto: " + port)

    def write(self, msg):
        self.ser.write(msg.encode('utf-8'))

    def read(self):
        return self.ser.readline().decode('utf-8').rstrip()

    def get_sensors(self):
        all: list[dict] = []
        data = self.read()
        if data == "":
            return None
        sensors = data.split(",")
        for sensor in sensors:
            sensor = sensor.split(":")
            if sensor == ['']:
                continue
            add_sensor = {
                'type': self.getType(sensor[0][0]),
                'value': sensor[1],
                'date': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                'id': sensor[0]
            }
            all.append(add_sensor)
        return all

    def get_sensor(self):
        data = self.read()
        if data == "":
            return None
        sensors = data.split(",")
        for sensor in sensors:
            sensor = sensor.split(":")
            if sensor == ['']:
                continue
            add_sensor = {
                'type': self.getType(sensor[0][0]),
                'value': sensor[1],
                'date': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                'id': sensor[0]
            }
            return add_sensor

    def close(self):
        self.ser.close()

    def getType(self, tipo: str):
        match tipo:
            case 'd' | 'D':
                return 'distance'
            case 't' | 'T':
                return 'temperature'
            case 'h' | 'H':
                return 'humidity'
            case _:
                return 'generic'

