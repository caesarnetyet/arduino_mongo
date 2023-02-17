import concurrent.futures
from controllers.arduino_controller.sensor import Sensor
from database import Database


class ArduinoController:
    def __init__(self, db_name: str = "test", threads: int = 4):
        self.db_name = db_name
        self.arduinos: list[Sensor] = []
        self.db = Database(db_name)
        self.num_threads = threads

    def add_arduino(self, arduino: Sensor):
        self.arduinos.append(arduino)

    def export_data(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = []
            for arduino in self.arduinos:
                future = executor.submit(self.export_arduino_data, arduino)
                futures.append(future)
            concurrent.futures.wait(futures)

    def export_arduino_data(self, arduino: Sensor):
        self.db.set_collection(arduino.interface_name())
        self.db.insert(arduino.get_dict(), arduino.interface_name())