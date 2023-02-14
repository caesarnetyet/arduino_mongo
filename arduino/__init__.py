import serial
from typing import TypeVar

T = TypeVar('T')


class Arduino:
    def __init__(self, interface: T, port, baudrate: int = 9600, ):
        self.interface: T = interface
        self.port: str = port
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.ser.flush()

    def write(self, msg):
        self.ser.write(msg.encode('utf-8'))

    def get_keys(self) -> list[str]:
        return self.interface.__annotations__.keys()

    def read(self):
        return self.ser.readline().decode('utf-8').rstrip()

    def get_dict(self) -> T:
        self.write("read")
        data = self.read()
        data = data.split(",")
        formated_data = [x.strip() for x in data]
        keys = self.get_keys()
        return dict(zip(keys, formated_data))

    def close(self):
        self.ser.close()
