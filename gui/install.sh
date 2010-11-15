#!/bin/bash
INSTALL_PATH=/usr/local/openkeeper
cd $(dirname $0)
SUDOER=sudo

if [ ! -d $INSTALL_PATH/gui ] ; then
	$SUDOER mkdir $INSTALL_PATH/gui #> /dev/null 2>&1
fi
$SUDOER cp * $INSTALL_PATH/gui -r && echo 'Install Success'
$SUDOER ln -sf $INSTALL_PATH/gui/ok-gui.sh /usr/bin/ok-gui
echo 'Please use ok-gui to start openkeeper gui.'
