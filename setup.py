from distutils.core import setup
import py2exe

setup(options = {"py2exe" : {"dll_excludes" : ["w9xpopen.exe", "MSVCP90.dll"],
							"compressed" : 1, "optimize" : 2, "bundle_files" : 1}
				},
	windows=[{"script" : "twirlpaper.py",
				"icon_resources": [(1, "twirldesktop.ico")]
			}],
	zipfile = None
)
