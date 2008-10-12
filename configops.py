"""Configuration data operations

Config data is stored as a dictionary
Default config file is [changed by, max size]:
    'username'      =   'Guest'     Username [FrameOps, 32 chars]
    'userid'        =   '00000000000000000000000000000000'      From server [FrameOps, 32 chars]
    'imageid'       =   0           From server [NetOps, int]
    'nextchange'    =   0.0         Next update time [FrameOps, 32 chars]
    'imagerating'   =   1           Image rating from server [NetOps, int]
    'userrating'    =   0           User image rating (0=unrated) [FrameOps, int]
    'flagimage'     =   False       Image appropriateness flag [FrameOps, Bool]
    'imageinfo'     =   ''          Image info from server [NetOps, 128 chars]
    'imageurl'      =   ''          Image URL from server [NetOps, 128 chars]
    'imagetags'     =   ''          Image tags from submmitter [NetOps, 128 chars]
    'subscribedtags'=   ''          Tags subscribed to by user [FrameOps, 128 chars]
    'ratedatleast'  =   1           Minimum image rating [FrameOps, int]
    'percentnew'    =   20          Percentage image unrated by user [FrameOps, int]
    'changeevery'   =   3600        Time between updates [FrameOps, int]

Unmodified config file:
                        data = {'username':'Guest',
                                'userid':'00000000000000000000000000000000',
                                'imageid':0,
                                'nextchange':0.0,
                                'imagerating':1,
                                'userrating':0,
                                'flagimage':False,
                                'imageinfo':'',
                                'imageurl':'',
                                'imagetags':'',
                                'subscribedtags':'',
                                'ratedatleast':1,
                                'percentnew':20,
                                'changeevery':3600,
                                }

Modified config file:
            data = {'username':'greatone',
                'userid':'00000000000000000000000000001234',
                'imageid':12,
                'nextchange':0.0,
                'imagerating':3,
                'userrating':1,
                'flagimage':False,
                'imageinfo':'Submitted By: Dmitri,\nLicense: Public Domain',
                'imageurl':'http://www.google.com/search?as_q=wallpaper',
                'imagetags':'surfer tide arms weird gogo jumping hot scorch sun waves sand beach slow fast sleep swim bikini bounce bop',
                'subscribedtags':'run skip hop dance twirl',
                'ratedatleast':1,
                'percentnew':20,
                'changeevery':3600,
"""


__author__      = 'Shultz Wang'
__version__     = 'Revision 0.1'
__date__        = 'Tuesday, August 07, 2007 22:59:05'
__copyright__   = 'Copyright (c) 2007 Shultz Wang'


# Project modules
import codecops


class ConfigWriteError(Exception):
    """config.dat file write error

    This exception does nothing"""
    pass


class ConfigOps(dict):
    """Configuration data operations"""

    def __init__(self, data=None):
        if data == None:
            data = {'username':'Twirlguest',
                'userid':'00000000000000000000000000001234',
                'imageid':12,
                'nextchange':0.0,
                'imagerating':3,
                'userrating':1,
                'flagimage':False,
                'imageinfo':'Submitted By: Dmitri,\nLicense: Public Domain',
                'imageurl':'http://www.google.com/search?as_q=wallpaper',
                'imagetags':'surfer tide arms weird gogo jumping hot scorch sun waves sand beach slow fast sleep swim bikini bounce bop',
                'subscribedtags':'run skip hop dance twirl',
                'ratedatleast':1,
                'percentnew':20,
                'changeevery':3600,
                }
        dict.__init__(self, data)

    def Load(self, twirlpath):
        """Load configuration data from a predetermined file
        (config.dat) in the executable's directory.  Read
        errors are ignored."""

        try:
            fconfig = open(twirlpath + 'config.dat','rb')
            try:
                dict.__init__(self,
                    codecops.Decode(fconfig.read()))
            finally:
                fconfig.close()
        except IOError:
            # Ignore file read errors
            pass
        except IndexError:
            # Ignore file data errors
            pass


    def Save(self, twirlpath):
        """Save configuration data from a predetermined file
        (config.dat) in the executable's directory.  Write
        errors raise ConfigWriteError."""

        try:
            fconfig = open(twirlpath + 'config.dat','wb')
            try:
                configtmp = self.copy()
                fconfig.write(codecops.Encode(configtmp))
            finally:
                fconfig.close()
        except IOError:
            raise ConfigWriteError
