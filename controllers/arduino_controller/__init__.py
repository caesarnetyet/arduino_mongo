import threading
import time
from uuid import uuid4

from controllers.arduino_controller.arduino import Arduino
from controllers.arduino_controller.sensor import Sensor
from database import Database, ParseJson


class ArduinoController:
    def __init__(self, model: str = 'dustbinv1',  expiration_time: int = 15):
        self.num_threads = 4
        self.model: str = model
        self.client_id: int = 1
        self.expiration_time = expiration_time
        self.db_name = 'test'
        self.collection_name = self.model
        self.sensors: list[Sensor] = []
        self.db = Database(self.db_name)
        self.db.set_collection(self.collection_name)
        self.deletion_thread = threading.Thread(target=self.delete_data)
        self.deletion_thread.start()

    def add_arduino(self, arduino: Sensor):
        self.sensors.append(arduino)

    def set_client(self, id: int):
        self.client_id = id

    def delete_data(self):
        while True:
            time.sleep(self.expiration_time * 60)
            ParseJson(self.collection_name).write([])
            print('Data deleted')

    def export_arduino_data(self):
        while True:
            for sensor_ in self.sensors:
                dict_sensor = sensor_.get_sensors()
                if dict_sensor is not None:
                    arduino_list: Arduino = {
                        'model': self.model,
                        'client_id': self.client_id,
                        'sensors': dict_sensor,
                        '_id': str(uuid4())
                    }
                    self.db.insert(arduino_list, self.collection_name)

