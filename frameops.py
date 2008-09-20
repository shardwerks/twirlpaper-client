"""Frame operations"""

#-----------------------------------------------------------------------------
# Name:        frameops.py
# Purpose:     
#
# Author:      Shultz Wang
#
# Created:     2007/08/12
# RCS-ID:      $Id: frameops.py $
# Copyright:   (c) 2007
# Licence:     <your licence>
#-----------------------------------------------------------------------------
#Boa:Frame:FrameOps


# Library modules
import wx
import webbrowser
# Project modules
import icons
import consts
import netops
from configops import ConfigOps


def create(parent, config, twirlpath):
    return FrameOps(parent, config, twirlpath)

[wxID_FRAMEOPS, wxID_FRAMEOPSBITMAPBUTTON1STAR, 
 wxID_FRAMEOPSBITMAPBUTTON2STAR, wxID_FRAMEOPSBITMAPBUTTON3STAR, 
 wxID_FRAMEOPSBITMAPBUTTON4STAR, wxID_FRAMEOPSBITMAPBUTTON5STAR, 
 wxID_FRAMEOPSBUTTONABOUTCANCEL, wxID_FRAMEOPSBUTTONABOUTHELP, 
 wxID_FRAMEOPSBUTTONABOUTOK, wxID_FRAMEOPSBUTTONLOGINCANCEL, 
 wxID_FRAMEOPSBUTTONLOGINHELP, wxID_FRAMEOPSBUTTONLOGINOK, 
 wxID_FRAMEOPSBUTTONNEWIMAGE, wxID_FRAMEOPSBUTTONOPTIONSCANCEL, 
 wxID_FRAMEOPSBUTTONOPTIONSHELP, wxID_FRAMEOPSBUTTONOPTIONSOK, 
 wxID_FRAMEOPSBUTTONRATECANCEL, wxID_FRAMEOPSBUTTONRATEHELP, 
 wxID_FRAMEOPSBUTTONRATEOK, wxID_FRAMEOPSBUTTONSIGNIN, 
 wxID_FRAMEOPSBUTTONSUBMITTERPAGE, wxID_FRAMEOPSCHECKBOXLOGINREMEMBER, 
 wxID_FRAMEOPSCHOICEOPTIONCHANGEEVERY, 
 wxID_FRAMEOPSCHOICEOPTIONPERCENTUNRATED, 
 wxID_FRAMEOPSCHOICEOPTIONRATEDATLEAST, wxID_FRAMEOPSNOTEBOOKAPP, 
 wxID_FRAMEOPSPANELABOUT, wxID_FRAMEOPSPANELLOGIN, 
 wxID_FRAMEOPSPANELOPTIONS, wxID_FRAMEOPSPANELRATE, 
 wxID_FRAMEOPSSTATICBOXABOUT, wxID_FRAMEOPSSTATICBOXLOGIN, 
 wxID_FRAMEOPSSTATICBOXOPTIONS, wxID_FRAMEOPSSTATICBOXRATE, 
 wxID_FRAMEOPSSTATICBOXTAG, wxID_FRAMEOPSSTATICTEXTCHANGEEVERY, 
 wxID_FRAMEOPSSTATICTEXTLOGIN, wxID_FRAMEOPSSTATICTEXTPASSWORD, 
 wxID_FRAMEOPSSTATICTEXTPERCENTUNRATED, 
 wxID_FRAMEOPSSTATICTEXTRATEDATLEAST, wxID_FRAMEOPSSTATICTEXTSIGNEDIN, 
 wxID_FRAMEOPSSTATICTEXTSUBSCRIBEDTAGS, wxID_FRAMEOPSSTATICTEXTTAGS, 
 wxID_FRAMEOPSTEXTCTRLIMAGEINFO, wxID_FRAMEOPSTEXTCTRLIMAGETAGS, 
 wxID_FRAMEOPSTEXTCTRLLOGIN, wxID_FRAMEOPSTEXTCTRLPASSWORD, 
 wxID_FRAMEOPSTEXTCTRLSUBSCRIBEDTAGS, wxID_FRAMEOPSTOGGLEBUTTONRATEFLAG, 
] = [wx.NewId() for _init_ctrls in range(49)]

