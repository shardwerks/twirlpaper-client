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
		urlopener = build_opener()
		urlopener.addheaders = [('User-Agent', consts.USER_AGENT)]
		imagedata = urlopener.open(quote(urladdr, ':/'))
		image = imagedata.read(41943040)	# Bound read to 4MB
		imagedata.close()
	except:
		raise Exception()
	return image


def SendMetadata(urladdr, meta):
	"""Generic metadata transmission"""
	try:
		urlopener = build_opener()
		urlopener.addheaders = [('User-Agent', consts.USER_AGENT)]
		answer = urlopener.open(quote(urladdr, ':/')).read(1048576)	# Bound read to 128kB
		return ParseMeta(answer)
	except:
		print 'Cannot connect to internet'


def SendLogin(username, password):
	"""Authenticate with HTTP Digest Authentication,
	then receive user ID"""

	# Use HTTP digest authentication
	try:
		authen = HTTPDigestAuthHandler()
		authen.add_password(realm = consts.REALM,
			uri = consts.URL_REQ_LOGIN,
			user = username.encode('utf-8'),
			#passwd = md5(password.encode('utf-8')+username.encode('utf-8')\
			#+consts.REALM).hexdigest())
			passwd = md5(password.encode('utf-8')).hexdigest())
		opener = build_opener(authen)
		opener.addheaders = [('User-Agent', consts.USER_AGENT)]
		install_opener(opener)
		# Take return value to be user ID, limit return value to 32 characters for protection
		answer = opener.open(consts.URL_REQ_LOGIN).read(1048576) # Bound read to 128kB
	except IOError, e:
		return ParseWebError(e)
	except:
		return {'msg':'Cannot reach website'}
	return ParseMeta(answer)


def ParseWebError(err):
	if hasattr(err, 'reason'):
		return {'msg':'Cannot fulfill request: %d' % err.reason}
	elif hasattr(err, 'code'):
		if err.code == 401:
			return {'msg':'Incorrect login/password'}
		else:
			return {'msg':'Cannot reach website: %d' % err.code}
	else:
		return {'msg':'Cannot reach website'}


def ParseMeta(meta):
	"""Separate returned metadata into dictionary"""
	#print meta
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
