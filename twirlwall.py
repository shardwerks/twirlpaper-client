"""Display an image as a desktop wallpaper"""


__author__		= "Shultz Wang"
__version__		= "Revision 0.1"
__date__		= "Tuesday, August 07, 2007 22:59:05"
__copyright__	= "Copyright (c) 2007 Shultz Wang"


# Library modules
#import os
#import sys
import wx
# Project modules
from configops import ConfigOps
from timerops import TimerOps

#23456789012345678901234567890123456789012345678901234567890123456789012345678
#TODOs:
# netops
# guiops
# switch displayops to use wx.Image so as to not have to include PIL in package: YAGNI?

# The problem I'm having with transferring the config object back and forth when
# calling the wxPython frames is that the config object is stateful.  If it's not
# holding state, then there wouldn't be a need to instantiate it.  If it's not
# stateful though, aren't I going back to non-OO methods?  Or is this closer to
# functional programming?
# This is going to be a problem with other modules as well, the timerops thread is
# holding state because its time count *IS* its state.

# Get executable's path - for when program is converted to exe by py2exe
#exepath=os.path.dirname(unicode(sys.executable,
#	sys.getfilesystemencoding( )))
exepath = 'd:\\'

wxapp = wx.PySimpleApp()

config = ConfigOps()
#config.Load(exepath)
config["waitperiod"]=180

timethread = TimerOps(config, exepath)
timethread.start()

guithread = GUIOps(threadtime, wxapp)
guithread.start()

