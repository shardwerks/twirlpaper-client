#-----------------------------------------------------------------------------
# Name:        Frame1.py
# Purpose:     
#
# Author:      Shultz Wang
#
# Created:     2007/08/12
# RCS-ID:      $Id: Frame1.py $
# Copyright:   (c) 2007
# Licence:     <your licence>
#-----------------------------------------------------------------------------
#Boa:Frame:Frame


# Library modules
import wx
import webbrowser
# Project modules
import netops
import twirlconst
from configops import ConfigOps


def create(parent, config, tpath):
    return Frame(parent, config, tpath)

[wxID_FRAME, wxID_FRAMEBUTTONABOUTCANCEL, wxID_FRAMEBUTTONABOUTHELP, 
 wxID_FRAMEBUTTONABOUTOK, wxID_FRAMEBUTTONLOGINCANCEL, 
 wxID_FRAMEBUTTONLOGINHELP, wxID_FRAMEBUTTONLOGINOK, 
 wxID_FRAMEBUTTONOPTIONSCANCEL, wxID_FRAMEBUTTONOPTIONSHELP, 
 wxID_FRAMEBUTTONOPTIONSOK, wxID_FRAMEBUTTONRATECANCEL, 
 wxID_FRAMEBUTTONRATEHELP, wxID_FRAMEBUTTONRATEOK, wxID_FRAMEBUTTONSIGNIN, 
 wxID_FRAMECHECKBOXLOGINREMEMBER, wxID_FRAMECHOICEOPTIONCHANGEEVERY, 
 wxID_FRAMECHOICEOPTIONPERCENTUNRATED, wxID_FRAMECHOICEOPTIONRATEDATLEAST, 
 wxID_FRAMENOTEBOOKAPP, wxID_FRAMEPANELABOUT, wxID_FRAMEPANELLOGIN, 
 wxID_FRAMEPANELOPTIONS, wxID_FRAMEPANELRATE, wxID_FRAMESTATICBOXABOUT, 
 wxID_FRAMESTATICBOXLOGIN, wxID_FRAMESTATICBOXOPTIONS, 
 wxID_FRAMESTATICBOXRATE, wxID_FRAMESTATICBOXTAG, 
 wxID_FRAMESTATICTEXTCHANGEEVERY, wxID_FRAMESTATICTEXTLOGIN, 
 wxID_FRAMESTATICTEXTPASSWORD, wxID_FRAMESTATICTEXTPERCENTUNRATED, 
 wxID_FRAMESTATICTEXTRATEDATLEAST, wxID_FRAMESTATICTEXTSIGNEDIN, 
 wxID_FRAMESTATICTEXTSUBSCRIBEDTAGS, wxID_FRAMESTATICTEXTTAGS, 
 wxID_FRAMETEXTCTRLIMAGETAGS, wxID_FRAMETEXTCTRLLOGIN, 
 wxID_FRAMETEXTCTRLPASSWORD, wxID_FRAMETEXTCTRLSUBSCRIBEDTAGS, 
 wxID_FRAMETOGGLEBUTTONRATEFLAG, 
] = [wx.NewId() for _init_ctrls in range(41)]

