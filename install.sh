#!/bin/bash
SUDOER=sudo

INSTALL_PATH=/usr/local/openkeeper
MYDIR=`dirname $0`
cd $MYDIR

$SUDOER rp-pppoe-3.10/ok-go
$SUDOER cp pppoe-connect /usr/sbin/

cd diallinux_v1.0_src_a/
make
cp dialnetkeeper ../
make clean
cd ..

#/usr/bin/ok-config

if [ -d "$INSTALL_PATH" ]
then
	echo "覆盖安装"
	$SUDOER rm -rf $INSTALL_PATH
else
	echo "初次安装"
fi
$SUDOER mkdir $INSTALL_PATH
$SUDOER cp * $INSTALL_PATH

$SUDOER ln -sf $INSTALL_PATH/ok /usr/bin/ok 
$SUDOER ln -sf $INSTALL_PATH/ok-stop /usr/bin/ok-stop 
$SUDOER ln -sf $INSTALL_PATH/ok-config /usr/bin/ok-config

echo "完成安装，使用ok拨号，使用ok-stop挂断，ok-config进行设置"

