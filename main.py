from controllers.arduino_controller import ArduinoController
from controllers.arduino_controller.sensor import Sensor
from temperatura import Temperatura

distancia = Sensor(6, 5, tipo="dis", id_="dis1",description="Sensor de distancia en tapa")
sonido = Sensor(25, tipo="son", id_="son1", description="Sensor de sonido hipotetico")
temp = Sensor(pin_in=21, tipo="temp",  id_="temp1", description="Detector de humedad para el bote")
hum = Sensor(pin_in=21, tipo="hum",  id_="hum1", description="Detector de humedad para el bote")
led = Sensor(pin_out=4, tipo="led", id_="led1", description="Led de actividad")
temperature = Temperatura(21)

while True:
    print(temperature.get_temperatura_humedad())

arduino = ArduinoController("dustbinv1", 1)

arduino.add_arduino(distancia)
arduino.add_arduino(sonido)
arduino.add_arduino(temp)
arduino.add_arduino(hum)
arduino.add_arduino(led)

arduino.export_arduino_data()
