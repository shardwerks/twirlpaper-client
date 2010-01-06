
"""
This is a way to save the startup time when running img2py on lots of
files...

    "   -u -i -n Cancel cancel.png icons.py",
    "-a -u -i -n Graystar graystar.png icons.py",
    "-a -u -i -n Help help.png icons.py",
    "-a -u -i -n Info info.png icons.py",
    "-a -u -i -n Link link.png icons.py",
    "-a -u -i -n OK ok.png icons.py",
    "-a -u -i -n Redflag redflag.png icons.py",
    "-a -u -i -n Star star.png icons.py",
    "-a -u -i -n Tag tag.png icons.py",
    "-a -u -i -n Twirl twirl.png icons.py",
    "-a -u -i -n User user.png icons.py",
    "-a -u -i -n Wrench wrench.png icons.py",

"""

import sys

from wx.tools import img2py


command_lines = [
    "   -u -i -n GrayOrangeStar grayorangestar.png icons.py",
    "-a -u -i -n GrayStar graystar.png icons.py",
    "-a -u -i -n Help help.png icons.py",
    "-a -u -i -n Info info.png icons.py",
    "-a -u -i -n Link link.png icons.py",
    "-a -u -i -n Twirl twirlspiral16.png icons.py",
    "-a -u -i -n User user.png icons.py",
    "-a -u -i -n Tag tag.png icons.py",
    "-a -u -i -n Wrench wrench.png icons.py",
    "-a -u -i -n YellowStar yellowstar.png icons.py",
    "-a -u -i -n YellowOrangeStar yelloworangestar.png icons.py",
    "-a -u -i -n SplashBMP twirlsplash.png icons.py",
    ]

def makeimages():
    for line in command_lines:
        args = line.split()
        img2py.main(args)


if __name__ == "__main__":
    for line in command_lines:
        args = line.split()
        img2py.main(args)

