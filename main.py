from controllers.arduino_controller import ArduinoController
from controllers.arduino_controller.sensor import Sensor
from interfaces.distance import Distance

#En sensor va la interfaz, el puerto del arduino y opcionalmente el baudrate o la banda de bits
distance = Sensor(interface=Distance, port="COM3")

#Cuando definimos el arduino controller le pasamos el nombre de la base de datos
arduino = ArduinoController("Test2")

arduino.add_arduino(distance)

arduino.export_data()
