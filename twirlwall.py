#!/usr/bin/env python
#Boa:App:BoaApp

"""Client todos:
- About page
- Splash screen png
- Password hashing
- codec.py
- netops.py
- Possible to detect whether popup menu is open?  If so, hold image change
- Possible to set icons next to submenu?
- Convert to exe
- Installer
- License
"""

# Library modules
import wx
#import os
#import sys
# Project modules
import icons
import frameops
import taskbarops
from configops import ConfigOps
from timerops import TimerOps

modules ={'frameops': [1, 'Main frame of Application', 'frameops.py']}

class BoaApp(wx.App):

    def OnInit(self):

        # Throw up splash screen
        splash = wx.SplashScreen(icons.getSplashBMPBitmap(),\
            wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 4000, None, -1,\
            wx.DefaultPosition, wx.DefaultSize,\
            wx.SIMPLE_BORDER | wx.FRAME_NO_TASKBAR | wx.STAY_ON_TOP)

        # Get executable's path
        #twirlpath = os.path.dirname(unicode(sys.executable,
        #	sys.getfilesystemencoding( )))
        twirlpath = 'd:\\'

        # Start config
        config = ConfigOps()
        config.Load(twirlpath)

        # Start timer
        self.timethread = TimerOps(self, config, twirlpath)
        self.timethread.start()

        # Start GUI
        self.frameops = frameops.create(None, config, twirlpath)
        self.frameops.Hide()
        self.SetTopWindow(self.frameops)
        self.taskbarops = taskbarops.TaskbarOps(self, config, twirlpath)
        return True

    def OnExit(self):
        # GUI closed, stop timer
        self.timethread.Stop()


def main():
    application = BoaApp(0)
    application.MainLoop()


if __name__ == '__main__':
    main()
