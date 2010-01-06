from distutils.core import setup
import py2exe

setup(options = {"py2exe": {"dll_excludes": ["w9xpopen.exe", "MSVCP90.dll"],
							"bundle_files": 1}},
	windows=["twirlpaper.py"],
	zipfile = None
)
