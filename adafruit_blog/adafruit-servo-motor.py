import time
import board
import pulseio
from adafruit_motor import servo


"""
High Level Servo Control
"""


def continuous_servo():
    # Continuous Servo Test Program for CircuitPython

    # create a PWMOut object on Pin A2.
    pwm = pulseio.PWMOut(board.A2, frequency=50)

    # Create a servo object, my_servo.
    my_servo = servo.ContinuousServo(pwm)

    while True:
        print("forward")
        my_servo.throttle = 1.0
        time.sleep(2.0)
        print("stop")
        my_servo.throttle = 0.0
        time.sleep(2.0)
        print("reverse")
        my_servo.throttle = -1.0
        time.sleep(2.0)
        print("stop")
        my_servo.throttle = 0.0
        time.sleep(4.0)


if __name__ == '__main__':
    continuous_servo()
    # https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/troubleshooting
