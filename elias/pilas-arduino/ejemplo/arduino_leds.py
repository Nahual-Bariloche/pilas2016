import time
from pilas_arduino.arduino_pilas import iniciar_arduino, ActuadorDigital

# python -m ejemplo.arduino_leds

def esperar(segundos):
    time.sleep(segundos)
    pass

arduino =iniciar_arduino();
led1 = ActuadorDigital(pin=10)
led2 = ActuadorDigital(pin=11)
led1.enceder()
esperar(2)
led2.enceder()
esperar(2)
led1.apagar()
esperar(2)
led2.apagar()