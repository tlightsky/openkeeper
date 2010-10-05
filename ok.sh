#!/bin/bash


# Must be root
if test "`/usr/bin/id -u`" != 0 ; then
    echo "$0: You must be root to run this script" >& 2
    exit 1
fi

cd $(dirname $0)
#请务必在下面填上自己的网关地址、账号和密码
#网关地址:
default_eth=eth0
ppp_eth=ppp0

#用户名:
username=`cat user`
#密码:
password=`cat pass`

count=0
maxcount=2  #拨号失败重试次数
echo $username > Netkeeper.dat
pppoe-stop > /dev/null 2>&1
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

#route add deafult gw 113.251.216.1 -e ppp0
#route add -net 172.0.0.0 netmask 255.0.0.0 gw $gateway
#route add -net 202.202.0.0 netmask 255.255.0.0 gw $gateway
#route add -net 211.83.0.0 netmask 255.255.0.0 gw $gateway
#route add -net 202.38.97.230 netmask 255.255.255.255 gw $gateway	#交大更新源 ftp.sjtu.edu.cn
#route add -net 202.38.93.66 netmask 255.255.255.255 gw $gateway		#科大更新源 debian.ustc.edu.cn
#route add -net 202.115.22.208 netmask 255.255.255.255 gw $gateway	#电子科大更新源 ubuntu.usetc.edu.cn
#route add -net 202.112.154.58 netmask 255.255.255.255 gw $gateway	#北交更新源 mirror.njtu.edu.cn
#route add -net 60.191.81.189 netmask 255.255.255.255 gw $gateway	#163镜像 mirrors.163.com
#route add -net 115.238.55.232 netmask 255.255.255.255 gw $gateway	#中标普华镜像 mirror.lupaworld.com
#route add -net 219.153.42.248 netmask 255.255.255.255 gw $gateway	#net9镜像 mirror9.net9.org
echo 处理结束
exit 0
