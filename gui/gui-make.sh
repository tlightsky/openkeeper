#!/bin/bash

#python ~/source/PyInstaller/Makespec.py --upx main.py #--onefile 
#python ~/source/PyInstaller/Build.py main.spec
#mv dist/main dist/ok-gui.bin
#cp install.sh dist/install.sh

#!/bin/bash
INSTALL_PATH=/usr/local/openkeeper
cd $(dirname $0)
SUDOER=sudo
RELEASE_PATH=openkeeper-gui-1.0

rm -rf $RELEASE_PATH
mkdir $RELEASE_PATH

cp -rf gui/* $RELEASE_PATH
rm $RELEASE_PATH/ui/*.pyc
rm $RELEASE_PATH/ui/*.ui
rm $RELEASE_PATH/util/*.pyc

echo tar cfz $RELEASE_PATH.tar.gz $RELEASE_PATH
tar cfz $RELEASE_PATH.tar.gz $RELEASE_PATH
rm -r $RELEASE_PATH
