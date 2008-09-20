#-----------------------------------------------------------------------------
# Name:        taskbarops.py
# Purpose:     
#
# Author:      Shultz Wang
#
# Created:     2007/08/17
# RCS-ID:      $Id: taskbarops.py $
# Copyright:   (c) 2007
# Licence:     <your licence>
#-----------------------------------------------------------------------------


# Library modules
import wx
import webbrowser
# Project modules
import icons
import netops
import twirlconst
from configops import ConfigOps

def create(parent, config, twirlpath):
    return TaskbarOps(parent, config, twirlpath)

[wxID_TBMENU_NEWIMAGE, wxID_TBMENU_EXIT, wxID_TBMENU_HELP,
wxID_TBMENU_OPTIONS, wxID_TBMENU_LOGIN, wxID_TBMENU_RATE,
wxID_TBMENU_TAG, wxID_TBMENU_FLAG, wxID_TBMENU_SUBMITTER
] = [wx.NewId() for _init_ctrls in range(9)]

class TaskbarOps(wx.TaskBarIcon):

    def _init_ctrls(self):
        wx.TaskBarIcon.__init__(self)
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarActivate)
        self.Bind(wx.EVT_TASKBAR_LEFT_UP, self.OnTaskBarNewImage)
        self.Bind(wx.EVT_MENU, self.OnTaskBarNewImage, id=wxID_TBMENU_NEWIMAGE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarExit, id=wxID_TBMENU_EXIT)
        self.Bind(wx.EVT_MENU, self.OnTaskBarHelp, id=wxID_TBMENU_HELP)
        self.Bind(wx.EVT_MENU, self.OnTaskBarOptions, id=wxID_TBMENU_OPTIONS)
        self.Bind(wx.EVT_MENU, self.OnTaskBarLogin, id=wxID_TBMENU_LOGIN)
        self.Bind(wx.EVT_MENU, self.OnTaskBarRate, id=wxID_TBMENU_RATE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarTag, id=wxID_TBMENU_TAG)
        self.Bind(wx.EVT_MENU, self.OnTaskBarFlag, id=wxID_TBMENU_FLAG)
        self.Bind(wx.EVT_MENU, self.OnTaskBarSubmitter,
            id=wxID_TBMENU_SUBMITTER)

    def __init__(self, parent):
        self._init_ctrls()
        self._parent = parent

        # Set taskbar icon and tooltip
        self.SetIcon(icons.getTwirliIcon(), "Twirli Wallpaper Changer")


    def CreatePopupMenu(self):
        """This method is called by the base class when it needs to popup
        the menu for the default EVT_RIGHT_DOWN event.  Just create
        the menu how you want it and return it from this function,
        the base class takes care of the rest."""
        menu = wx.Menu()
        menu.Append(wxID_TBMENU_EXIT, "Exit")
        menu.AppendSeparator()
        menu.Append(wxID_TBMENU_HELP, "Help")
        menu.Append(wxID_TBMENU_OPTIONS, "Options")
        menu.Append(wxID_TBMENU_LOGIN, "Sign in")
        menu.AppendSeparator()
        menu.Append(wxID_TBMENU_TAG, "Tag")
        menu.Append(wxID_TBMENU_FLAG, "Flag as Inappropriate")
        menu.Append(wxID_TBMENU_SUBMITTER, "Wallpaper Homepage")
        menu.Append(wxID_TBMENU_RATE, "Rate")
        menu.Append(wxID_TBMENU_NEWIMAGE, "New wallpaper")
        return menu

    def OnTaskBarActivate(self, event):
        # Show frame if hidden
        if self._parent.frameops.IsShown() != True:
            self._parent.frameops.Show()
            self._parent.frameops.Raise()


    def OnTaskBarNewImage(self, event):
        #***get new image through netops
        netops.SendMetaData(2)

    def OnTaskBarExit(self, event):
        #***get new image through netops
        self.Destroy()
        self._parent.frameops.Destroy()

    def OnTaskBarHelp(self, event):
        #***replace with real op
        webbrowser.open("http://www.google.com/search?as_q=taskbar")

    def OnTaskBarOptions(self, event):
        self._parent.frameops.notebookApp.ChangeSelection(
            self._parent.frameops.panelAbout)
        self._parent.frameops.Show()
        self._parent.frameops.Raise()

    def OnTaskBarLogin(self, event):
        self._parent.frameops.notebookApp.ChangeSelection(
            self._parent.frameops.panelLogin)
        self._parent.frameops.Show()
        self._parent.frameops.Raise()

    def OnTaskBarRate(self, event):
        #***replace with real op
        netops.SendMetaData(7)

    def OnTaskBarTag(self, event):
        self._parent.frameops.notebookApp.ChangeSelection(
            self._parent.frameops.panelRate)
        self._parent.frameops.Show()
        self._parent.frameops.Raise()

    def OnTaskBarFlag(self, event):
        #***replace with real op
        netops.SendMetaData(6)

    def OnTaskBarSubmitter(self, event):
        #***replace with real op
        webbrowser.open("http://www.google.com/search?as_q=homepage")
