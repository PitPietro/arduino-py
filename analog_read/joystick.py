from pyfirmata import util, Arduino
import time


def joy():
    board = Arduino('/dev/ttyACM1')
    it = util.Iterator(board)
    it.start()

    x_axis = board.get_pin('a:2:i')
    y_axis = board.get_pin('a:3:i')
    joy_press = board.get_pin('d:7:i')
    s1 = board.get_pin('d:4:i')
    s2 = board.get_pin('d:3:i')
    s3 = board.get_pin('d:2:i')

    while True:
        x = x_axis.read()
        y = y_axis.read()
        d7_press = analog_state(joy_press)
        s1_press = analog_state(s1)
        s2_press = analog_state(s2)
        s3_press = analog_state(s3)
        print('x = {}; y = {}; joy press = {}; S3-D2: {}; S2-D3: {}; S1-D4: {}'
              .format(x, y, d7_press, s1_press, s2_press, s3_press))
        time.sleep(0.2)


def analog_state(analog_input):
    if analog_input.read():
        return 'UP'
    else:
        return 'DOWN'


if __name__ == '__main__':
    print('(x; y)')
    print('TRUE --> NOT pressed\nFALSE --> pressed')
    joy()
