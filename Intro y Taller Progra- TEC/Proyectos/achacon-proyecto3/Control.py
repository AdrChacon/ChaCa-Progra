import serial, time

arduino = serial.Serial("COM3", 9600)
def Control():
        arduino.reset_input_buffer()
        Joystick = []
        Joystick = Joystick + [arduino.readline()]
        if Joystick[0] == b'9\r\n':
            return
        else:
            return Joystick[0]
        
