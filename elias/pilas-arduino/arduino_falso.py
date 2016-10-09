#!/usr/bin/env python
class ArduinoFalso(object):

    def __init__(self, baud, port, timeout=None):
        self.port = port
        self.baud = baud
        self.timeout = timeout
        self.output = []
        self.input = []
        self.is_open = True
        self.is_high = 0

    def flush(self):
        pass

    def write(self, line):
        print line
        self.output.append(line)

    def isOpen(self):
        return self.is_open

    def close(self):
        if self.is_open:
            self.is_open = False
        else:
            raise ValueError('Mock serial port is already closed.')

    def readline(self):
        """
        @TODO: This does not take timeout into account at all.
        """
        self.actualizar()
        return self.input.pop(0)

    def reset_mock(self):
        self.output = []
        self.input = []

    def push_line(self, line, term='\r\n'):
        self.input.append(str(line) + term)
        
    def actualizar(self):
        if self.is_high:
            self.is_high -= 1
        else:
            self.is_high +=1  
        self.push_line(self.is_high)
        

