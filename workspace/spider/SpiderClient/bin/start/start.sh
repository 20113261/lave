#!/bin/bash

CURR_PATH=`cd $(dirname $0);pwd;`
cd $CURR_PATH
source ./start_check.sh
check

if [ ! -n "$1" ] ;then
    echo "需要指定一个参数，slave_group 值为其中一个:routine,test,online_c,online_d"
    exit 1
fi

slave_group=$1

source ./slave_process.sh


# 取SpidrClient目录
cd ../../
ROOT_PATH=`pwd`
cd $CURR_PATH

# 设置环境变量:PYTHONPATH,CONFIG_FILE
export PYTHONPATH=${ROOT_PATH}/lib:${ROOT_PATH}/bin
export CONFIG_FILE=${ROOT_PATH}/conf/slave.${slave_group}.ini
HOST=$(hostname)

echo "PYTHONPATH=$PYTHONPATH"
echo "CONFIG_FILE=$CONFIG_FILE"

# 获取进程数
get_process_size ${slave_group}
proce_size=$?

start_port=8089

for ((i=${start_port};i<$[ ${start_port} + ${proce_size} ];i++ ))
do
    echo "create slave $i"
    { nohup stdbuf -oL python ../slave.py $i 2>&3 | nohup cronolog /search/spider_log/rotation/%Y%m%d/%Y%m%d%H/slave.log_${i}.%Y%m%d%H.${HOST}.std ;} 3>&1 | nohup cronolog /search/spider_log/rotation/%Y%m%d/%Y%m%d%H/slave.log_${i}.%Y%m%d%H.${HOST}.err &
    echo $! 
done