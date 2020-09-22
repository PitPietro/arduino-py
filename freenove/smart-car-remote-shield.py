from pyfirmata import util, Arduino
import turtle
import time

MIDDLE = 0.5


class RemoteShield:
    def __init__(self, pot_1, pot_2, x_axis, y_axis, joy_press, s1, s2, s3):
        self.pot_1 = pot_1
        self.pot_2 = pot_2
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.joy_press = joy_press
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def remote_shield(self):
        it = util.Iterator(board)
        it.start()
        while True:
            x = self.x_axis.read()
            y = self.y_axis.read()
            d7_press = analog_state(self.joy_press)
            s1_press = analog_state(self.s1)
            s2_press = analog_state(self.s2)
            s3_press = analog_state(self.s3)
            pot_1_press = self.pot_1.read()
            pot_2_press = self.pot_2.read()
            print('x = {}; y = {}; joy press = {}; S3-D2: {}; S2-D3: {}; S1-D4: {}; POT1: {}; POT": {}'
                  .format(x, y, d7_press, s1_press, s2_press, s3_press, pot_1_press, pot_2_press))
            print(pot_1_press)
            time.sleep(0.2)

    def joy_draw(self):
        it = util.Iterator(board)
        it.start()
        pen = turtle.Turtle()
        pen.home()

        while True:
            x = round(self.x_axis.read(), 1)
            y = round(self.y_axis.read(), 1)

            if x > MIDDLE:
                new_pos = pen.xcor() + 10
                pen.setx(new_pos)
            elif x < MIDDLE:
                new_pos = pen.xcor() - 10
                pen.setx(new_pos)

            if y < MIDDLE:
                new_pos = pen.ycor() + 10
                pen.sety(new_pos)
            elif y > MIDDLE:
                new_pos = pen.ycor() - 10
                pen.sety(new_pos)

            print(x, '  ', y)
            time.sleep(0.1)

    def drawing(self):
        it = util.Iterator(board)
        it.start()
        pen = turtle.Turtle()
        pen.home()
        move_n = 50
        iterator = 0
        while True:
            s1_v = self.s1.read()
            s2_v = self.s2.read()
            s3_v = self.s3.read()
            joy_v = self.joy_press.read()
            if not s1_v:
                move_n *= -1
            if not s2_v:
                new_pos = pen.ycor() + move_n
                pen.sety(new_pos)
            if not s3_v:
                new_pos = pen.xcor() + move_n
                pen.setx(new_pos)
            if not joy_v:
                iterator += 1
                if iterator % 2 == 0:
                    pen.up()
                else:
                    pen.down()
            print('default: {}| ({} ; {})| <-> {}| ^ {} | i : {}'
                  .format(move_n, pen.xcor(), pen.ycor(), s3_v, s2_v, iterator))
            time.sleep(0.1)


def analog_state(analog_input):
    if analog_input.read():
        return 'UP'
    else:
        return 'DOWN'


if __name__ == '__main__':
    board = Arduino('/dev/ttyACM0')
    my_shield = RemoteShield(
        board.get_pin('a:0:i'),
        board.get_pin('a:1:i'),
        board.get_pin('a:2:i'),
        board.get_pin('a:3:i'),
        board.get_pin('d:7:i'),
        board.get_pin('d:4:i'),
        board.get_pin('d:3:i'),
        board.get_pin('d:2:i')
    )

    print('(x; y)')
    print('TRUE --> NOT pressed\nFALSE --> pressed')
    # my_shield.remote_shield()
    # my_shield.drawing()
    my_shield.joy_draw()
