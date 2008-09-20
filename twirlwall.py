#!/usr/bin/env python
#Boa:App:BoaApp

# Library modules
import wx
#import os
#import sys
# Project modules
import frameops
import taskbarops
from configops import ConfigOps
from timerops import TimerOps

modules ={'frameops': [1, 'Main frame of Application', 'frameops.py']}

class BoaApp(wx.App):

    def OnInit(self):
        # Get executable's path
        #twirlpath = os.path.dirname(unicode(sys.executable,
        #	sys.getfilesystemencoding( )))
        twirlpath = 'd:\\'

        # Start config
        config = ConfigOps()
        config.Load(twirlpath)

        # Start timer
        self.timethread = TimerOps(config, twirlpath)
        self.timethread.start()

        # Start GUI
        self.frameops = frameops.create(None, config, twirlpath)
        self.frameops.Hide()
        self.SetTopWindow(self.frameops)
        self.taskbarops = taskbarops.TaskbarOps(self)
        return True

    def OnExit(self):
        # GUI closed, stop timer
        self.timethread.Stop()


def main():
    application = BoaApp(0)
    application.MainLoop()


if __name__ == '__main__':
    main()
