#!/bin/bash

# Must be root
if test "`/usr/bin/id -u`" != 0 ; then
	echo "$0: You must be root to run this script" >& 2
	exit 1
fi
MYDIR=`dirname $0`
cd $MYDIR
CONFIG_PATH=config
[[ ! -d $CONFIG_PATH ]]&&mkdir $CONFIG_PATH

function setconfig() {
	read U
	if [ -z $U ] ; then
		echo "选择(default:$2)"
		U=$2
	fi
	if [ -f $CONFIG_PATH/$1 ] ; then
		echo "覆盖原$1"
		rm $CONFIG_PATH/$1 > /dev/null 2>&1
	fi
	echo $U > $CONFIG_PATH/$1
	chown root.root $CONFIG_PATH/$1
	chmod 600 $CONFIG_PATH/$1
}

echo "请输入用户名"
setconfig user chongzhi

echo "请输入密码"
setconfig pass 123456

echo "请输入网关"
setconfig eth eth0

