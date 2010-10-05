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

echo "请输入用户名"
read U
$SUDOER rm user
echo $U > user
$SUDOER chown root.root user
$SUDOER chmod 700 user

echo "请输入密码"
read U
$SUDOER rm pass
echo $U > pass
$SUDOER chown root.root pass
$SUDOER chmod 700 pass

if [ -d "$INSTALL_PATH" ]
then
	echo "覆盖安装"
	$SUDOER rm -rf $INSTALL_PATH
else
	echo "初次安装"
fi
$SUDOER mkdir $INSTALL_PATH
$SUDOER cp * $INSTALL_PATH
