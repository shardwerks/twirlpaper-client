"""Error popup operations"""

#-----------------------------------------------------------------------------
# Name:		errpops.py
# Purpose:	 
#
# Author:	  Shultz Wang
#
# Created:	 2010/01/21
# RCS-ID:	  $Id: errpops.py $
# Copyright:   (c) 2010
# Licence:	 <your licence>
#-----------------------------------------------------------------------------


# Library modules
import wx
# Project modules
import icons

[wxID_MSGPOPS, wxID_MSGPOPSBUTTONOK, wxID_MSGPOPSSTATICTEXTMSG, wxID_MSGPOPSPANELMSG
] = [wx.NewId() for _init_ctrls in range(4)]


class MsgPops(wx.Frame):

	def _init_ctrls(self, prnt):
		"""Initialize controls"""

		# Pop up frame in middle of display
		dispx, dispy = wx.DisplaySize()
		upperx, uppery = ((dispx-244)/2, (dispy-129)/2)

		wx.Frame.__init__(self, id=wxID_MSGPOPS, name='MsgPops', parent=prnt,
			  pos=wx.Point(upperx, uppery), size=wx.Size(244, 144),
			  style=(wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER & ~wx.MAXIMIZE_BOX),
			  title='Twirlpaper Message')
		self.SetClientSize(wx.Size(236, 136))

		self.panelRate = wx.Panel(id=wxID_MSGPOPSPANELMSG, name='panelMsg',
			  parent=self, pos=wx.Point(0, 0), size=wx.Size(236, 136),
			  style=wx.TAB_TRAVERSAL)

		self.buttonOK = wx.Button(id=wxID_MSGPOPSBUTTONOK, label='OK',
			  name='buttonOK', parent=self.panelRate, pos=wx.Point(82, 100),
			  size=wx.Size(72, 24), style=0)
		self.buttonOK.Bind(wx.EVT_BUTTON, self.OnButtonOKButton,
			  id=wxID_MSGPOPSBUTTONOK)

		self.staticTextMsg = wx.StaticText(id=wxID_MSGPOPSSTATICTEXTMSG,
			  label='No news is good news.', name='staticTextMsg',
			  parent=self.panelRate, pos=wx.Point(16, 16), size=wx.Size(204,
			  80), style=wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE)
		#self.staticTextMsg.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL,
		#	  wx.BOLD, False, 'MS Shell Dlg 2'))


	def __init__(self, parent):
		"""Initialize frame and icons"""
		self._init_ctrls(parent)

		# Merely hide frame if the close window [X] button used
		self.Bind(wx.EVT_CLOSE, self.OnFrameClose)

		self.SetIcon(icons.getTwirlIcon())


	def OnFrameShow(self, msg):
		"""Update message before showing"""
		self.staticTextMsg.SetLabel(msg)

		# Update complete, show frame
		self.Show()
		self.Raise()

		
	def OnFrameClose(self, event):
		"""Hide the frame when the close window [X] used"""
		self.Hide()


	def OnButtonOKButton(self, event):
		"""Hide frame"""
		self.Hide()
