"""Timer operations thread"""


__author__        = 'Shultz Wang'
__version__        = 'Revision 0.1'
__date__        = 'Tuesday, August 07, 2007 22:59:05'
__copyright__    = 'Copyright (c) 2007 Shultz Wang'


# Library modules
from time import time, sleep
from threading import Thread
# Project modules
import netops
import consts
from displayops import DisplayImage
from displayops import DisplayError


class TimerOps(Thread):
    """Timer for wallpaper change"""

    def __init__(self, parent, config, twirlpath):
        Thread.__init__(self)
        self._running = True
        self._parent = parent
        self._config = config
        self._twirlpath = twirlpath

    def run(self):
        """Run time check every second until stopped"""
        # Use time.sleep instead of threading.Timer since the latter will
        # spawn a separate thread and not be subject to waiting until
        # the countdown is complete before while-looping again
        while (self._running):
            sleep(1)
            #self._config['nextchange']=0
            self.TimeCheck()

    def Stop(self):
        """Stop running thread"""
        self._running = False


    def TimeCheck(self):
        """Check if the wait period has passed and update image,
        but hold off on update until GUI frame is closed so that user
        may complete any actions based on current image before image
        is changed, unless update initiated by used with New Wallpaper."""

        if time() > self._config['nextchange']\
            and not self._parent.frameops.IsShown():
            #and not self._parent.taskbarops.IsOpen:
            # Download new image to the executable's directory, and
            # name it wallpaper.jpg
            imagedata = netops.DownloadImage()
            #imagedata = netops.SendMetadata(consts.URL_REQ_IMAGE,{
            #        'username':self._config['username'].encode('utf-8'),
            #        'userid':self._config['userid']})
            # Parse returned data
            #self._config.update('imageid' = imagemeta['imageid'],
            #   'imagerating' = imagemeta['imagerating'],
            #   'userrating' = imagemeta['userrating'],
            #   'flagimage' = imagemeta['flagimage'],
            #   'imageinfo' = imagemeta['imageinfo'],
            #   ['imageurl'] = imagemeta['imageurl']
            #   ['imagetags'] = imagemeta['imagetags'])

            # Display new image
            try:
                DisplayImage(imagedata, self._twirlpath)
            except DisplayError:
                # Send error to server
                netops.SendMetadata(consts.URL_SEND_META,
                    {'username':self._config['username'].encode('utf-8'),
                    'userid':self._config['userid'], 'err':'disp'})

            # Update change time
            self._config['nextchange'] = time() + self._config['changeevery']
