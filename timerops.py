"""Timer operations thread"""


__author__		= "Shultz Wang"
__version__		= "Revision 0.1"
__date__		= "Tuesday, August 07, 2007 22:59:05"
__copyright__	= "Copyright (c) 2007 Shultz Wang"


# Library modules
from time import time
from time import sleep
from threading import Thread
# Project modules
import netops
import twirlconst
from displayops import DisplayImage


class TimerOps(Thread):
	"""Timer for wallpaper change"""

	def __init__(self, config, twirlpath):
		Thread.__init__(self)
		self._running = True
		self._config = config
		self._twirlpath = twirlpath

	def run(self):
		# Use time.sleep instead of threading.Timer since the latter will
		# spawn a separate thread and not be subject to waiting until
		# the countdown is complete before while-looping again
		while (self._running):
		    sleep(1)
		    self.TimeCheck()

	def Stop(self):
		self._running = False


	def TimeCheck(self):
		"""Check if the wait period has passed and update image"""

		if time() > self._config["nextchangetime"]:
			# Download new image to the executable's directory, and
			# name it wallpaper.jpg
			imagedata = netops.DownloadImage()

			# Display new image
			try:
				DisplayImage(imagedata, self._twirlpath)
			except DisplayError:
				# Send error to server
				netops.SendMetaData(DISPLAYERROR)

			# Update change time
			self._config["nextchangetime"] = time() + self._config["changeevery"]
