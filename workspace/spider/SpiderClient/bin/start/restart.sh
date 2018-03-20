#!/bin/bash

CURR_PATH=`cd $(dirname $0);pwd;`
cd $CURR_PATH
source ./start_check.sh
check

if [ ! -n "$1" ] ;then
    echo "must need param slave_group like:routine, test, test1, online_c, online_d"
    exit 1
fi
slave_group=$1

sh kill.sh

sleep 5
sh start.sh ${slave_group}