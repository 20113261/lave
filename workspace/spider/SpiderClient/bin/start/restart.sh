#!/bin/bash
if [ ! -n "$1" ] ;then
    echo "must need param slave_group like:routine,test,online_c,online_c"
    exit 1
fi
slave_group=$1

CURR_PATH=`cd $(dirname $0);pwd;`
cd $CURR_PATH

sh kill.sh

sleep 5
sh start5.sh ${slave_group}

nohup stdbuf -oL python bossStatus.py  2>&1 | cronolog /search/spider_log/logs/rotation/%Y%m%d/restart.%Y%m%d_%H.log &