class FrameOps(wx.Frame):

    def _init_coll_notebookApp_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panelRate, select=True,
              text='Rate')
        parent.AddPage(imageId=-1, page=self.panelLogin, select=False,
              text='Sign In')
        parent.AddPage(imageId=-1, page=self.panelOptions, select=False,
              text='Options')
        parent.AddPage(imageId=-1, page=self.panelAbout, select=False,
              text='About')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEOPS, name='FrameOps',
              parent=prnt, pos=wx.Point(331, 208), size=wx.Size(344, 429),
              style=wx.DEFAULT_FRAME_STYLE, title='Twirli')
        self.SetClientSize(wx.Size(336, 402))

        self.notebookApp = wx.Notebook(id=wxID_FRAMEOPSNOTEBOOKAPP,
              name='notebookApp', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(336, 402), style=0)

        self.panelRate = wx.Panel(id=wxID_FRAMEOPSPANELRATE, name='panelRate',
              parent=self.notebookApp, pos=wx.Point(0, 0), size=wx.Size(328,
              376), style=wx.TAB_TRAVERSAL)

        self.panelLogin = wx.Panel(id=wxID_FRAMEOPSPANELLOGIN,
              name='panelLogin', parent=self.notebookApp, pos=wx.Point(0, 0),
              size=wx.Size(328, 376), style=wx.TAB_TRAVERSAL)

        self.panelOptions = wx.Panel(id=wxID_FRAMEOPSPANELOPTIONS,
              name='panelOptions', parent=self.notebookApp, pos=wx.Point(0, 0),
              size=wx.Size(328, 376), style=wx.TAB_TRAVERSAL)

        self.textCtrlImageTags = wx.TextCtrl(id=wxID_FRAMEOPSTEXTCTRLIMAGETAGS,
              name='textCtrlImageTags', parent=self.panelRate, pos=wx.Point(104,
              208), size=wx.Size(200, 48),
              style=wx.TE_MULTILINE | wx.TE_READONLY, value='')

        self.staticTextTags = wx.StaticText(id=wxID_FRAMEOPSSTATICTEXTTAGS,
              label='  Image Tags:', name='staticTextTags',
              parent=self.panelRate, pos=wx.Point(24, 224), size=wx.Size(66,
              13), style=0)

        self.textCtrlSubscribedTags = wx.TextCtrl(id=wxID_FRAMEOPSTEXTCTRLSUBSCRIBEDTAGS,
              name='textCtrlSubscribedTags', parent=self.panelRate,
              pos=wx.Point(104, 264), size=wx.Size(200, 48),
              style=wx.TE_MULTILINE, value='')
        self.textCtrlSubscribedTags.SetMaxLength(128)
        self.textCtrlSubscribedTags.Bind(wx.EVT_TEXT,
              self.OnTextCtrlSubscribedTagsText,
              id=wxID_FRAMEOPSTEXTCTRLSUBSCRIBEDTAGS)

        self.buttonRateOK = wx.Button(id=wxID_FRAMEOPSBUTTONRATEOK,
              label='OK', name='buttonRateOK', parent=self.panelRate,
              pos=wx.Point(24, 344), size=wx.Size(75, 23), style=0)
        self.buttonRateOK.Bind(wx.EVT_BUTTON, self.OnButtonRateOKButton,
              id=wxID_FRAMEOPSBUTTONRATEOK)

        self.buttonRateCancel = wx.Button(id=wxID_FRAMEOPSBUTTONRATECANCEL,
              label='Cancel', name='buttonRateCancel', parent=self.panelRate,
              pos=wx.Point(128, 344), size=wx.Size(75, 23), style=0)
        self.buttonRateCancel.Bind(wx.EVT_BUTTON, self.OnButtonRateCancelButton,
              id=wxID_FRAMEOPSBUTTONRATECANCEL)

        self.staticTextSubscribedTags = wx.StaticText(id=wxID_FRAMEOPSSTATICTEXTSUBSCRIBEDTAGS,
              label='Subscribed Tags:', name='staticTextSubscribedTags',
              parent=self.panelRate, pos=wx.Point(16, 280), size=wx.Size(82,
              13), style=0)

        self.staticTextLogin = wx.StaticText(id=wxID_FRAMEOPSSTATICTEXTLOGIN,
              label='Username:', name='staticTextLogin', parent=self.panelLogin,
              pos=wx.Point(48, 40), size=wx.Size(52, 13), style=0)
        self.staticTextLogin.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'MS Shell Dlg 2'))

        self.staticTextPassword = wx.StaticText(id=wxID_FRAMEOPSSTATICTEXTPASSWORD,
              label=' Password:', name='staticTextPassword',
              parent=self.panelLogin, pos=wx.Point(48, 72), size=wx.Size(53,
              13), style=0)

        self.textCtrlLogin = wx.TextCtrl(id=wxID_FRAMEOPSTEXTCTRLLOGIN,
              name='textCtrlLogin', parent=self.panelLogin, pos=wx.Point(128,
              40), size=wx.Size(168, 21), style=0, value='')
        self.textCtrlLogin.SetMaxLength(32)
        self.textCtrlLogin.Bind(wx.EVT_TEXT, self.OnTextCtrlLoginText,
              id=wxID_FRAMEOPSTEXTCTRLLOGIN)

        self.checkBoxLoginRemember = wx.CheckBox(id=wxID_FRAMEOPSCHECKBOXLOGINREMEMBER,
              label='Remember me on this computer',
              name='checkBoxLoginRemember', parent=self.panelLogin,
              pos=wx.Point(128, 152), size=wx.Size(176, 13), style=0)
        self.checkBoxLoginRemember.SetValue(False)
        self.checkBoxLoginRemember.Bind(wx.EVT_CHECKBOX,
              self.OnCheckBoxLoginRememberCheckbox,
              id=wxID_FRAMEOPSCHECKBOXLOGINREMEMBER)

        self.buttonRateHelp = wx.Button(id=wxID_FRAMEOPSBUTTONRATEHELP,
              label='Help', name='buttonRateHelp', parent=self.panelRate,
              pos=wx.Point(232, 344), size=wx.Size(75, 23), style=0)
        self.buttonRateHelp.Bind(wx.EVT_BUTTON, self.OnButtonRateHelpButton,
              id=wxID_FRAMEOPSBUTTONRATEHELP)

        self.buttonLoginOK = wx.Button(id=wxID_FRAMEOPSBUTTONLOGINOK,
              label='OK', name='buttonLoginOK', parent=self.panelLogin,
              pos=wx.Point(24, 344), size=wx.Size(75, 23), style=0)
        self.buttonLoginOK.Bind(wx.EVT_BUTTON, self.OnButtonLoginOKButton,
              id=wxID_FRAMEOPSBUTTONLOGINOK)

        self.buttonLoginCancel = wx.Button(id=wxID_FRAMEOPSBUTTONLOGINCANCEL,
              label='Cancel', name='buttonLoginCancel', parent=self.panelLogin,
              pos=wx.Point(128, 344), size=wx.Size(75, 23), style=0)
        self.buttonLoginCancel.Bind(wx.EVT_BUTTON,
              self.OnButtonLoginCancelButton,
              id=wxID_FRAMEOPSBUTTONLOGINCANCEL)

        self.buttonLoginHelp = wx.Button(id=wxID_FRAMEOPSBUTTONLOGINHELP,
              label='Help', name='buttonLoginHelp', parent=self.panelLogin,
              pos=wx.Point(232, 344), size=wx.Size(75, 23), style=0)
        self.buttonLoginHelp.Bind(wx.EVT_BUTTON, self.OnButtonLoginHelpButton,
              id=wxID_FRAMEOPSBUTTONLOGINHELP)

        self.buttonOptionsOK = wx.Button(id=wxID_FRAMEOPSBUTTONOPTIONSOK,
              label='OK', name='buttonOptionsOK', parent=self.panelOptions,
              pos=wx.Point(24, 344), size=wx.Size(75, 23), style=0)
        self.buttonOptionsOK.Bind(wx.EVT_BUTTON, self.OnButtonOptionsOKButton,
              id=wxID_FRAMEOPSBUTTONOPTIONSOK)

        self.buttonOptionsCancel = wx.Button(id=wxID_FRAMEOPSBUTTONOPTIONSCANCEL,
              label='Cancel', name='buttonOptionsCancel',
              parent=self.panelOptions, pos=wx.Point(128, 344), size=wx.Size(75,
              23), style=0)
        self.buttonOptionsCancel.Bind(wx.EVT_BUTTON,
              self.OnButtonOptionsCancelButton,
              id=wxID_FRAMEOPSBUTTONOPTIONSCANCEL)

        self.buttonOptionsHelp = wx.Button(id=wxID_FRAMEOPSBUTTONOPTIONSHELP,
              label='Help', name='buttonOptionsHelp', parent=self.panelOptions,
              pos=wx.Point(232, 344), size=wx.Size(75, 23), style=0)
        self.buttonOptionsHelp.Bind(wx.EVT_BUTTON,
              self.OnButtonOptionsHelpButton,
              id=wxID_FRAMEOPSBUTTONOPTIONSHELP)

        self.choiceOptionRatedAtLeast = wx.Choice(choices=["1 Star", "2 Stars",
              "3 Stars", "4 Stars", "5 Stars"],
              id=wxID_FRAMEOPSCHOICEOPTIONRATEDATLEAST,
              name='choiceOptionRatedAtLeast', parent=self.panelOptions,
              pos=wx.Point(200, 40), size=wx.Size(80, 21), style=0)
        self.choiceOptionRatedAtLeast.SetStringSelection('')
        self.choiceOptionRatedAtLeast.SetSelection(0)
        self.choiceOptionRatedAtLeast.Bind(wx.EVT_CHOICE,
              self.OnChoiceOptionRatedAtLeastChoice,
              id=wxID_FRAMEOPSCHOICEOPTIONRATEDATLEAST)

        self.staticTextRatedAtLeast = wx.StaticText(id=wxID_FRAMEOPSSTATICTEXTRATEDATLEAST,
              label='Display images rated at least:',
              name='staticTextRatedAtLeast', parent=self.panelOptions,
              pos=wx.Point(40, 40), size=wx.Size(142, 13), style=0)

        self.staticTextPercentUnrated = wx.StaticText(id=wxID_FRAMEOPSSTATICTEXTPERCENTUNRATED,
              label=' Percentage of unrated images:',
              name='staticTextPercentUnrated', parent=self.panelOptions,
              pos=wx.Point(32, 72), size=wx.Size(152, 13), style=0)

        self.choiceOptionPercentUnrated = wx.Choice(choices=["5%", "10%", "20%",
              "50%", "75%", "100%"],
              id=wxID_FRAMEOPSCHOICEOPTIONPERCENTUNRATED,
              name='choiceOptionPercentUnrated', parent=self.panelOptions,
              pos=wx.Point(200, 72), size=wx.Size(80, 21), style=0)
        self.choiceOptionPercentUnrated.SetSelection(2)
        self.choiceOptionPercentUnrated.Bind(wx.EVT_CHOICE,
              self.OnChoiceOptionPercentUnratedChoice,
              id=wxID_FRAMEOPSCHOICEOPTIONPERCENTUNRATED)

        self.staticTextChangeEvery = wx.StaticText(id=wxID_FRAMEOPSSTATICTEXTCHANGEEVERY,
              label='Change image every:', name='staticTextChangeEvery',
              parent=self.panelOptions, pos=wx.Point(80, 104), size=wx.Size(103,
              13), style=0)

        self.choiceOptionChangeEvery = wx.Choice(choices=["15 minutes",
              "30 minutes", "1 hour", "2 hours", "4 hours", "8 hours", "1 day",
              "2 days", "4 days", "1 week"],
              id=wxID_FRAMEOPSCHOICEOPTIONCHANGEEVERY,
              name='choiceOptionChangeEvery', parent=self.panelOptions,
              pos=wx.Point(200, 104), size=wx.Size(80, 21), style=0)
        self.choiceOptionChangeEvery.SetStringSelection('')
        self.choiceOptionChangeEvery.SetSelection(3)
        self.choiceOptionChangeEvery.Bind(wx.EVT_CHOICE,
              self.OnChoiceOptionChangeEveryChoice,
              id=wxID_FRAMEOPSCHOICEOPTIONCHANGEEVERY)

        self.toggleButtonRateFlag = wx.ToggleButton(id=wxID_FRAMEOPSTOGGLEBUTTONRATEFLAG,
              label='Flag As Inappropriate', name='toggleButtonRateFlag',
              parent=self.panelRate, pos=wx.Point(176, 32), size=wx.Size(120,
              23), style=0)
        self.toggleButtonRateFlag.SetValue(False)
        self.toggleButtonRateFlag.Bind(wx.EVT_TOGGLEBUTTON,
              self.OnToggleButtonRateFlagTogglebutton,
              id=wxID_FRAMEOPSTOGGLEBUTTONRATEFLAG)

        self.textCtrlPassword = wx.TextCtrl(id=wxID_FRAMEOPSTEXTCTRLPASSWORD,
              name='textCtrlPassword', parent=self.panelLogin, pos=wx.Point(128,
              72), size=wx.Size(168, 21), style=wx.TE_PASSWORD, value='')
        self.textCtrlPassword.SetMaxLength(32)
        self.textCtrlPassword.Bind(wx.EVT_TEXT, self.OnTextCtrlPasswordText,
              id=wxID_FRAMEOPSTEXTCTRLPASSWORD)

        self.staticBoxRate = wx.StaticBox(id=wxID_FRAMEOPSSTATICBOXRATE,
              label='Rating', name='staticBoxRate', parent=self.panelRate,
              pos=wx.Point(8, 8), size=wx.Size(312, 168), style=0)

        self.staticBoxTag = wx.StaticBox(id=wxID_FRAMEOPSSTATICBOXTAG,
              label='Tags', name='staticBoxTag', parent=self.panelRate,
              pos=wx.Point(8, 184), size=wx.Size(312, 144), style=0)

        self.panelAbout = wx.Panel(id=wxID_FRAMEOPSPANELABOUT,
              name='panelAbout', parent=self.notebookApp, pos=wx.Point(0, 0),
              size=wx.Size(328, 376), style=wx.TAB_TRAVERSAL)

        self.buttonAboutOK = wx.Button(id=wxID_FRAMEOPSBUTTONABOUTOK,
              label='OK', name='buttonAboutOK', parent=self.panelAbout,
              pos=wx.Point(24, 344), size=wx.Size(75, 23), style=0)
        self.buttonAboutOK.Bind(wx.EVT_BUTTON, self.OnButtonAboutOKButton,
              id=wxID_FRAMEOPSBUTTONABOUTOK)

        self.staticBoxLogin = wx.StaticBox(id=wxID_FRAMEOPSSTATICBOXLOGIN,
              label='Sign In', name='staticBoxLogin', parent=self.panelLogin,
              pos=wx.Point(8, 8), size=wx.Size(312, 176), style=0)

        self.staticBoxOptions = wx.StaticBox(id=wxID_FRAMEOPSSTATICBOXOPTIONS,
              label='Display Options', name='staticBoxOptions',
              parent=self.panelOptions, pos=wx.Point(8, 8), size=wx.Size(312,
              136), style=0)

        self.buttonAboutCancel = wx.Button(id=wxID_FRAMEOPSBUTTONABOUTCANCEL,
              label='Cancel', name='buttonAboutCancel', parent=self.panelAbout,
              pos=wx.Point(128, 344), size=wx.Size(75, 23), style=0)
        self.buttonAboutCancel.Bind(wx.EVT_BUTTON,
              self.OnButtonAboutCancelButton,
              id=wxID_FRAMEOPSBUTTONABOUTCANCEL)

        self.buttonAboutHelp = wx.Button(id=wxID_FRAMEOPSBUTTONABOUTHELP,
              label='Help', name='buttonAboutHelp', parent=self.panelAbout,
              pos=wx.Point(232, 344), size=wx.Size(75, 23), style=0)
        self.buttonAboutHelp.Bind(wx.EVT_BUTTON, self.OnButtonAboutHelpButton,
              id=wxID_FRAMEOPSBUTTONABOUTHELP)

        self.staticBoxAbout = wx.StaticBox(id=wxID_FRAMEOPSSTATICBOXABOUT,
              label='About Twirli', name='staticBoxAbout',
              parent=self.panelAbout, pos=wx.Point(8, 8), size=wx.Size(312,
              320), style=0)

        self.buttonSignIn = wx.Button(id=wxID_FRAMEOPSBUTTONSIGNIN,
              label='Sign In', name='buttonSignIn', parent=self.panelLogin,
              pos=wx.Point(128, 112), size=wx.Size(75, 23), style=0)
        self.buttonSignIn.Bind(wx.EVT_BUTTON, self.OnButtonSignInButton,
              id=wxID_FRAMEOPSBUTTONSIGNIN)

        self.staticTextSignedIn = wx.StaticText(id=wxID_FRAMEOPSSTATICTEXTSIGNEDIN,
              label='You are not signed in.', name='staticTextSignedIn',
              parent=self.panelLogin, pos=wx.Point(88, 208), size=wx.Size(163,
              18), style=0)
        self.staticTextSignedIn.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL,
              wx.BOLD, False, 'MS Shell Dlg 2'))

        self.bitmapButton1Star = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAMEOPSBITMAPBUTTON1STAR, name='bitmapButton1Star',
              parent=self.panelRate, pos=wx.Point(32, 32), size=wx.Size(24, 24),
              style=wx.BU_AUTODRAW)
        self.bitmapButton1Star.Bind(wx.EVT_BUTTON,
              self.OnBitmapButton1StarButton,
              id=wxID_FRAMEOPSBITMAPBUTTON1STAR)

        self.bitmapButton2Star = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAMEOPSBITMAPBUTTON2STAR, name='bitmapButton2Star',
              parent=self.panelRate, pos=wx.Point(56, 32), size=wx.Size(24, 24),
              style=wx.BU_AUTODRAW)
        self.bitmapButton2Star.Bind(wx.EVT_BUTTON,
              self.OnBitmapButton2StarButton,
              id=wxID_FRAMEOPSBITMAPBUTTON2STAR)

        self.bitmapButton3Star = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAMEOPSBITMAPBUTTON3STAR, name='bitmapButton3Star',
              parent=self.panelRate, pos=wx.Point(80, 32), size=wx.Size(24, 24),
              style=wx.BU_AUTODRAW)
        self.bitmapButton3Star.Bind(wx.EVT_BUTTON,
              self.OnBitmapButton3StarButton,
              id=wxID_FRAMEOPSBITMAPBUTTON3STAR)

        self.bitmapButton4Star = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAMEOPSBITMAPBUTTON4STAR, name='bitmapButton4Star',
              parent=self.panelRate, pos=wx.Point(104, 32), size=wx.Size(24,
              24), style=wx.BU_AUTODRAW)
        self.bitmapButton4Star.Bind(wx.EVT_BUTTON,
              self.OnBitmapButton4StarButton,
              id=wxID_FRAMEOPSBITMAPBUTTON4STAR)

        self.bitmapButton5Star = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAMEOPSBITMAPBUTTON5STAR, name='bitmapButton5Star',
              parent=self.panelRate, pos=wx.Point(128, 32), size=wx.Size(24,
              24), style=wx.BU_AUTODRAW)
        self.bitmapButton5Star.Bind(wx.EVT_BUTTON,
              self.OnBitmapButton5StarButton,
              id=wxID_FRAMEOPSBITMAPBUTTON5STAR)

        self.textCtrlImageInfo = wx.TextCtrl(id=wxID_FRAMEOPSTEXTCTRLIMAGEINFO,
              name='textCtrlImageInfo', parent=self.panelRate, pos=wx.Point(32,
              64), size=wx.Size(264, 64),
              style=wx.TE_READONLY | wx.TE_MULTILINE, value='')

        self.buttonSubmitterPage = wx.Button(id=wxID_FRAMEOPSBUTTONSUBMITTERPAGE,
              label='Wallpaper Homepage', name='buttonSubmitterPage',
              parent=self.panelRate, pos=wx.Point(176, 136), size=wx.Size(120,
              23), style=0)
        self.buttonSubmitterPage.Bind(wx.EVT_BUTTON,
              self.OnButtonSubmitterPageButton,
              id=wxID_FRAMEOPSBUTTONSUBMITTERPAGE)

        self.buttonNewImage = wx.Button(id=wxID_FRAMEOPSBUTTONNEWIMAGE,
              label='New Wallpaper', name='buttonNewImage',
              parent=self.panelRate, pos=wx.Point(32, 136), size=wx.Size(120,
              23), style=0)
        self.buttonNewImage.Bind(wx.EVT_BUTTON, self.OnButtonNewImageButton,
              id=wxID_FRAMEOPSBUTTONNEWIMAGE)

        self._init_coll_notebookApp_Pages(self.notebookApp)


    def __init__(self, parent, config, twirlpath):
        """Initialize frame and icons, update frame with
        values from config"""
        self._init_ctrls(parent)

        # Merely hide frame if the close window [X] button used
        self.Bind(wx.EVT_CLOSE, self.OnFrameClose)
        
        # Load config data and make temporary copy, updates not passed
        # to main copy until user pressed OK so as to not cause any
        # intervening image downloads to be based on intermediate values
        self._config = config
        self._configtmp = ConfigOps()
        self._configtmp.update(config)
        
        # Set local config variables
        self._twirlpath = twirlpath
        self._hashed = ""

        # Set program icon
        self.SetIcon(icons.getTwirliIcon())

		# Generate list containing icons
        iconlist = wx.ImageList(16, 16)
        iconyellowstar = iconlist.Add(icons.getYellowStarBitmap())
        iconuser = iconlist.Add(icons.getUserBitmap())
        iconwrench = iconlist.Add(icons.getWrenchBitmap())
        iconinfo = iconlist.Add(icons.getInfoBitmap())

        # Assign icon list to notebook, then assign icons
        # to individual pages
        self.notebookApp.AssignImageList(iconlist)
        self.notebookApp.SetPageImage(0, iconyellowstar)
        self.notebookApp.SetPageImage(1, iconuser)
        self.notebookApp.SetPageImage(2, iconwrench)
        self.notebookApp.SetPageImage(3, iconinfo)


    def OnFrameShow(self):
        """Update all frame options and status before showing"""

        # Update local copy of config
        self._configtmp.update(self._config)

        # Fix notebook background color when switching themes in XP
        self.notebookApp.SetBackgroundColour(\
            self.notebookApp.GetThemeBackgroundColour())

        # Set flag
        self.toggleButtonRateFlag.SetValue(self._configtmp["flagimage"])

        # Set ratings
        self._iconstars = [icons.getGrayStarBitmap(),
            icons.getYellowStarBitmap(),
            icons.getGrayOrangeStarBitmap(),
            icons.getYellowOrangeStarBitmap()]
        self.SetStars()

        # Set image info
        self.textCtrlImageInfo.WriteText(self._configtmp["imageinfo"])

        # Set tags
        self.textCtrlImageTags.WriteText(self._configtmp["imagetags"])
        self.textCtrlSubscribedTags.WriteText(self._configtmp["subscribedtags"])

        # If login still valid, change text on Sign In page
        if (self._configtmp["userid"] != "0000000000000000")\
            and (self._configtmp["rememberme"] == True):
            self.staticTextSignedIn.SetLabel("    You are signed in.")
            self.textCtrlLogin.WriteText(self._configtmp["login"])
            self.checkBoxLoginRemember.SetValue(True)
        
        # Set options
        _ratelist = [1, 2, 3, 4, 5]
        self.choiceOptionRatedAtLeast.SetSelection(
            _ratelist.index(self._configtmp["ratedatleast"]))
        _percentlist = [5, 10, 20, 50, 75, 100]
        self.choiceOptionPercentUnrated.SetSelection(
            _percentlist.index(self._configtmp["percentnew"]))
        _changeeverylist = [900, 1800, 3600, 7200, 14400, 28800, 86400,
            172800, 345600, 604800]
        self.choiceOptionChangeEvery.SetSelection(
            _changeeverylist.index(self._configtmp["changeevery"]))
        
        # Update complete, show frame
        self.Show()
        self.Raise()


    def OnFrameClose(self, event):
        """Hide the frame when the close window [X] used"""
        self.Hide()

    def SetStars(self):
        """Set ratings stars based on image and user ratings"""
        startype = [self._iconstars[
            self.CalcStar(starnum,\
                self._configtmp["imagerating"],
                self._configtmp["userrating"])]\
            for starnum in range(1,6)]
        self.bitmapButton1Star.SetBitmapLabel(startype[0])
        self.bitmapButton2Star.SetBitmapLabel(startype[1])
        self.bitmapButton3Star.SetBitmapLabel(startype[2])
        self.bitmapButton4Star.SetBitmapLabel(startype[3])
        self.bitmapButton5Star.SetBitmapLabel(startype[4])

    def CalcStar(self, starnum, imagerating, userrating):
        """Calculate the star type that the star button should get
        Star types = [ gray, yellow, gray/orange, yellow/orange ]
        Indicating = [ image/user unrated, image rated,
                                    user rated, image/user rated ]"""
        type = 0
        if imagerating >= starnum: type += 1
        if userrating >= starnum: type += 2
        return type


    def OnBitmapButton1StarButton(self, event):
        """Set star bitmaps to match 1-star button press"""
        self._configtmp["userrating"] = 1
        self.SetStars()

    def OnBitmapButton2StarButton(self, event):
        """Set star bitmaps to match 2-star button press"""
        self._configtmp["userrating"] = 2
        self.SetStars()

    def OnBitmapButton3StarButton(self, event):
        """Set star bitmaps to match 3-star button press"""
        self._configtmp["userrating"] = 3
        self.SetStars()

    def OnBitmapButton4StarButton(self, event):
        """Set star bitmaps to match 4-star button press"""
        self._configtmp["userrating"] = 4
        self.SetStars()

    def OnBitmapButton5StarButton(self, event):
        """Set star bitmaps to match 5-star button press"""
        self._configtmp["userrating"] = 5
        self.SetStars()

    def OnToggleButtonRateFlagTogglebutton(self, event):
        """Set flag variable but do not send until user presses OK"""
        self._configtmp["flagimage"] = self.toggleButtonRateFlag.GetValue()

    def OnButtonNewImageButton(self, event):
        """Initiate new image by setting next change time to 0"""
        self._config["nextchangetime"] = 0

    def OnButtonSubmitterPageButton(self, event):
        """Open webbrowser to image URL"""
        webbrowser.open(self._configtmp["imageurl"])

    def OnTextCtrlSubscribedTagsText(self, event):
        """Save user tags but do not send until user presses OK"""
        self._configtmp["subscribedtags"] = event.GetString()

    def OnButtonRateOKButton(self, event):
        """All OK buttons do the same actions --
        Function forwarded to OnButtonOKButton"""
        self.OnButtonOKButton()

    def OnButtonRateCancelButton(self, event):
        """Rehide frame if action cancelled"""
        self.Hide()

    def OnButtonRateHelpButton(self, event):
        """Open webbrowser to Rate panel help page"""
        webbrowser.open(consts.HELP_RATE)

    def OnTextCtrlLoginText(self, event):
        """Save login but do not send until user presses OK"""
        self._configtmp["login"] = event.GetString()

    def OnTextCtrlPasswordText(self, event):
        #***encode password and store it as a hashed value
        #***self._hashed = encoded....
        self._hashed = event.GetString()

    def OnButtonSignInButton(self, event):
        """Send login and hashed password to server, get back userid.
        Save valid userid immediately to config so that any image
        requests are associated with the correct user.
        Update text on Sign In page based on whether userid is valid."""
        self._configtmp["userid"] =\
            netops.SendLogin(self._configtmp["login"], self._hashed)
        if self._configtmp["userid"] != "0000000000000000":
            self.staticTextSignedIn.SetLabel("    You are signed in.")
            self._config["userid"] = self._configtmp["userid"]
        else:
            self.staticTextSignedIn.SetLabel("You are not signed in.")

    def OnCheckBoxLoginRememberCheckbox(self, event):
        """Save remember me setting but do not send until user presses OK"""
        self._configtmp["rememberme"] = event.IsChecked()

    def OnButtonLoginOKButton(self, event):
        """All OK buttons do the same actions --
        Function forwarded to OnButtonOKButton"""
        self.OnButtonOKButton()

    def OnButtonLoginCancelButton(self, event):
        """Rehide frame if action cancelled"""
        self.Hide()

    def OnButtonLoginHelpButton(self, event):
        """Open webbrowser to Sign In panel help page"""
        webbrowser.open(consts.HELP_LOGIN)

    def OnChoiceOptionRatedAtLeastChoice(self, event):
        """Update minimum rating choice according to user selection"""
        _ratedict = {"1 Star":1, "2 Stars":2, "3 Stars":3,
            "4 Stars":4, "5 Stars":5}
        self._configtmp["ratedatleast"] = _ratedict[event.GetString()]

    def OnChoiceOptionPercentUnratedChoice(self, event):
        """Update percentage choice according to user selection"""
        _percentdict = {"5%":5, "10%":10, "20%":20, "50%":50,
            "75%":75, "100%":100}
        self._configtmp["percentnew"] = _percentdict[event.GetString()]

    def OnChoiceOptionChangeEveryChoice(self, event):
        """Update change time to last change time plus new changeevery so
        that program does not wait until last changeevery time is up before
        changing again, which is strange if last changeevery is longer.
        E.g. Don't make user wait out the rest of the week if he changed
        his changeevery to an hour.
        """
        _changedict = {"15 minutes":900, "30 minutes":1800, "1 hour":3600,
            "2 hours":7200, "4 hours":14400, "8 hours":28800, "1 day":86400,
            "2 days":172800, "4 days":345600, "1 week":604800}

        self._configtmp["nextchangetime"] = self._config["nextchangetime"]\
            - self._configtmp["changeevery"] + _changedict[event.GetString()]
        self._configtmp["changeevery"] = _changedict[event.GetString()]

    def OnButtonOptionsOKButton(self, event):
        """All OK buttons do the same actions --
        Function forwarded to OnButtonOKButton"""
        self.OnButtonOKButton()

    def OnButtonOptionsCancelButton(self, event):
        """Rehide frame if action cancelled"""
        self.Hide()

    def OnButtonOptionsHelpButton(self, event):
        """Open webbrowser to Options panel help page"""
        webbrowser.open(consts.HELP_OPTIONS)

    def OnButtonAboutOKButton(self, event):
        """All OK buttons do the same actions --
        Function forwarded to OnButtonOKButton"""
        self.OnButtonOKButton()

    def OnButtonAboutCancelButton(self, event):
        """Rehide frame if action cancelled"""
        self.Hide()

    def OnButtonAboutHelpButton(self, event):
        """Open webbrowser to About panel help page"""
        webbrowser.open(consts.HELP_ABOUT)

    def OnButtonOKButton(self):
        """Send all metadata to server, update and save config,
        then hide frame"""
        netops.SendMetadata(consts.ALL_META)
        if self._config != self._configtmp:
            self._config.update(self._configtmp)
            self._config.Save(self._twirlpath)
        self.Hide()
