"""Taskbar icon operations"""

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
import consts
import netops
from configops import ConfigOps


[wxID_TBMENU_NEWIMAGE, wxID_TBMENU_EXIT, wxID_TBMENU_HELP,
wxID_TBMENU_OPTIONS, wxID_TBMENU_LOGIN, wxID_TBMENU_RATE1STAR,
wxID_TBMENU_RATE2STARS, wxID_TBMENU_RATE3STARS, wxID_TBMENU_RATE4STARS,
wxID_TBMENU_RATE5STARS, wxID_TBMENU_TAG, wxID_TBMENU_FLAG,
wxID_TBMENU_SUBMITTER
] = [wx.NewId() for _init_ctrls in range(13)]

class TaskbarOps(wx.TaskBarIcon):

    def _init_ctrls(self):
        """Initialize taskbar icon controls - click response, menu"""
        wx.TaskBarIcon.__init__(self)
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarNewImage)
        self.Bind(wx.EVT_MENU, self.OnTaskBarNewImage, id=wxID_TBMENU_NEWIMAGE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarExit, id=wxID_TBMENU_EXIT)
        self.Bind(wx.EVT_MENU, self.OnTaskBarHelp, id=wxID_TBMENU_HELP)
        self.Bind(wx.EVT_MENU, self.OnTaskBarOptions, id=wxID_TBMENU_OPTIONS)
        self.Bind(wx.EVT_MENU, self.OnTaskBarLogin, id=wxID_TBMENU_LOGIN)
        self.Bind(wx.EVT_MENU, self.OnTaskBarRate1Star,\
            id=wxID_TBMENU_RATE1STAR)
        self.Bind(wx.EVT_MENU, self.OnTaskBarRate2Stars,\
            id=wxID_TBMENU_RATE2STARS)
        self.Bind(wx.EVT_MENU, self.OnTaskBarRate3Stars,\
            id=wxID_TBMENU_RATE3STARS)
        self.Bind(wx.EVT_MENU, self.OnTaskBarRate4Stars,\
            id=wxID_TBMENU_RATE4STARS)
        self.Bind(wx.EVT_MENU, self.OnTaskBarRate5Stars,\
            id=wxID_TBMENU_RATE5STARS)
        self.Bind(wx.EVT_MENU, self.OnTaskBarTag, id=wxID_TBMENU_TAG)
        self.Bind(wx.EVT_MENU, self.OnTaskBarFlag, id=wxID_TBMENU_FLAG)
        self.Bind(wx.EVT_MENU, self.OnTaskBarSubmitter,
            id=wxID_TBMENU_SUBMITTER)


    def __init__(self, parent, config, twirlpath):
        self._init_ctrls()
        self._parent = parent
        self._config = config
        self._twirlpath = twirlpath

        # Set taskbar icon and tooltip
        self.SetIcon(icons.getTwirlIcon(), "Twirlpaper\n"
            + "  Double click: new wallpaper\n"
            + "  Right click: options")


    def CreatePopupMenu(self):
        """This method is called by the base class when it needs to popup
        the menu for the default EVT_RIGHT_DOWN event.  Just create
        the menu how you want it and return it from this function,
        the base class takes care of the rest."""
        submenu = wx.Menu()
        submenu.AppendRadioItem(wxID_TBMENU_RATE1STAR, "1 Star")
        submenu.AppendRadioItem(wxID_TBMENU_RATE2STARS, "2 Stars")
        submenu.AppendRadioItem(wxID_TBMENU_RATE3STARS, "3 Stars")
        submenu.AppendRadioItem(wxID_TBMENU_RATE4STARS, "4 Stars")
        submenu.AppendRadioItem(wxID_TBMENU_RATE5STARS, "5 Stars")
        menu = wx.Menu()
        
        newimageitem = wx.MenuItem(menu, wxID_TBMENU_NEWIMAGE, "New wallpaper")
        newimageitem.SetBitmap(icons.getTwirlBitmap())
        menu.AppendItem(newimageitem)
        
        menu.AppendSubMenu(submenu, "Rate")
        
        tagitem = wx.MenuItem(menu, wxID_TBMENU_TAG, "Tag")
        tagitem.SetBitmap(icons.getTagBitmap())
        menu.AppendItem(tagitem)
        
        menu.AppendCheckItem(wxID_TBMENU_FLAG, "Flag as Inappropriate")
        
        submitteritem = wx.MenuItem(menu,\
            wxID_TBMENU_SUBMITTER, "Wallpaper Homepage")
        submitteritem.SetBitmap(icons.getLinkBitmap())
        menu.AppendItem(submitteritem)
        
        menu.AppendSeparator()
        
        loginitem = wx.MenuItem(menu, wxID_TBMENU_LOGIN, "Sign in")
        loginitem.SetBitmap(icons.getUserBitmap())
        menu.AppendItem(loginitem)
        
        optionsitem = wx.MenuItem(menu, wxID_TBMENU_OPTIONS, "Options")
        optionsitem.SetBitmap(icons.getWrenchBitmap())
        menu.AppendItem(optionsitem)
        
        helpitem = wx.MenuItem(menu, wxID_TBMENU_HELP, "Help")
        helpitem.SetBitmap(icons.getHelpBitmap())
        menu.AppendItem(helpitem)
        
        menu.AppendSeparator()
        menu.Append(wxID_TBMENU_EXIT, "Exit")

        # Show the user rating, if user has not rated the image, show
        # the image rating
        radiolist = [None, wxID_TBMENU_RATE1STAR, wxID_TBMENU_RATE2STARS,
            wxID_TBMENU_RATE3STARS, wxID_TBMENU_RATE4STARS,
            wxID_TBMENU_RATE5STARS]
        if self._config["userrating"] == 0:
            checked = radiolist[self._config["imagerating"]]
        else:
            checked = radiolist[self._config["userrating"]]
        submenu.Check(checked, True)

        # Show the flag value
        menu.Check(wxID_TBMENU_FLAG, self._config["flagimage"])

        return menu


    def OnTaskBarNewImage(self, event):
        """Initiate new image by setting next change time to 0"""
        self._config["nextchange"] = 0

    def OnTaskBarExit(self, event):
        """Destroy taskbar icon then frame"""
        self.Destroy()
        self._parent.frameops.Destroy()

    def OnTaskBarHelp(self, event):
        """Open webbrowser to taskbar help page"""
        webbrowser.open(consts.URL_HELP_TASKBAR)

    def OnTaskBarOptions(self, event):
        """Open frame to Options panel"""
        self._parent.frameops.notebookApp.SetSelection(consts.PANEL_OPTIONS)
        self._parent.frameops.OnFrameShow()

    def OnTaskBarLogin(self, event):
        """Open frame to Sign In panel"""
        self._parent.frameops.notebookApp.SetSelection(consts.PANEL_LOGIN)
        self._parent.frameops.OnFrameShow()

    def OnTaskBarRate1Star(self, event):
        """Set config data and send metadata to server"""
        self._config["userrating"] = 1
        self._config.Save(self._twirlpath)
        netops.SendMetadata({"username":self._config["username"].encode("utf-8"),
            "userid":self._config["userid"], "imageid":self._config["imageid"],
            "imagerating":1})

    def OnTaskBarRate2Stars(self, event):
        """Set config data and send metadata to server"""
        self._config["userrating"] = 2
        self._config.Save(self._twirlpath)
        netops.SendMetadata({"username":self._config["username"].encode("utf-8"),
            "userid":self._config["userid"], "imageid":self._config["imageid"],
            "imagerating":2})

    def OnTaskBarRate3Stars(self, event):
        """Set config data and send metadata to server"""
        self._config["userrating"] = 3
        self._config.Save(self._twirlpath)
        netops.SendMetadata({"username":self._config["username"].encode("utf-8"),
            "userid":self._config["userid"], "imageid":self._config["imageid"],
            "imagerating":3})

    def OnTaskBarRate4Stars(self, event):
        """Set config data and send metadata to server"""
        self._config["userrating"] = 4
        self._config.Save(self._twirlpath)
        netops.SendMetadata({"username":self._config["username"].encode("utf-8"),
            "userid":self._config["userid"], "imageid":self._config["imageid"],
            "imagerating":4})

    def OnTaskBarRate5Stars(self, event):
        """Set config data and send metadata to server"""
        self._config["userrating"] = 5
        self._config.Save(self._twirlpath)
        netops.SendMetadata({"username":self._config["username"].encode("utf-8"),
            "userid":self._config["userid"], "imageid":self._config["imageid"],
            "imagerating":5})

    def OnTaskBarTag(self, event):
        """Open frame to Rate/Tag panel"""
        self._parent.frameops.notebookApp.SetSelection(consts.PANEL_RATETAG)
        self._parent.frameops.OnFrameShow()

    def OnTaskBarFlag(self, event):
        """Toggle config data and send metadata to server"""
        self._config["flagimage"] = not self._config["flagimage"]
        self._config.Save(self._twirlpath)
        netops.SendMetadata({"username":self._config["username"].encode("utf-8"),
            "userid":self._config["userid"], "imageid":self._config["imageid"],
            "flagimage":self._config["flagimage"]})

    def OnTaskBarSubmitter(self, event):
        """Open webbrowser to image URL"""
        webbrowser.open(self._config["imageurl"])
