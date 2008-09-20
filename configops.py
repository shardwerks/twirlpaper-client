"""Configuration data operations

Config data is stored as a dictionary
Default config file is:
        "login"                         =       "guest"                                 Username, owned by GUIOps
        "userid"                        =       "0000000000000000"              From server, owned by GUIOps
        "rememberme"            =       False                                   Store username/userif, owned by GUIOps
        "imageid"                       =       "0000000000000000"              From server, owned by NetOps
        "nextchangetime"        =       0.0             Next update time, owned by GUIOps
        "imagerating"           =       1               Image rating from server, owned by NetOps
        "userrating"            =       0               Image rating from user (0 is unrated), owned by GUIOps
        "imageinfo"                     =       ""              Image info from server, owned by NetOps
        "imageurl"                      =       ""              Image URL from server, owned by NetOps
        "imagetags"                     =       ""              Image tags from submmitter, owned by NetOps
        "subscribedtags"        =       ""              Tags subscribed to by user, owned by GUIOps
        "ratedatleast"          =       1               Minimum image rating, owned by GUIOps
        "percent"                       =       20              Percentage image unrated by user, owned by GUIOps
        "changeevery"           =       3600    Time between updates, owned by GUIOps
        "url"                           =       ""                              Image source URL, hardcoded

Unmodified config file:
                        data = {"login":"guest",
                                "userid":"0000000000000000",
                                "rememberme":False,
                                "imageid":"0000000000000000",
                                "nextchangetime":0.0,
                                "imagerating":1,
                                "userrating":0,
                                "imageinfo":"",
                                "imageurl":"",
                                "imagetags":"",
                                "subscribedtags":"",
                                "ratedatleast":1,
                                "percentnew":20,
                                "changeevery":3600,
                                "url":"",
                                }
"""


__author__              = "Shultz Wang"
__version__             = "Revision 0.1"
__date__                = "Tuesday, August 07, 2007 22:59:05"
__copyright__   = "Copyright (c) 2007 Shultz Wang"


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
            data = {"login":"greatone",
                "userid":"0000000000001234",
                "rememberme":True,
                "imageid":"0000000000000000",
                "nextchangetime":0.0,
                "imagerating":3,
                "userrating":1,
                "imageinfo":"Submitted By: Dmitri,\nLicense: Public Domain",
                "imageurl":"http://www.google.com/search?as_q=wallpaper",
                "imagetags":"surfer tide arms weird gogo jumping hot scorch sun waves sand beach slow fast sleep swim bikini bounce bop",
                "subscribedtags":"run skip hop dance twirl",
                "ratedatleast":1,
                "percentnew":20,
                "changeevery":3600,
                "url":"",
                }
        dict.__init__(self, data)

    def Load(self, twirlpath):
        """Load configuration data from a predetermined file
        (config.dat) in the executable's directory.  Read
        errors are ignored."""

        try:
            fconfig = open(twirlpath + "config.dat","rb")
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
            fconfig = open(twirlpath + "config.dat","wb")
            try:
                configtmp = self.copy()
                if not self["rememberme"]:
                    configtmp["login"] = "guest"
                    configtmp["userid"] = "0000000000000000"
                configdat = codecops.Encode(configtmp)
                fconfig.write(configdat)
            finally:
                fconfig.close()
        except IOError:
            raise ConfigWriteError
