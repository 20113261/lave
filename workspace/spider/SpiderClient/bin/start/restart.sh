#!/bin/bash

CURR_PATH=`cd $(dirname $0);pwd;`
cd $CURR_PATH

sh kill.sh

sleep  5
sh start5.sh 10

nohup stdbuf -oL python bossStatus.py  2>&1 | cronolog /search/spider_log/logs/rotation/%Y%m%d/restart.%Y%m%d_%H.log &

