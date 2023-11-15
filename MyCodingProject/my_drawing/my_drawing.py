"""
File: my_drawing.py
Name: my_draw
----------------------
TODO: Drawing
"""

import random
from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GPolygon, GArc
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousedragged, onmousemoved
from campy.graphics.gimage import GImage
from campy.gui.events.timer import pause


SIZE = 100       # Controls the width and height of the rect
WIDTH = 800      # Controls the width of the window
HEIGHT = 800     # Controls the height of the window


def main():
    """
    Title: My favorite line sticker
    "Programming has got me feeling so world-weary.
    Time to use my favorite Line sticker – drawing the endlessly world-weary white bear
    """
    window = GWindow(width=WIDTH, height=HEIGHT, title='My_drawing')

    body = GArc(350, 360, 150, 240, x=(window.width-350)/2, y=(window.height-360)/2)
    window.add(body)
    ear_left = GArc(30, 40, 0, 270, x=233, y=248)
    window.add(ear_left)
    ear_right = GArc(30, 40, 270, 270, x=536, y=248)
    window.add(ear_right)
    body_up = GArc(271, 150, 0, 180, x=265, y=230)
    window.add(body_up)
    eye_left = GOval(35, 40, x=290, y=320)
    window.add(eye_left)
    eye_right = GOval(35, 40, x=475, y=320)
    window.add(eye_right)
    eye_left_fill = GOval(32, 25, x=291, y=320)
    eye_left_fill.filled = True
    window.add(eye_left_fill)
    eye_right_fill = GOval(32, 25, x=476, y=320)
    eye_right_fill.filled = True
    window.add(eye_right_fill)
    nose = GOval(15, 15, x=(window.width-10)/2, y=360)
    nose.filled = True
    window.add(nose)
    nose2 = GRect(5, 20, x=(window.width-1)/2, y=370)
    nose2.filled = True
    window.add(nose2)
    mouth = GRect(30, 5, x=(window.width-26)/2, y=390)
    mouth.filled = True
    window.add(mouth)
    face_left = GOval(22, 18, x=250, y=360)
    face_left.filled = True
    face_left.fill_color = 'pink'
    face_left.color = 'pink'
    window.add(face_left)
    face_right = GOval(22, 18, x=528, y=360)
    face_right.filled = True
    face_right.fill_color = 'pink'
    face_right.color = 'pink'
    window.add(face_right)


if __name__ == '__main__':
    main()
