from controllers.arduino_controller import ArduinoController
from controllers.arduino_controller.sensor import Sensor

distancia = Sensor(5, 6, tipo="dis")
sonido = Sensor(25, tipo="son")
temp_hum = Sensor(23, tipo="temp")

arduino = ArduinoController("dustbinv1", 1)

arduino.add_arduino(distancia)
arduino.add_arduino(sonido)
arduino.add_arduino(temp_hum)

arduino.export_arduino_data()
