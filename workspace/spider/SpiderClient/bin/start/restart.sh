#!/bin/bash

CURR_PATH=`cd $(dirname $0);pwd;`
cd $CURR_PATH

sh kill.sh
sh start5.sh 1

#nohup python bossStatus.py 1>../../logs/restart.log 2>../../logs/restart_err.log &
#nohup python bossStatus.py  2>&1 | cronolog ../../logs/rotation/%Y%m%d/restart.%Y%m%d_%H.log &
