from controllers.arduino_controller import ArduinoController
from controllers.arduino_controller.sensor import Sensor


sensors = Sensor(type= 'Distance', port="/dev/cu.usbmodem14101")

arduino = ArduinoController("dustbinv1", 1)

arduino.add_arduino(sensors)

arduino.export_arduino_data()
