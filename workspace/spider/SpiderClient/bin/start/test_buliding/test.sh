#!/bin/bash

echo "-------任务启动-------"

export PYTHONPATH=/home/SpiderClient/bin:/home/SpiderCline/lib
export CONFIG_FILE=/home/SpiderClient/conf/slave.test.ini

echo "完成配置环境变量"
echo "PYTHONPATH=$PYTHONPATH"
echo "CONFIG_FILE=$CONFIG_FILE"

ResultData=`python Mini_test.py`

