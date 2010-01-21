# -*- coding: utf-8 -*-

from distutils.core import setup
#import py2exe
from py2exe.build_exe import py2exe
import os


# From http://www.py2exe.org/index.cgi/BetterCompression
#--------------------------------------------------------------------------
#
# Define our own command class based on py2exe so we can perform some
# customizations, and in particular support UPXing the binary files.
#
#--------------------------------------------------------------------------

class Py2exeUPX(py2exe):

    def initialize_options(self):
        # Add a new "upx" option for compression with upx
        py2exe.initialize_options(self)
        self.upx = 1

    '''
    def copy_file(self, *args, **kwargs):
        # Override to UPX copied binaries.
        (fname, copied) = result = py2exe.copy_file(self, *args, **kwargs)

        basename = os.path.basename(fname)
        if (copied and self.upx and
            (basename[:6]+basename[-4:]).lower() != 'python.dll' and
            basename in ('_ctypes.pyd', '_hashlib.pyd', '_socket.pyd', 'bz2.pyd', 'select.pyd',
                'unicodedata.pyd', 'PIL._imaging.pyd', 'wx._controls_.pyd', 'wx._core_.pyd',
                'wx._gdi_.pyd', 'wx._misc_.pyd', 'wx._windows_.pyd', 'wxmsw28uh_adv_vc.dll',
                'wxmsw28uh_html_vc.dll', 'wxbase28uh_vc.dll', 'wxbase28uh_net_vc.dll',
                'wxmsw28uh_core_vc.dll')):
            #fname[-4:].lower() in ('.pyd', '.dll')):
            os.system('upx --best "%s"' % os.path.normpath(fname))
        return result
    '''

    def patch_python_dll_winver(self, dll_name, new_winver=None):
        # Override this to first check if the file is upx'd and skip if so
        if not self.dry_run:
            if not os.system('upx -qt "%s" >nul' % dll_name):
                if self.verbose:
                    print "Skipping setting sys.winver for '%s' (UPX'd)" % \
                          dll_name
            else:
                py2exe.patch_python_dll_winver(self, dll_name, new_winver)
                # We UPX this one file here rather than in copy_file so
                # the version adjustment can be successful
                if self.upx:
                    os.system('upx --best "%s"' % os.path.normpath(dll_name))


setup(	cmdclass = {'py2exe': Py2exeUPX},
		options = {"py2exe" : {"dll_excludes" : ["w9xpopen.exe", "MSVCP90.dll"],
							# Can't use the compressed/optimize with bundle, causes icons to disappear
							#"compressed" : 1,
							#"optimize" : 2,
							"bundle_files" : 1,
							# From http://www.py2exe.org/index.cgi/OptimizingSize
							"excludes" : ['_ssl', 'doctest', 'pdb', 'unittest', 'difflib', 'inspect']
							}
				},
		windows = [{"script" : "twirlpaper.py",
				"icon_resources": [(1, "twirldesktop.ico")]
			}],
		name = 'Twirlpaper Wallpaper Changer',
		version = '0.1.0',
		description = 'Automatic internet wallpaper retriever and changer',
		author = 'Shultz Wang',
		author_email = 'info@twirlpaper.com',
		url = 'http://www.twirlpaper.com',
		license = 'Copyright © 2009 Leo Engine, all rights reserved',
		zipfile = None
)
