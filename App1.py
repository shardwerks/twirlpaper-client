#!/usr/bin/env python
#Boa:App:BoaApp

# Library modules
import wx
# Project modules
import Frame1
from configops import ConfigOps

modules ={'Frame1': [1, 'Main frame of Application', u'Frame1.py']}

class BoaApp(wx.App):

    def OnInit(self):
        self.config = ConfigOps()
        self.main = Frame1.create(None, self.config, 'd:\\')
        self.main.Show()
        self.SetTopWindow(self.main)
        return True


def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
