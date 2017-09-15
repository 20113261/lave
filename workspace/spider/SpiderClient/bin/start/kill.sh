#!/usr/bin/env python  
source ./slave_process.sh
# 获取进程数
get_process_size ${slave_group}
proce_size=$?

python kill.py ${proce_size}
