#!/bin/bash
cd $(dirname $0)
SUDOER=sudo
$SUDOER python main.py
