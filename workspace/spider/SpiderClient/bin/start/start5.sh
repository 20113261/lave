#!/bin/bash

if [ ! -n "$1" ] ;then
    echo "must need param slave_group like:routine,test,online_c,online_c"
    exit 1
fi

slave_group=$1

source ./slave_process.sh

CURR_PATH=`cd $(dirname $0);pwd;`
cd $CURR_PATH

# 取SpidrClient目录
cd ../../
ROOT_PATH=`pwd`
cd $CURR_PATH

export PYTHONPATH=${ROOT_P}/lib:${ROOT_P}/bin:${RPPT_P}/bin/mioji
export CONFIG_FILE=${ROOT_P}/conf/slave.${slave_group}.ini
HOST=$(hostname)

echo "PYTHONPATH=$PYTHONPATH"
echo "CONFIG_FILE=$CONFIG_FILE"

# 获取进程数
get_process_size ${slave_group}
proce_size=$?

for ((i=8089;i<$[ 8089 + ${proce_size} ];i++ ))
do
    echo "create slave $i"
    { nohup stdbuf -oL python ../slave.py  $i ../../conf/conf.ini 2>&3 | nohup cronolog /search/spider_log/rotation/%Y%m%d/%Y%m%d%H/slave.log_${i}.%Y%m%d%H.${HOST}.std ;} 3>&1 | nohup cronolog /search/spider_log/rotation/%Y%m%d/%Y%m%d%H/slave.log_${i}.%Y%m%d%H.${HOST}.err &
    echo $! > ../pid/pid$i
done


