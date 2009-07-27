"""Internet operations"""


__author__      = 'Shultz Wang'
__version__     = 'Revision 0.1'
__date__        = 'Tuesday, August 07, 2007 22:59:05'
__copyright__   = 'Copyright (c) 2007 Shultz Wang'


# Library modules
from hashlib import md5
from types import UnicodeType
from urllib import urlencode
from urllib2 import urlopen, HTTPDigestAuthHandler, build_opener, install_opener
# Project modules
import consts

#for dummy ops
import os
import random


def DownloadImage(urladdr):
    """Receive image from server"""
    try:
        imagedata = urlopen(urladdr)
        image = imagedata.read()
        imagedata.close()
    except:
        raise Exception("Cannot download image")
    return image


def SendMetadata(urladdr, meta):
    """Generic metadata transmission"""
    try:
        print meta
        answer = urlopen(urladdr, urlencode(meta)).read()
        print answer
        
        return ParseMeta(answer)
    except:
        print 'Cannot connect to internet'

        
def SendLogin(username, password):
    """Authenticate with HTTP Digest Authentication,
    then receive user ID"""

    # Use HTTP digest authentication
    authen = HTTPDigestAuthHandler()
    authen.add_password(realm = consts.REALM,
        uri = consts.URL_REQ_LOGIN,
        user = username.encode('utf-8'),
        passwd = md5(password.encode('utf-8')+username.encode('utf-8')\
            +consts.REALM).hexdigest())
    install_opener(build_opener(authen))
    urlopen(consts.URL_REQ_LOGIN)

    print username
    print password
    # Take return value to be user ID, limit return value to 32 characters for protection
    answer = urlopen(consts.URL_REQ_LOGIN).read()
    print answer
    return ParseMeta(answer)


def ParseMeta(meta):
    """Separate returned metadata into dictionary"""
    lines = meta.split('\r\n')
    parsed = {}
    for item in lines:
        if item != '':
            parts = item.partition('=')
            parsed[parts[0]] = parts[2]
    print parsed
    return parsed
