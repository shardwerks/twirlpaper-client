#!/usr/bin/env python
#Boa:App:BoaApp


# Library modules
import wx
from os.path import dirname
import sys
# Project modules
import icons
import frameops
import taskbarops
from timerops import TimerOps
from configops import ConfigOps

modules ={u'frameops': [1, 'Main frame of Application', 'frameops.py']}

class BoaApp(wx.App):

    def OnInit(self):

        # Throw up splash screen
        splash = wx.SplashScreen(icons.getSplashBMPBitmap(),\
            wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 3000, None, -1,\
            wx.DefaultPosition, wx.DefaultSize,\
            wx.NO_BORDER | wx.FRAME_NO_TASKBAR | wx.STAY_ON_TOP)

        # Get executable's path
        self._twirlpath = dirname(unicode(sys.executable, sys.getfilesystemencoding()))
        print 'twirlpath is ' + self._twirlpath
        #self._twirlpath = 'C:\\Documents and Settings\\New User\\Desktop\\Twirlpaper\\'

        # Start config
        self._config = ConfigOps()
        self._config.Load(self._twirlpath)

        # Start timer
        self.timethread = TimerOps(self, self._config, self._twirlpath)
        self.timethread.start()

        # Start GUI
        self.frameops = frameops.create(None, self._config, self._twirlpath)
        self.frameops.Hide()
        self.SetTopWindow(self.frameops)
        self.taskbarops =\
            taskbarops.TaskbarOps(self, self._config, self._twirlpath)
        return True

    def OnExit(self):
        # GUI closed, stop timer
        self.timethread.Stop()
        self._config.Save(self._twirlpath)


def main():

	# From http://sebsauvage.net/python/snyppets/#py2exe
	try:
		# See if a console exists
		sys.stdout.write("\n")
		sys.stdout.flush()
	except IOError:
		class dummyStream:
			''' dummyStream behaves like a stream but does nothing. '''
			def __init__(self): pass
			def write(self,data): pass
			def read(self,data): pass
			def flush(self): pass
			def close(self): pass
		# and now redirect all default streams to this dummyStream:
		sys.stdout = dummyStream()
		sys.stderr = dummyStream()
		sys.stdin = dummyStream()
		sys.__stdout__ = dummyStream()
		sys.__stderr__ = dummyStream()
		sys.__stdin__ = dummyStream()

	application = BoaApp(0)
	application.MainLoop()


if __name__ == '__main__':
    main()
