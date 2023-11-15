"""
File: bouncing_ball.py
Name: bouncing_ball
-------------------------
TODO: click mouse to let ball bouncing, if ball over the window, back to the original.
"""

import random
from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GPolygon, GArc
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousedragged, onmousemoved
from campy.graphics.gimage import GImage
from campy.gui.events.timer import pause

VX = 3
yx = 0
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
mouse_x = 10
mouse_y = 10
over_count = 0
switch = True        # Set a switch

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncing)
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball)


def bouncing(mouse):
    global VX, yx, switch, over_count
    if switch and over_count <= 3:                                    # If ball over the window 3 times stop
        switch = False
        yx = 0
        while True:
            ball.move(VX, yx)
            yx += GRAVITY
            if ball.y <= 0 or ball.y + ball.height >= window.height:   # Let ball bouncing
                yx = -yx * 0.9
            pause(DELAY)
            if ball.x > window.width:                                  # If ball over the window reassign
                over_count += 1
                window.add(ball, x=START_X, y=START_Y)
                switch = True
                break
    print(over_count)


if __name__ == "__main__":
    main()
