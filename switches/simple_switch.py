from pyfirmata import util, Arduino


def switch():
    board = Arduino('/dev/ttyACM0')
    it = util.Iterator(board)
    it.start()

    digital_input = board.get_pin('d:10:i')
    led_13 = board.get_pin('d:13:o')
    while True:
        sw_value = digital_input.read()
        if sw_value:
            led_13.write(1)
            print('Led ON')
        else:
            led_13.write(0)
            print('Led OFF')


if __name__ == '__main__':
    switch()
