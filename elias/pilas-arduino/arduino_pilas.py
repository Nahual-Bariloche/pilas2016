#!/usr/bin/env python
from Arduino import Arduino
from arduino_falso import ArduinoFalso

class _ArduinoPilas(Arduino):
    _instance = None
    _setted = False;
    _init = False;
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(_ArduinoPilas, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self,baud=9600, port=None, init=False):
        if not self._init and not init:
            mensaje = "Arudino no fue inicializado usar la funcion iniciar_arduino()!"
            raise Exception(mensaje)
        if self._init and init:
            mensaje = "Arudino ya fue inicializado anteriormente!"
            raise Exception(mensaje)         
        if init:
            self._init = True
        if not self._setted:
            try:
                Arduino.__init__(self, baud, port)
            except:
                mock_serial = ArduinoFalso(baud, '/dev/ttyACM0')
                Arduino.__init__(self, sr=mock_serial)
            self._setted =True
            
    def __del__(self):
        self.close()
        
class ActuadorDigital(object):    
    def __init__(self,arduino=None, pin=13):
        if arduino == None:
            arduino=_ArduinoPilas()
        self.arduino = arduino
        self.pin = pin
      
    def enceder(self):
        self.arduino.digitalWrite(self.pin,"HIGH")
    
    def apagar(self):
        self.arduino.digitalWrite(self.pin,"LOW")

def iniciar_arduino(baud=9600, port=None):   
    return _ArduinoPilas(baud, port, init=True)
