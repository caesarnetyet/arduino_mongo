from uuid import uuid4

import serial
from typing import TypeVar

T = TypeVar('T')


class Sensor:
    def __init__(self, interface: T, port, baudrate: int = 9600, ):
        self.interface: T = interface
        self.port: str = port
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.ser.flush()

    def write(self, msg):
        self.ser.write(msg.encode('utf-8'))

    def interface_name(self) -> str:
        return self.interface.__name__

    def read(self):
        return self.ser.readline().decode('utf-8').rstrip()

    def get_dict(self) -> T:
        dict_data = {"_id": str(uuid4())}

        data = self.read()
        sensors = data.split(",")
        for sensor in sensors:
            sensor = sensor.split(":")
            try:
                dict_data[sensor[0]] = float(sensor[1])
            except ValueError:
                dict_data[sensor[0]] = sensor[1]
        return dict_data

    def close(self):
        self.ser.close()
