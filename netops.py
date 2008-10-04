"""Internet operations"""


__author__              = "Shultz Wang"
__version__             = "Revision 0.1"
__date__                = "Tuesday, August 07, 2007 22:59:05"
__copyright__   = "Copyright (c) 2007 Shultz Wang"


# Library modules
from hashlib import md5
from types import UnicodeType
from urllib2 import urlopen, HTTPDigestAuthHandler, build_opener, install_opener
# Project modules
import consts

#for dummy ops
import os
import random

"""
class NetOps():

        def __init__(self):
                self._url = ""
"""
        # Send request to server

class NetError(Exception):
	"""Internet connection error

	This exception does nothing"""
	pass



#       def DownloadImage(self):
def DownloadImage():
        # Receive image and metadata
        # save imageid, imagerating, userrating, imageinfo, imageurl, imagetags
        # return a tmp config so update doesn't collide with user op?

        #dummy op
    try:
        fchoose = random.choice(os.listdir("C:\\Documents and Settings\\New User\\Desktop\\Twirlpaper\\Wallpapers\\Test"))
        f = open("C:\\Documents and Settings\\New User\\Desktop\\Twirlpaper\\Wallpapers\\Test\\"+fchoose, 'rb')
        g = f.read()
        f.close()
    except:
        raise #Exception("Cannot get files from hard drive")
    return g


def SendMetadata(config, twirlconst):
    # Send username and metadata
    meta = {"username":config["username"].encode("utf-8"),
        "clientid":config["clientid"], "imageid":config["imageid"]}

    if twirlconst == consts.FLAG_IMAGE:
        meta["flagimage"] = True
    elif twirlconst == consts.RATE_1_STAR:
        meta["userrating"] = 1
    elif twirlconst == consts.RATE_2_STARS:
        meta["userrating"] = 2
    elif twirlconst == consts.RATE_3_STARS:
        meta["userrating"] = 3
    elif twirlconst == consts.RATE_4_STARS:
        meta["userrating"] = 4
    elif twirlconst == consts.RATE_5_STARS:
        meta["userrating"] = 5
    elif twirlconst == consts.ALL_META:
        for setting in ["nextchange", "userrating", "flagimage",
            "ratedatleast", "percentnew", "changeevery"]:
                meta[setting] = config[setting]
        meta["subscribedtags"] =\
            config["subscribedtags"].encode("utf-8")

    elif twirlconst == consts.DISPLAY_ERROR:
        meta["error"] = "display"

    try:
        print meta
        #***answer = urlopen(consts.URL_SEND_META, urlencode(quote_plus(meta))).read()
    except NetError:
        print "cannot connect to internet"

def SendLogin(username, password):
    # Use HTTP digest authentication
    authen = HTTPDigestAuthHandler()
    authen.add_password(realm = consts.REALM,
        uri = consts.URL_REQ_LOGIN,
        user = username.encode("utf-8"),
        passwd = md5(password.encode("utf-8")+consts.REALM).hexdigest())
    install_opener(build_opener(authen))
    urlopen(consts.URL_REQ_LOGIN)

    print username
    print password
    # Take return value to be client ID, limit return value to 32 characters for protection
    answer = urlopen(consts.URL_REQ_LOGIN).read()#[:32]
    print answer
    return answer
