#!/bin/bash
cd $(dirname $0)
SUDOER=sudo
INSTALL_PATH=/usr/local/openkeeper
$SUDOER python $INSTALL_PATH/gui/main.py
