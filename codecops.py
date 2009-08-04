"""Encode and decode dictionary to and from a string"""


__author__	  = 'Shultz Wang'
__version__	 = 'Revision 0.1'
__date__		= 'Tuesday, August 07, 2007 22:59:05'
__copyright__   = 'Copyright (c) 2007 Shultz Wang'


# Library modules
try:
	# Use the faster cPickle if possible
	import cPickle as pickle
except ImportError:
	import pickle
from binascii import hexlify, unhexlify


class DecodeError(Exception):
	"""Error decoding string into dictionary

	This exception does nothing"""
	pass


def Encode(dictinst):
	"""Encode dictionary into string
	Current method is NOT meant to be secure."""
	s = pickle.dumps(dictinst, pickle.HIGHEST_PROTOCOL)
	t = hexlify(s)
	# For some reason a2b_base64 would fail once in a while
	#u = binascii.a2b_base64(t)
	#return u
	return t


def Decode(dictstr):
	"""Decode string into dictionary
	Will raise DecodeError if decode unsuccessful
	Current method is NOT meant to be secure"""
	try:
		# For some reason a2b_base64 would fail once in a while
		#v = binascii.b2a_base64(dictstr)
		#w = binascii.unhexlify(v[:-1])
		w = unhexlify(dictstr)
		x = pickle.loads(w)
		return x
	except:
		#raise DecodeError('String cannot be decoded')
		pass

