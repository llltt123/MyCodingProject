"""
File: draw_line.py
Name: draw_line
-------------------------
TODO: Click mouse and create 1st circle and second circle to print a line, then remove the circle.
"""

import random
from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousedragged, onmousemoved
from campy.graphics.gimage import GImage
from campy.gui.events.timer import pause

SIZE = 10           # Controls the width and height of the rect
WIDTH = 800         # Controls the width of the window
HEIGHT = 500        # Controls the height of the window
line_x = 0          # The start point of line x
line_y = 0          # The start point of line y
line_x2 = 0         # The end point of line x
line_y2 = 0         # The end point of line y
click_count = 0     # The click_count of mouse
hole_object = 0     # The first circle x and y
hole_object2 = 0    # The second circle x and y
window = GWindow()


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global click_count                                                  # 裡面會執行
    global line_x
    global line_y
    global line_x2
    global line_y2
    global hole_object
    global hole_object2
    if click_count % 2 != 0:                                            # Judge the first click
        hole = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        hole.color = 'black'
        window.add(hole)
        hole_object = window.get_object_at(mouse.x, mouse.y)            # Get the first circle object
        line_x = mouse.x
        line_y = mouse.y
    if click_count % 2 == 0:                                            # Judge the second click
        hole2 = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        hole2.color = 'black'
        window.add(hole2)
        hole_object2 = window.get_object_at(mouse.x, mouse.y)           # Get the second circle object
        line_x2 = mouse.x
        line_y2 = mouse.y
    click_count += 1
    if click_count >= 2 and click_count % 2 == 0:                       # If we click twice, then draw a line
        pen = GLine(line_x, line_y, line_x2, line_y2)                   # then remove the circle
        pen.color = 'black'
        window.add(pen)
        window.remove(hole_object)
        window.remove(hole_object2)


if __name__ == "__main__":
    main()
