from controllers.arduino_controller import ArduinoController
from controllers.arduino_controller.sensor import Sensor
from temperatura import Temperatura

distancia = Sensor(5, 6, tipo="dis")
sonido = Sensor(25, tipo="son")
temp_hum = Sensor(pin_in=4, tipo="temp")

temperatura = Temperatura()
while True:
    print(temperatura.get_temperatura_humedad())

arduino = ArduinoController("dustbinv1", 1)

arduino.add_arduino(distancia)
arduino.add_arduino(sonido)
arduino.add_arduino(temp_hum)

arduino.export_arduino_data()