class Frame(wx.Frame):

    def _init_coll_notebookApp_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panelRate, select=False,
              text='Rate')
        parent.AddPage(imageId=-1, page=self.panelLogin, select=False,
              text='Sign In')
        parent.AddPage(imageId=-1, page=self.panelOptions, select=False,
              text='Options')
        parent.AddPage(imageId=-1, page=self.panelAbout, select=True,
              text='About')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME, name='Frame', parent=prnt,
              pos=wx.Point(324, 243), size=wx.Size(344, 349),
              style=wx.DEFAULT_FRAME_STYLE, title='Twirli')
        self.SetClientSize(wx.Size(336, 322))

        self.notebookApp = wx.Notebook(id=wxID_FRAMENOTEBOOKAPP,
              name='notebookApp', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(336, 322), style=0)

        self.panelRate = wx.Panel(id=wxID_FRAMEPANELRATE, name='panelRate',
              parent=self.notebookApp, pos=wx.Point(0, 0), size=wx.Size(328,
              296), style=wx.TAB_TRAVERSAL)

        self.panelLogin = wx.Panel(id=wxID_FRAMEPANELLOGIN, name='panelLogin',
              parent=self.notebookApp, pos=wx.Point(0, 0), size=wx.Size(328,
              296), style=wx.TAB_TRAVERSAL)

        self.panelOptions = wx.Panel(id=wxID_FRAMEPANELOPTIONS,
              name='panelOptions', parent=self.notebookApp, pos=wx.Point(0, 0),
              size=wx.Size(328, 296), style=wx.TAB_TRAVERSAL)

        self.textCtrlImageTags = wx.TextCtrl(id=wxID_FRAMETEXTCTRLIMAGETAGS,
              name='textCtrlImageTags', parent=self.panelRate, pos=wx.Point(104,
              128), size=wx.Size(200, 48),
              style=wx.TE_MULTILINE | wx.TE_READONLY, value='')

        self.staticTextTags = wx.StaticText(id=wxID_FRAMESTATICTEXTTAGS,
              label='Image Tags:', name='staticTextTags', parent=self.panelRate,
              pos=wx.Point(16, 144), size=wx.Size(60, 13), style=0)

        self.textCtrlSubscribedTags = wx.TextCtrl(id=wxID_FRAMETEXTCTRLSUBSCRIBEDTAGS,
              name='textCtrlSubscribedTags', parent=self.panelRate,
              pos=wx.Point(104, 184), size=wx.Size(200, 48),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlSubscribedTags.Bind(wx.EVT_TEXT,
              self.OnTextCtrlSubscribedTagsText,
              id=wxID_FRAMETEXTCTRLSUBSCRIBEDTAGS)

        self.buttonRateOK = wx.Button(id=wxID_FRAMEBUTTONRATEOK, label='OK',
              name='buttonRateOK', parent=self.panelRate, pos=wx.Point(24, 264),
              size=wx.Size(75, 23), style=0)
        self.buttonRateOK.Bind(wx.EVT_BUTTON, self.OnButtonRateOKButton,
              id=wxID_FRAMEBUTTONRATEOK)

        self.buttonRateCancel = wx.Button(id=wxID_FRAMEBUTTONRATECANCEL,
              label='Cancel', name='buttonRateCancel', parent=self.panelRate,
              pos=wx.Point(128, 264), size=wx.Size(75, 23), style=0)
        self.buttonRateCancel.Bind(wx.EVT_BUTTON, self.OnButtonRateCancelButton,
              id=wxID_FRAMEBUTTONRATECANCEL)

        self.staticTextSubscribedTags = wx.StaticText(id=wxID_FRAMESTATICTEXTSUBSCRIBEDTAGS,
              label='Subscribed Tags:', name='staticTextSubscribedTags',
              parent=self.panelRate, pos=wx.Point(16, 200), size=wx.Size(82,
              13), style=0)

        self.staticTextLogin = wx.StaticText(id=wxID_FRAMESTATICTEXTLOGIN,
              label='Username:', name='staticTextLogin', parent=self.panelLogin,
              pos=wx.Point(48, 40), size=wx.Size(52, 13), style=0)
        self.staticTextLogin.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'MS Shell Dlg 2'))

        self.staticTextPassword = wx.StaticText(id=wxID_FRAMESTATICTEXTPASSWORD,
              label=' Password:', name='staticTextPassword',
              parent=self.panelLogin, pos=wx.Point(48, 72), size=wx.Size(53,
              13), style=0)

        self.textCtrlLogin = wx.TextCtrl(id=wxID_FRAMETEXTCTRLLOGIN,
              name='textCtrlLogin', parent=self.panelLogin, pos=wx.Point(128,
              40), size=wx.Size(168, 21), style=0, value='Guest')
        self.textCtrlLogin.Bind(wx.EVT_TEXT, self.OnTextCtrlLoginText,
              id=wxID_FRAMETEXTCTRLLOGIN)

        self.checkBoxLoginRemember = wx.CheckBox(id=wxID_FRAMECHECKBOXLOGINREMEMBER,
              label='Remember me on this computer',
              name='checkBoxLoginRemember', parent=self.panelLogin,
              pos=wx.Point(128, 152), size=wx.Size(176, 13), style=0)
        self.checkBoxLoginRemember.SetValue(False)
        self.checkBoxLoginRemember.Bind(wx.EVT_CHECKBOX,
              self.OnCheckBoxLoginRememberCheckbox,
              id=wxID_FRAMECHECKBOXLOGINREMEMBER)

        self.buttonRateHelp = wx.Button(id=wxID_FRAMEBUTTONRATEHELP,
              label='Help', name='buttonRateHelp', parent=self.panelRate,
              pos=wx.Point(232, 264), size=wx.Size(75, 23), style=0)
        self.buttonRateHelp.Bind(wx.EVT_BUTTON, self.OnButtonRateHelpButton,
              id=wxID_FRAMEBUTTONRATEHELP)

        self.buttonLoginOK = wx.Button(id=wxID_FRAMEBUTTONLOGINOK, label='OK',
              name='buttonLoginOK', parent=self.panelLogin, pos=wx.Point(24,
              264), size=wx.Size(75, 23), style=0)
        self.buttonLoginOK.Bind(wx.EVT_BUTTON, self.OnButtonLoginOKButton,
              id=wxID_FRAMEBUTTONLOGINOK)

        self.buttonLoginCancel = wx.Button(id=wxID_FRAMEBUTTONLOGINCANCEL,
              label='Cancel', name='buttonLoginCancel', parent=self.panelLogin,
              pos=wx.Point(128, 264), size=wx.Size(75, 23), style=0)
        self.buttonLoginCancel.Bind(wx.EVT_BUTTON,
              self.OnButtonLoginCancelButton, id=wxID_FRAMEBUTTONLOGINCANCEL)

        self.buttonLoginHelp = wx.Button(id=wxID_FRAMEBUTTONLOGINHELP,
              label='Help', name='buttonLoginHelp', parent=self.panelLogin,
              pos=wx.Point(232, 264), size=wx.Size(75, 23), style=0)
        self.buttonLoginHelp.Bind(wx.EVT_BUTTON, self.OnButtonLoginHelpButton,
              id=wxID_FRAMEBUTTONLOGINHELP)

        self.buttonOptionsOK = wx.Button(id=wxID_FRAMEBUTTONOPTIONSOK,
              label='OK', name='buttonOptionsOK', parent=self.panelOptions,
              pos=wx.Point(24, 264), size=wx.Size(75, 23), style=0)
        self.buttonOptionsOK.Bind(wx.EVT_BUTTON, self.OnButtonOptionsOKButton,
              id=wxID_FRAMEBUTTONOPTIONSOK)

        self.buttonOptionsCancel = wx.Button(id=wxID_FRAMEBUTTONOPTIONSCANCEL,
              label='Cancel', name='buttonOptionsCancel',
              parent=self.panelOptions, pos=wx.Point(128, 264), size=wx.Size(75,
              23), style=0)
        self.buttonOptionsCancel.Bind(wx.EVT_BUTTON,
              self.OnButtonOptionsCancelButton,
              id=wxID_FRAMEBUTTONOPTIONSCANCEL)

        self.buttonOptionsHelp = wx.Button(id=wxID_FRAMEBUTTONOPTIONSHELP,
              label='Help', name='buttonOptionsHelp', parent=self.panelOptions,
              pos=wx.Point(232, 264), size=wx.Size(75, 23), style=0)
        self.buttonOptionsHelp.Bind(wx.EVT_BUTTON,
              self.OnButtonOptionsHelpButton, id=wxID_FRAMEBUTTONOPTIONSHELP)

        self.choiceOptionRatedAtLeast = wx.Choice(choices=["1 Star", "2 Stars",
              "3 Stars", "4 Stars", "5 Stars"],
              id=wxID_FRAMECHOICEOPTIONRATEDATLEAST,
              name='choiceOptionRatedAtLeast', parent=self.panelOptions,
              pos=wx.Point(200, 40), size=wx.Size(80, 21), style=0)
        self.choiceOptionRatedAtLeast.SetStringSelection('')
        self.choiceOptionRatedAtLeast.SetSelection(0)
        self.choiceOptionRatedAtLeast.Bind(wx.EVT_CHOICE,
              self.OnChoiceOptionRatedAtLeastChoice,
              id=wxID_FRAMECHOICEOPTIONRATEDATLEAST)

        self.staticTextRatedAtLeast = wx.StaticText(id=wxID_FRAMESTATICTEXTRATEDATLEAST,
              label='Display images rated at least:',
              name='staticTextRatedAtLeast', parent=self.panelOptions,
              pos=wx.Point(40, 40), size=wx.Size(142, 13), style=0)

        self.staticTextPercentUnrated = wx.StaticText(id=wxID_FRAMESTATICTEXTPERCENTUNRATED,
              label=' Percentage of unrated images:',
              name='staticTextPercentUnrated', parent=self.panelOptions,
              pos=wx.Point(32, 72), size=wx.Size(152, 13), style=0)

        self.choiceOptionPercentUnrated = wx.Choice(choices=["5%", "10%", "20%",
              "50%", "75%", "100%"], id=wxID_FRAMECHOICEOPTIONPERCENTUNRATED,
              name='choiceOptionPercentUnrated', parent=self.panelOptions,
              pos=wx.Point(200, 72), size=wx.Size(80, 21), style=0)
        self.choiceOptionPercentUnrated.SetSelection(2)
        self.choiceOptionPercentUnrated.Bind(wx.EVT_CHOICE,
              self.OnChoiceOptionPercentUnratedChoice,
              id=wxID_FRAMECHOICEOPTIONPERCENTUNRATED)

        self.staticTextChangeEvery = wx.StaticText(id=wxID_FRAMESTATICTEXTCHANGEEVERY,
              label='Change image every:', name='staticTextChangeEvery',
              parent=self.panelOptions, pos=wx.Point(80, 104), size=wx.Size(103,
              13), style=0)

        self.choiceOptionChangeEvery = wx.Choice(choices=["15 minutes",
              "30 minutes", "1 hour", "2 hours", "4 hours", "8 hours", "1 day",
              "2 days", "4 days", "1 week"],
              id=wxID_FRAMECHOICEOPTIONCHANGEEVERY,
              name='choiceOptionChangeEvery', parent=self.panelOptions,
              pos=wx.Point(200, 104), size=wx.Size(80, 21), style=0)
        self.choiceOptionChangeEvery.SetStringSelection('')
        self.choiceOptionChangeEvery.SetSelection(3)
        self.choiceOptionChangeEvery.Bind(wx.EVT_CHOICE,
              self.OnChoiceOptionChangeEveryChoice,
              id=wxID_FRAMECHOICEOPTIONCHANGEEVERY)

        self.toggleButtonRateFlag = wx.ToggleButton(id=wxID_FRAMETOGGLEBUTTONRATEFLAG,
              label='Flag As Inappropriate', name='toggleButtonRateFlag',
              parent=self.panelRate, pos=wx.Point(152, 64), size=wx.Size(152,
              23), style=0)
        self.toggleButtonRateFlag.SetValue(False)
        self.toggleButtonRateFlag.Bind(wx.EVT_TOGGLEBUTTON,
              self.OnToggleButtonRateFlagTogglebutton,
              id=wxID_FRAMETOGGLEBUTTONRATEFLAG)

        self.textCtrlPassword = wx.TextCtrl(id=wxID_FRAMETEXTCTRLPASSWORD,
              name='textCtrlPassword', parent=self.panelLogin, pos=wx.Point(128,
              72), size=wx.Size(168, 21), style=wx.TE_PASSWORD, value='')
        self.textCtrlPassword.Bind(wx.EVT_TEXT, self.OnTextCtrlPasswordText,
              id=wxID_FRAMETEXTCTRLPASSWORD)

        self.staticBoxRate = wx.StaticBox(id=wxID_FRAMESTATICBOXRATE,
              label='Rating', name='staticBoxRate', parent=self.panelRate,
              pos=wx.Point(8, 8), size=wx.Size(312, 88), style=0)

        self.staticBoxTag = wx.StaticBox(id=wxID_FRAMESTATICBOXTAG,
              label='Tags', name='staticBoxTag', parent=self.panelRate,
              pos=wx.Point(8, 104), size=wx.Size(312, 144), style=0)

        self.panelAbout = wx.Panel(id=wxID_FRAMEPANELABOUT, name='panelAbout',
              parent=self.notebookApp, pos=wx.Point(0, 0), size=wx.Size(328,
              296), style=wx.TAB_TRAVERSAL)

        self.buttonAboutOK = wx.Button(id=wxID_FRAMEBUTTONABOUTOK, label='OK',
              name='buttonAboutOK', parent=self.panelAbout, pos=wx.Point(24,
              264), size=wx.Size(75, 23), style=0)
        self.buttonAboutOK.Bind(wx.EVT_BUTTON, self.OnButtonAboutOKButton,
              id=wxID_FRAMEBUTTONABOUTOK)

        self.staticBoxLogin = wx.StaticBox(id=wxID_FRAMESTATICBOXLOGIN,
              label='Sign In', name='staticBoxLogin', parent=self.panelLogin,
              pos=wx.Point(8, 8), size=wx.Size(312, 176), style=0)

        self.staticBoxOptions = wx.StaticBox(id=wxID_FRAMESTATICBOXOPTIONS,
              label='Display Options', name='staticBoxOptions',
              parent=self.panelOptions, pos=wx.Point(8, 8), size=wx.Size(312,
              136), style=0)

        self.buttonAboutCancel = wx.Button(id=wxID_FRAMEBUTTONABOUTCANCEL,
              label='Cancel', name='buttonAboutCancel', parent=self.panelAbout,
              pos=wx.Point(128, 264), size=wx.Size(75, 23), style=0)
        self.buttonAboutCancel.Bind(wx.EVT_BUTTON,
              self.OnButtonAboutCancelButton, id=wxID_FRAMEBUTTONABOUTCANCEL)

        self.buttonAboutHelp = wx.Button(id=wxID_FRAMEBUTTONABOUTHELP,
              label='Help', name='buttonAboutHelp', parent=self.panelAbout,
              pos=wx.Point(232, 264), size=wx.Size(75, 23), style=0)
        self.buttonAboutHelp.Bind(wx.EVT_BUTTON, self.OnButtonAboutHelpButton,
              id=wxID_FRAMEBUTTONABOUTHELP)

        self.staticBoxAbout = wx.StaticBox(id=wxID_FRAMESTATICBOXABOUT,
              label='About Twirli', name='staticBoxAbout',
              parent=self.panelAbout, pos=wx.Point(8, 8), size=wx.Size(312,
              240), style=0)

        self.buttonSignIn = wx.Button(id=wxID_FRAMEBUTTONSIGNIN,
              label='Sign In', name='buttonSignIn', parent=self.panelLogin,
              pos=wx.Point(128, 112), size=wx.Size(75, 23), style=0)
        self.buttonSignIn.Bind(wx.EVT_BUTTON, self.OnButtonSignInButton,
              id=wxID_FRAMEBUTTONSIGNIN)

        self.staticTextSignedIn = wx.StaticText(id=wxID_FRAMESTATICTEXTSIGNEDIN,
              label='You are not signed in.', name='staticTextSignedIn',
              parent=self.panelLogin, pos=wx.Point(88, 208), size=wx.Size(163,
              18), style=0)
        self.staticTextSignedIn.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL,
              wx.BOLD, False, 'MS Shell Dlg 2'))

        self._init_coll_notebookApp_Pages(self.notebookApp)

    def __init__(self, parent, config, tpath):
        self._init_ctrls(parent)
        
        # Load config data and make temporary copy, updates not passed
        # to main copy until user pressed OK so as to not cause any
        # intervening image downloads to be based on intermediate values
        self._config = config
        self._configtmp = ConfigOps()
        self._configtmp.update(config)
        
        # If login still valid, change text on Sign In page
        if self._configtmp["userid"] != "0000000000000000":
            self.staticTextSignedIn.SetLabel("    You are signed in.")

        # Set image tags
        self.textCtrlImageTags.Clear()
        self.textCtrlImageTags.WriteText(self._configtmp["imagetags"])

        self._tpath = tpath
        self._flag = False
        self._hashed = ""


    def OnToggleButtonRateFlagTogglebutton(self, event):
        self._flag = True

    def OnTextCtrlSubscribedTagsText(self, event):
        self._configtmp["subscribedtags"] = event.GetString()

    def OnButtonRateOKButton(self, event):
        self.OnButtonOKButton()

    def OnButtonRateCancelButton(self, event):
        self.Close()

    def OnButtonRateHelpButton(self, event):
        try:
            #*** update when real url available
            webbrowser.open("http://www.google.com/search?as_q=rate")
        except:
            #*** where should no-browser-exception be passed?
            pass

    def OnTextCtrlLoginText(self, event):
        self._configtmp["login"] = event.GetString()

    def OnTextCtrlPasswordText(self, event):
        #***encode password and store it as a hashed value
        #***self._hashed = encoded....
        self._hashed = event.GetString()

    def OnButtonSignInButton(self, event):
        # Send login and hashed password to server, get back userid.
        # Save userid immediately to config so that any image requests
        # are associated with the correct user.
        # Update text on Sign In page based on whether userid is valid.
        self._configtmp["userid"] =\
            netops.SendLogin(self._configtmp["login"], self._hashed)
        self._config["userid"] = self._configtmp["userid"]
        if self._configtmp["userid"] != "0000000000000000":
            self.staticTextSignedIn.SetLabel("    You are signed in.")
        else:
            self.staticTextSignedIn.SetLabel("You are not signed in.")

    def OnCheckBoxLoginRememberCheckbox(self, event):
        self._configtmp["rememberme"] = event.IsChecked()

    def OnButtonLoginOKButton(self, event):
        self.OnButtonOKButton()

    def OnButtonLoginCancelButton(self, event):
        self.Close()

    def OnButtonLoginHelpButton(self, event):
        try:
            #*** update when real url available
            webbrowser.open("http://www.google.com/search?as_q=login")
        except:
            #*** where should no-browser-exception be passed?
            pass

    def OnChoiceOptionRatedAtLeastChoice(self, event):
        _ratedict = {"1 Star":1, "2 Stars":2, "3 Stars":3,
            "4 Stars":4, "5 Stars":5}
        self._configtmp["ratedatleast"] = _ratedict[event.GetString()]

    def OnChoiceOptionPercentUnratedChoice(self, event):
        _percentdict = {"5%":5, "10%":10, "20%":20, "50%":50,
            "75%":75, "100%":100}
        self._configtmp["percentnew"] = _percentdict[event.GetString()]

    def OnChoiceOptionChangeEveryChoice(self, event):
        _changedict = {"15 minutes":900, "30 minutes":1800, "1 hour":3600,
            "2 hours":7200, "4 hours":14400, "8 hours":28800, "1 day":86400,
            "2 days":172800, "4 days":345600, "1 week":604800}

        # Update change time to last change time plus new changeevery so
        # that program does not wait until last changeevery time is up before
        # changing again, which is strange if last changeevery is longer.
        # E.g. Don't make user wait out the rest of the week if he changed
        # his changeevery to an hour.
        self._configtmp["nextchangetime"] = self._configtmp["nextchangetime"]\
            - self._configtmp["changeevery"] + _changedict[event.GetString()]
        self._configtmp["changeevery"] = _changedict[event.GetString()]

    def OnButtonOptionsOKButton(self, event):
        self.OnButtonOKButton()

    def OnButtonOptionsCancelButton(self, event):
        self.Close()

    def OnButtonOptionsHelpButton(self, event):
        try:
            #*** update when real url available
            webbrowser.open("http://www.google.com/search?as_q=options")
        except:
            #*** where should no-browser-exception be passed?
            pass

    def OnButtonAboutOKButton(self, event):
        self.OnButtonOKButton()

    def OnButtonAboutCancelButton(self, event):
        self.Close()

    def OnButtonAboutHelpButton(self, event):
        try:
            #*** update when real url available
            webbrowser.open("http://www.google.com/search?as_q=about")
        except:
            #*** where should no-browser-exception be passed?
            pass

    def OnButtonOKButton(self):
        self._config.update(self._configtmp)
        netops.SendMetaData(twirlconst.FRAMEOK)
        
        #*** should send flag and imageid and userid
        if self._flag: netops.SendMetaData(FLAG)
        self._config.Save(self._tpath)
        print self._config
        self.Close()


if __name__ == '__main__':
    config = ConfigOps()
    app = wx.PySimpleApp()
    frame = create(None, config)
    frame.Show()

    app.MainLoop()
