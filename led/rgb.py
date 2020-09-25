from pyfirmata import util, Arduino
import time


def rgb():
    board = Arduino('/dev/ttyACM0')
    # it = util.Iterator(board)
    # it.start()

    red_pin = board.get_pin('d:11:p')
    green_pin = board.get_pin('d:10:p')
    blue_pin = board.get_pin('d:9:p')
    print('PWM says: \"Let\'s start!\"')
    red_pin.write(0)
    green_pin.write(0)
    blue_pin.write(0)
    time.sleep(0.5)
    print('START')
    green_pin.write(0.1)
    time.sleep(5)
    print('STOP')
    green_pin.write(0)


if __name__ == '__main__':
    rgb()
