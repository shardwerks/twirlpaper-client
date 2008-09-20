"""Internet operations"""


__author__		= "Shultz Wang"
__version__		= "Revision 0.1"
__date__		= "Tuesday, August 07, 2007 22:59:05"
__copyright__	= "Copyright (c) 2007 Shultz Wang"


# Library modules
# Project modules
import twirlconst

#for dummy ops
import os
import random

"""
class NetOps():

	def __init__(self):
		self._url = ""
"""
	# Send request to server


#	def DownloadImage(self):
def DownloadImage():
	# Receive image and metadata

	#dummy op
	try:
		try:
			fchoose = random.choice(os.listdir("d:\\Wallpapers\\JPG"))
			f = open("d:\\Wallpapers\\JPG\\"+fchoose, 'rb')
			g = f.read()
		finally:
			f.close()
	except:
		raise #Exception("Cannot get files from d drive")
	return g


#	def SendMetaData(self, twirlconst):
def SendMetaData(twirlconst):
	# Send login and metadata

	#dummy op
	print "Meta data sending holder: %s" % twirlconst

def SendLogin(login, hashed):
	return random.randint(0,10000000000000000)

