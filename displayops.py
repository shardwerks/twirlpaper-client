"""Screen display operations"""


__author__	  = 'Shultz Wang'
__version__	 = 'Revision 0.1'
__date__		= 'Tuesday, August 07, 2007 22:59:05'
__copyright__   = 'Copyright (c) 2007 Shultz Wang'


# Library modules
try:
	# Use the faster cStringIO if possible
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO
from ctypes import windll, c_char_p
from PIL.Image import open, new


class DisplayError(Exception):
	"""Image cannot be displayed error

	This exception does nothing"""
	pass


def DisplayImage(imagedata, twirlpath):
	"""Display image as wallpaper (Microsoft Windows version)

	Takes an image file and the executable's path.  If image cannot
	be displayed, DisplayError is raised."""

	# If image dimensions != display size,
	# resize image, then save image as BMP
	try:
		# pilimage = Image.open(StringIO(image)) did not work,
		# because image file objects were not closed
		# ==> Be sure that local test file objects get closed!
		pilimage = open(StringIO(imagedata))

		# Can get display size through
		#	dispx, dispy = wx.DisplaySize()
		# or
		#	SM_CXSCREEN = 0
		#	SM_CYSCREEN = 1
		#	dispx, dispy = (ctypes.windll.user32.GetSystemMetrics(SM_CXSCREEN),
		#		ctypes.windll.user32.GetSystemMetrics(SM_CYSCREEN))
		# Using ctypes method since ctypes already imported, no need to
		# depend on wx.App being already created.
		SM_CXSCREEN = 0
		SM_CYSCREEN = 1
		dispx, dispy = (windll.user32.GetSystemMetrics(SM_CXSCREEN),
			windll.user32.GetSystemMetrics(SM_CYSCREEN))
		imagex, imagey = pilimage.size

		# Resize based on the dimension furthest away from display resolution and
		# paste into black background of display size to avoid OS resize or stretch
		ratiox, ratioy = (float(dispx)/imagex, float(dispy)/imagey)
		if ratiox < 1 or ratioy < 1:
			if ratiox < ratioy:
				resizex, resizey = (dispx, int(imagey*ratiox))
				pastex, pastey = (0, (dispy-resizey)/2)
			else:
				resizex, resizey = (int(imagex*ratioy), dispy)
				pastex, pastey = ((dispx-resizex)/2, 0)
			pilimage = pilimage.resize((resizex, resizey), Image.ANTIALIAS)
		else:
			pastex, pastey = ((dispx-imagex)/2, (dispy-imagey)/2)
		pilblank = new('RGB', (dispx,dispy), 0)
		pilblank.paste(pilimage, (pastex,pastey))
		pilblank.save(twirlpath + '\image.bmp')
	except:
		raise DisplayError('Image cannot be displayed')

	# Display image
	SPI_SETDESKWALLPAPER = 20
	SPIF_UPDATEINIFILE = 1		# Change INI file
	SPIF_SENDWININICHANGE = 2	# Notify Windows of INI file change
	windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0,
		c_char_p(twirlpath + '\image.bmp'), SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
