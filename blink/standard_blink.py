from pyfirmata import util, Arduino
import time


def blink(b_time):
    board = Arduino('/dev/ttyACM0')
    it = util.Iterator(board)
    it.start()

    led_13 = board.get_pin('d:13:o')
    while True:
        led_13.write(1)
        print('Led ON')
        time.sleep(b_time)
        led_13.write(0)
        print('Led OFF')
        time.sleep(b_time)


if __name__ == '__main__':
    blink(0.2)
