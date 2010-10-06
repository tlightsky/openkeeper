#!/bin/bash
SUDOER=sudo

# Must be root
if test "`/usr/bin/id -u`" != 0 ; then
	echo "$0: You must be root to run this script" >& 2
	exit 1
fi


INSTALL_PATH=/usr/local/openkeeper
MYDIR=`dirname $0`
cd $MYDIR

echo "请输入用户名"
read U
$SUDOER rm user > /dev/null 2>&1
echo $U > user
$SUDOER chown root.root user
$SUDOER chmod 700 user

echo "请输入密码"
read U
$SUDOER rm pass > /dev/null 2>&1
echo $U > pass
$SUDOER chown root.root pass
$SUDOER chmod 700 pass

