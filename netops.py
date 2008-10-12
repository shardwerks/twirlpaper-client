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


class NetError(Exception):
	"""Internet connection error

	This exception does nothing"""
	pass



def DownloadImage():
        # Receive image and metadata
        # save imageid, imagerating, userrating, imageinfo, imageurl, imagetags
        # return a tmp config so update doesn't collide with user op?

        #dummy op
    try:
        fchoose = random.choice(os.listdir("C:\\Documents and Settings\\New User\\Desktop\\Twirlpaper\\Wallpapers\\JPG"))
        f = open("C:\\Documents and Settings\\New User\\Desktop\\Twirlpaper\\Wallpapers\\JPG\\"+fchoose, 'rb')
        #fchoose = random.choice(os.listdir("C:\\Documents and Settings\\New User\\Desktop\\Twirlpaper\\Wallpapers\\Test"))
        #f = open("C:\\Documents and Settings\\New User\\Desktop\\Twirlpaper\\Wallpapers\\Test\\"+fchoose, 'rb')
        g = f.read()
        f.close()
    except:
        raise #Exception("Cannot get files from hard drive")
    return g


def SendMetadata(urladdr, meta):
    # Send metadata
    try:
        print meta
        answer = urlopen(urladdr, urlencode(meta)).read()
        print answer
        return answer
    except NetError:
        print 'Cannot connect to internet'

        
def SendLogin(username, password):
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
    return answer
