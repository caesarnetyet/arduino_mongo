from controllers.arduino_controller import ArduinoController
from controllers.arduino_controller.sensor import Sensor
from temperatura import Temperatura

distancia = Sensor(5, 6, tipo="dis", description="Sensor de distancia en tapa")
sonido = Sensor(25, tipo="son", description="Sensor de sonido hipotetico")
temp_hum = Sensor(pin_in=4, tipo="temp", description="Detector de humedad para el bote")
led = Sensor(pin_out=26, tipo="led", description="Led de actividad")

arduino = ArduinoController("dustbinv1", 1)

arduino.add_arduino(distancia)
arduino.add_arduino(sonido)
arduino.add_arduino(temp_hum)
arduino.add_arduino(led)

arduino.export_arduino_data()
