from pyfirmata import util, Arduino
import time


def potentiometer():
    board = Arduino('/dev/ttyACM0')
    it = util.Iterator(board)
    it.start()

    analog_input = board.get_pin('a:0:i')

    while True:
        analog_value = analog_input.read()
        print(analog_value)
        time.sleep(0.1)


if __name__ == '__main__':
    potentiometer()
