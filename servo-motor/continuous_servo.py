from pyfirmata import util, Arduino
import time


def servo():
    board = Arduino('/dev/ttyACM0')
    # it = util.Iterator(board)
    # it.start()

    servo_pin = board.get_pin('d:10:p')
    print('PWM says: \"Let\'s start!\"')
    while True:
        for i in range(0, 101, 4):
            s_value = i / 100
            servo_pin.write(s_value)
            print('value: ', s_value)
            time.sleep(0.05)
        print('Stop')
        time.sleep(1)
        print('Start')
        for i in range(100, -1, -4):
            s_value = i / 100
            servo_pin.write(s_value)
            print('value: ', s_value)
            time.sleep(0.05)
        time.sleep(1)
        print('Stop')


if __name__ == '__main__':
    servo()
