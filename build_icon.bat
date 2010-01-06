cd Media
pngcrush.exe -d crushed -reduce -brute -fix *.png
move /y crushed\*.* .
encode_bitmaps.py
move /y icons.py ..
cd ..
