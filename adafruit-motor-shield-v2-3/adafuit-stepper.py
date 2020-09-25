import time
import board
from adafruit_motorkit import MotorKit


def stepper():
    kit = MotorKit(i2c=board.I2C())
    for i in range(100):
        kit.stepper1.opestep()
        time.sleep(0.05)


if __name__ == '__main__':
    stepper()
