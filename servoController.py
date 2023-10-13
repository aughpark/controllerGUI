from tkinter import *
from pyfirmata import Arduino, util
import time
import threading


class ServoController:
    def __init__(self, port, pin_number):
        self.board = Arduino(port)
        self.servo_pin = self.board.get_pin(f'd:{pin_number}:s')
        self.isMoving = False

    # Move Servo Function (ROM: 0-180)
    def move_servo(self, angle):
        self.servo_pin.write(angle)

    # Continuously Rotate Servo by 5 degree ticks
    def auto_rotate(self):
        while self.isMoving:
            for angle in range(0, 181, 5):
                if not self.isMoving:
                    break
                self.move_servo(angle)
                time.sleep(0.05)
            for angle in range(180, -1, -5):
                if not self.isMoving:
                    break
                self.move_servo(angle)
                time.sleep(0.05)

    # Start Function: Changes status to true and allows for program to continually run without waiting
    def start(self):
        self.isMoving = True
        threading.Thread(target=self.auto_rotate, daemon=True).start()

    # Stop Function: Changes status to false
    def stop(self):
        self.isMoving = False

    def cleanup(self):
        self.board.exit()
