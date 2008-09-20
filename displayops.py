"""Screen display operations"""


__author__		= "Shultz Wang"
__version__		= "Revision 0.1"
__date__		= "Tuesday, August 07, 2007 22:59:05"
__copyright__	= "Copyright (c) 2007 Shultz Wang"


# Library modules
try:
	# Use the faster cStringIO if possible
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO
from ctypes import windll
from PIL import Image


class DisplayError(Exception):
	"""Image cannot be displayed error

	This exception does nothing"""
	pass


def DisplayImage(imagedata, exepath):
	"""Display image as wallpaper (Microsoft Windows version)

	Takes an image filename, a tuple containing the display
	size (x,y), and the executable's path.  If image cannot
	be displayed, DisplayError is raised."""

	# If image dimensions != display size,
	# resize image, then save image as BMP
	try:
		# pilimage = Image.open(StringIO(image)) did not work,
		# because image file objects were not closed
		# ==> Be sure that local test file objects get closed!
		pilimage = Image.open(StringIO(imagedata))

		# Can get display size through
		#	dispx, dispy = wx.DisplaySize()
		# or
		#	SM_CXSCREEN = 0
		#	SM_CYSCREEN = 1
		#	dispx, dispy = (ctypes.windll.user32.GetSystemMetrics(SM_CXSCREEN),
		#		ctypes.windll.user32.GetSystemMetrics(SM_CYSCREEN))
		# Using ctypes method since ctypes already imported, no need to
		# depend on wx.App being  already created.
		SM_CXSCREEN = 0
		SM_CYSCREEN = 1
		dispx, dispy = (windll.user32.GetSystemMetrics(SM_CXSCREEN),
			windll.user32.GetSystemMetrics(SM_CYSCREEN))
		imagex, imagey = pilimage.size
		if dispx < imagex or dispy < imagey:
			pilimage.thumbnail((dispx,dispy), Image.ANTIALIAS)
		pilimage.save(exepath + "image.bmp")
	except:
		raise DisplayError("Image cannot be displayed")

	# Display image
	SPI_SETDESKWALLPAPER = 20
	SPIF_UPDATEINIFILE = 1		# Change INI file
	SPIF_SENDWININICHANGE = 2	# Notify Windows of INI file change
	windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0,
		exepath + "image.bmp" , SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
