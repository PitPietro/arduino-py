from pyfirmata import util, Arduino
import time


def smart_shield():
    board = Arduino('/dev/ttyACM0')
    it = util.Iterator(board)
    it.start()

    motor_a_dir = board.get_pin('d:7:o')
    # PWM
    motor_a_speed = board.get_pin('d:6:p')

    my_motor = board.get_pin('d:3:p')

    while True:
        print('I\'m in')
        motor_a_dir.write(0)
        motor_a_speed.write(0.9)
        # my_motor.write()
        time.sleep(0.1)


if __name__ == '__main__':
    smart_shield()
