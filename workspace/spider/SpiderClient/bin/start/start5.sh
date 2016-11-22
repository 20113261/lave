#!/bin/bash

CURR_PATH=`cd $(dirname $0);pwd;`
cd $CURR_PATH

export PYTHONPATH=$PYTHONPATH:../../lib
HOST=$(hostname)

for ((i=8089;i<$[ 8089 + $1 ];i++))
do
    nohup stdbuf -oL python ../slave.py  $i ../../conf/conf.ini 2>&1 | cronolog ../../logs/rotation/%Y%m%d/%Y%m%d%H/slave.log_${i}.%Y%m%d%H.${HOST} &
    echo $! > ../pid/pid$i
done


