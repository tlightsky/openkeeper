#!/bin/bash


# Must be root
if test "`/usr/bin/id -u`" != 0 ; then
    echo "$0: You must be root to run this script" >& 2
    exit 1
fi
DEBUG=1

CONFIG_PATH=config
if [ ! -d $CONFIG_PATH ] ; then
	echo "没有配置文件，调用配ok-config命令置"
	ok-config
fi

cd $(dirname $0)
#请务必在下面填上自己的网关地址、账号和密码
#网关地址:
default_eth=`cat $CONFIG_PATH/eth`
ppp_eth=ppp0

#用户名:
username=`cat $CONFIG_PATH/user`
#密码:
password=`cat $CONFIG_PATH/pass`

count=0
maxcount=2  #拨号失败重试次数
echo $username > Netkeeper.dat
pppoe-stop > /dev/null 2>&1
echo "尝试使用用户名$username,网卡$default_eth"
until test -n "`ifconfig | grep ppp`"
do
	if [ "$count" != 0 ]
		then echo "第$count次登录失败"
	fi
	realusername=`./dialnetkeeper`
	realusername=${realusername//\"/\\\"}
	cp pppoe.conf pppoe.conf-tmp
	cp pap-secrets pap-secrets-tmp
	#"0605852@cqupt"	*	"hqhqhq"
	#USER='0605852@cqupt'
	echo "ETH=$default_eth" >> pppoe.conf-tmp
	echo "USER='\"$realusername\"'" >> pppoe.conf-tmp
	echo "\"$realusername\"	*	\"$password\"" >> pap-secrets-tmp
	#set s//\\/
	cp pppoe.conf-tmp /etc/ppp/pppoe.conf
	cp pap-secrets-tmp /etc/ppp/pap-secrets
	pppoe-start #> /dev/null
	if test -n "`ifconfig|grep ppp`" ; then
		break
	else
		count=`expr $count + 1`
		if [ "$count" -eq "$maxcount" ]
		then echo 达到最大失败次数，请检查账户密码信息，或者稍后再试
		exit 0
		fi
		sleep 1
	fi
done
echo 登录成功
rm Netkeeper.dat

tmp_ip=`/sbin/ifconfig $ppp_eth|awk "(/[0-9]?[0-9]?[0-9]\.[1-9]?[1-9]?[1-9]\.[0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]/) {print}"|cut -d: -f2`
tmp_ip=${tmp_ip%% *}
ppp_ip=$tmp_ip
# 添加外网路由
route add default gw $ppp_ip -e $ppp_eth

gateway_ip=`/sbin/route -n|grep 0.0.0.0.*172|cut -c17-28`
if test -n $gateway_ip ; then
	echo "为网关$gateway_ip添加内网路由..."
	route del -net 172.0.0.0/8 > /dev/null 2>&1
	route del -net 202.202.0.0/16 > /dev/null 2>&1
	route add -net 172.0.0.0/8 gw $gateway_ip -e $default_eth > /dev/null 2>&1
	route add -net 202.202.0.0/16 gw $gateway_ip -e $default_eth > /dev/null 2>&1
fi

echo 处理结束
exit 0
