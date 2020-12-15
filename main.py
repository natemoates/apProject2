from cmu_graphics import *

tree = Group(Polygon(100, 300, 200, 100, 300, 300, fill='green'),
             Rect(175, 300, 50, 50, fill='brown'))


def on_mouse_press(x_cor, y_cor):
    pass


cmu_graphics.loop()
