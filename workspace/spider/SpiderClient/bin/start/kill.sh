#!/usr/bin/env python
CURR_PATH=`cd $(dirname $0);pwd;`
echo $CURR_PATH
cd $CURR_PATH
source ./slave_process.sh
# 获取进程数
get_process_size ${slave_group}
proce_size=$?

python kill.py ${proce_size}
