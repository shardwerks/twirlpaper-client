"""Internet operations"""


__author__	  = 'Shultz Wang'
__version__	 = 'Revision 0.1'
__date__		= 'Tuesday, August 07, 2007 22:59:05'
__copyright__   = 'Copyright (c) 2007 Shultz Wang'


# Library modules
from hashlib import md5
from types import UnicodeType
from urllib import urlencode, quote
from urllib2 import urlopen, HTTPDigestAuthHandler, build_opener, install_opener
# Project modules
import consts

#for dummy ops
#import os
#import random


def DownloadImage(urladdr):
	"""Receive image from server"""
	try:
		useragent = urlencode({'User-Agent': 'Twirlpaper/0.1.0'})
		imagedata = urlopen(quote(urladdr, ':/'), useragent)
		image = imagedata.read(41943040)	# Bound read to 4MB
		imagedata.close()
	except:
		raise Exception("Cannot download image")
	return image


def SendMetadata(urladdr, meta):
	"""Generic metadata transmission"""
	try:
		meta['User-Agent'] = 'Twirlpaper/0.1.0'
		answer = urlopen(urladdr, urlencode(meta)).read(1048576)	# Bound read to 128kB
		return ParseMeta(answer)
	except:
		print 'Cannot connect to internet'


def SendLogin(username, password):
	"""Authenticate with HTTP Digest Authentication,
	then receive user ID"""

	# Use HTTP digest authentication
	try:
		useragent = urlencode({'User-Agent': 'Twirlpaper/0.1.0'})
		authen = HTTPDigestAuthHandler()
		authen.add_password(realm = consts.REALM,
			uri = consts.URL_REQ_LOGIN,
			user = username.encode('utf-8'),
			#passwd = md5(password.encode('utf-8')+username.encode('utf-8')\
			#+consts.REALM).hexdigest())
			passwd = md5(password.encode('utf-8')).hexdigest())
		install_opener(build_opener(authen))
		urlopen(consts.URL_REQ_LOGIN, useragent)
	except:
		return {'msg':'Cannot connect to website'}

	try:
		# Take return value to be user ID, limit return value to 32 characters for protection
		useragent = urlencode({'User-Agent': 'Twirlpaper/0.1.0'})
		answer = urlopen(consts.URL_REQ_LOGIN, useragent).read(1048576)	# Bound read to 128kB
	except:
		return {'msg':'Cannot connect to website'}
	return ParseMeta(answer)


def ParseMeta(meta):
	"""Separate returned metadata into dictionary"""
	lines = meta.split('\r\n')
	parsed = {}
	for item in lines:
		if item != '':
			parts = item.partition('=')
			if parts[2] == '':
				parsed[parts[0]] = '0'
			else:
				parsed[parts[0]] = parts[2]
	print parsed
	return parsed
