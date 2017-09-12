#!/usr/bin/env python  

if [ ! -n "$1" ] ;then
    echo "must need param slave_group like:routine,test,online_c,online_c"
    exit 1
fi

source ./slave_process.sh

# 获取进程数
get_process_size
proce_size=$?

python kill.py $proce_size
