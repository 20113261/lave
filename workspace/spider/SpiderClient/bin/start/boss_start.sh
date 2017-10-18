#!/bin/bash

HOST=$(hostname)
port=$1
echo "create slave ${port}"
nohup stdbuf -oL python  ../slave.py ${port} 2>&1 | cronolog /search/spider_log/rotation/%Y%m%d/%Y%m%d%H/slave.log_${port}.%Y%m%d%H.${HOST}&