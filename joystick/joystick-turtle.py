from pyfirmata import util, Arduino
import turtle
import time

from utils import analog_state

MIDDLE = 0.5


class MyTurtle:
    """
    MyTurtle class
    """

    def __init__(self, x_axis, y_axis, joy_press, s1, s2, s3):
        """
        :param x_axis:
        :param y_axis:
        :param joy_press:
        :param s1:
        :param s2:
        :param s3:
        """
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.joy_press = joy_press
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.btn_counter = 0
        self.btn_state = 0
        self.btn_prev_state = 0

    def joy_draw(self):
        it = util.Iterator(board)
        it.start()
        pen = turtle.Turtle()
        pen.home()
        pen_l = 1

        while True:
            x = round(self.x_axis.read(), 1)
            y = round(self.y_axis.read(), 1)
            self.btn_state = self.joy_press.read()

            if x > MIDDLE:
                new_pos = pen.xcor() + pen_l
                pen.setx(new_pos)
            elif x < MIDDLE:
                new_pos = pen.xcor() - pen_l
                pen.setx(new_pos)

            if y < MIDDLE:
                new_pos = pen.ycor() + pen_l
                pen.sety(new_pos)
            elif y > MIDDLE:
                new_pos = pen.ycor() - pen_l
                pen.sety(new_pos)

            # detect the state of pressure of the JoyStick
            if self.btn_state != self.btn_prev_state:
                if analog_state(self.btn_state) == 'UP':
                    self.btn_counter += 1
                    print('Btn UP --> HIGH\nNumber of button pushes: ', self.btn_counter)
                else:
                    print('Btn DOWN --> LOW')

                time.sleep(0.05)

            # save the current state as the last state, for next time through the loop
            self.btn_prev_state = self.btn_state

            if self.btn_counter % 2 == 0:
                pen.down()
            else:
                pen.up()
            print(x, '  ', y)
            time.sleep(0.001)


if __name__ == '__main__':
    board = Arduino('/dev/ttyACM0')
    my_shield = MyTurtle(
        board.get_pin('a:2:i'),
        board.get_pin('a:3:i'),
        board.get_pin('d:7:i'),
        board.get_pin('d:4:i'),
        board.get_pin('d:3:i'),
        board.get_pin('d:2:i')
    )

    print('(x; y)')
    print('TRUE --> NOT pressed\nFALSE --> pressed')
    my_shield.joy_draw()
    #TODO read the value of the switch on led 7: it is not an analog value
