#!/bin/bash
INSTALL_PATH=/usr/local/openkeeper
cd $(dirname $0)
SUDOER=sudo

$SUDOER cp ok-gui.bin $INSTALL_PATH/
