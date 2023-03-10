from controllers.arduino_controller import ArduinoController
from controllers.arduino_controller.sensor import Sensor


sensors = Sensor(5,6, "dis")

arduino = ArduinoController("dustbinv1", 1)

arduino.add_arduino(sensors)

arduino.export_arduino_data()
