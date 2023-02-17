from controllers.arduino_controller.sensor import Sensor
from database import Database


class ArduinoController:
    def __init__(self, db_name: str = "test"):
        self.db_name = db_name
        self.arduinos: list[Sensor] = []
        self.db = Database(db_name)

    def add_arduino(self, arduino: Sensor):
        self.arduinos.append(arduino)

    def export_data(self):
        while True:
            for arduino in self.arduinos:
                self.db.set_collection(arduino.interface_name())
                self.db.insert(arduino.get_dict(), arduino.interface_name())
