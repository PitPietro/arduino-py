from pyfirmata import util, Arduino
import time


def joy():
    board = Arduino('/dev/ttyACM1')
    it = util.Iterator(board)
    it.start()

    x_axis = board.get_pin('a:2:i')

    while True:
        analog_x = x_axis.read()
        print('x: {}'.format(analog_x))
        time.sleep(0.1)


if __name__ == '__main__':
    joy()
