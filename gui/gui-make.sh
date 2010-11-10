#!/bin/bash

python ~/source/PyInstaller/Makespec.py --upx main.py #--onefile 
python ~/source/PyInstaller/Build.py main.spec
mv dist/main dist/ok-gui.bin
cp install.sh dist/install.sh
