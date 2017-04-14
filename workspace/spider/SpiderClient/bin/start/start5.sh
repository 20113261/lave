#!/bin/bash

CURR_PATH=`cd $(dirname $0);pwd;`
cd $CURR_PATH

export PYTHONPATH=$PYTHONPATH:../../lib
HOST=$(hostname)

# 增加 Spider 监控服务

if [ `/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"` == '10.10.246.77' ];then
	nohup stdbuf -oL python ../mioji/server/simple_server.py 2>&1 | cronolog /search/spider_monitor_log/rotation/%Y%m%d/%Y%m%d%H/slave_monitor.log.%Y%m%d%H &
	echo $! > monitor_pid
fi

for ((i=8089;i<$[ 8089 + $1 ];i++))
do
    nohup stdbuf -oL python ../slave.py  $i ../../conf/conf.ini 2>&1 | cronolog ../../logs/rotation/%Y%m%d/%Y%m%d%H/slave.log_${i}.%Y%m%d%H.${HOST} &
    echo $! > ../pid/pid$i
done


