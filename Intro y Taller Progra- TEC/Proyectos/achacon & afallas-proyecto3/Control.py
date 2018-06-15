import serial, time

# Se define el arduino en el puerto COM3
arduino = serial.Serial("COM3", 9600)


def Control():
        """Esta funcion lee la informacion enviada por el Arduino"""
        arduino.reset_input_buffer()
        Joystick = []
        Joystick = Joystick + [arduino.readline()]
        if Joystick[0] == b'9\r\n':
            return
        else:
            return Joystick[0]
        
