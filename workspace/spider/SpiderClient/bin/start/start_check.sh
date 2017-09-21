#!/bin/bash

function check(){
    user=`whoami`
    echo "start user is ${user}"
    if [ ${user} != "spider" ]
    then
        echo "only spider can run me"
        slave_info=`mioji-host -a|xargs mioji-host -e`
        mioji-mail -m "dujun@mioji.com;peifei@mioji.com;hourong@mioji.com" -b "[通知][slave启动异常]" -c "slave ${slave_info} 使用${user}启动，应该是有spider启动"
        exit 1
    else
        echo ""
    fi
}
