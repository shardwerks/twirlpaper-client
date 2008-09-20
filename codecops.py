"""Encode and decode dictionary to and from a string"""


__author__		= "Shultz Wang"
__version__		= "Revision 0.1"
__date__		= "Tuesday, August 07, 2007 22:59:05"
__copyright__	= "Copyright (c) 2007 Shultz Wang"


# Library modules
try:
	# Use the faster cPickle if possible
	import cPickle as pickle
except ImportError:
	import pickle
import binascii

class DecodeError(Exception):
	"""Error decoding string into dictionary

	This exception does nothing"""
	pass


def Encode(dictinst):
	"""Encode dictionary into string

	Current method is NOT secure"""

	s = pickle.dumps(dictinst, pickle.HIGHEST_PROTOCOL)
	t = binascii.hexlify(s)
	u = binascii.a2b_base64(t)
	return u


def Decode(dictstr):
	"""Decode string into dictionary

	Will raise DecodeError if decode unsuccessful
	Current method is NOT secure"""

	try:
		v = binascii.b2a_base64(dictstr)
		w = binascii.unhexlify(v[:-1])
		x = pickle.loads(w)
		return x
	except:
		raise DecodeError("String cannot be decoded")
