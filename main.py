import servoController
from tkinter import *
from pyfirmata import Arduino, SERVO, util

# Arduino Pinout
servoPin = 9

# Serial to USB connection
port = 'COM3'
servoController = servoController.ServoController(port, servoPin)

# Creation of GUI Window
root = Tk()
root.title("Servo GUI")

# VARIABLES
isMoving = BooleanVar(value=False)
currAngleVar = IntVar(value=0)
currAngleStr = StringVar()
currAngleStr.set("CURRENT ANGLE: ---")

# FUNCTIONS


def start():
    start_button['state'] = DISABLED
    stop_button['state'] = NORMAL
    servoController.start()


def stop():
    start_button['state'] = NORMAL
    stop_button['state'] = DISABLED
    servoController.stop()


def send():
    try:
        angle = int(inputPOS.get())
        if 0 <= angle <= 180:
            currAngleVar.set(angle)
            currAngleStr.set(f"CURRENT ANGLE: {angle}")
            servoController.move_servo(angle)
        else:
            currAngleStr.set("Invalid input. Enter an integer between 0 and 180")
    except ValueError:
        currAngleStr.set("Invalid input. Enter an integer between 0 and 180")


def set_servo_angle(val):
    angle = int(float(val))
    currAngleVar.set(angle)
    currAngleStr.set(f"CURRENT ANGLE: {angle}")
    servoController.move_servo(angle)


# Make UI resizable
root.columnconfigure([0, 1, 2], weight=1)
root.rowconfigure([0, 1, 2], weight=1)

# Initialization
desiredPOS = Label(text="INPUT TARGET: (0-180) ")
inputPOS = Entry()
positionSend = Button(root, text="Send", command=send, padx=10, pady=5)
currAngle = Label(textvariable=currAngleStr, padx=100, pady=10)
start_button = Button(root, text="Start", command=start, padx=50, pady=10)
stop_button = Button(root, text="Stop", state=DISABLED, command=stop, padx=50, pady=10)
servoSlider = Scale(root, from_=0, to=180, orient=HORIZONTAL, command=set_servo_angle)


# GRID
desiredPOS.grid(row=0, column=0, padx=10, pady=5, sticky=W)
inputPOS.grid(row=0, column=1, padx=10, pady=5, sticky=E+W)
positionSend.grid(row=0, column=2, padx=10, pady=5, sticky=E)


servoSlider.grid(row=1, column=0, columnspan=3, sticky=E+W)

currAngle.grid(row=2, column=0, padx=10, pady=5, sticky=W)
start_button.grid(row=2, column=1, padx=10, pady=5, sticky=E+W)
stop_button.grid(row=2, column=2, padx=10, pady=5, sticky=E+W)

root.mainloop()
