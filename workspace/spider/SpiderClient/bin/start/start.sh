#!/bin/bash

CURR_PATH=`cd $(dirname $0);pwd;`
cd $CURR_PATH

export PYTHONPATH=$PYTHONPATH:../../lib
number=$1

HOST=$(hostname)

nohup stdbuf -oL python  ../slave.py $number ../../conf/conf.ini 2>&1 | cronolog ../../logs/rotation/%Y%m%d/%Y%m%d%H/slave.log_${number}.%Y%m%d%H.${HOST}&

