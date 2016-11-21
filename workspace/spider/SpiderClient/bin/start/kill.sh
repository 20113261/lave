#!/bin/sh   

#keys=`(ps -ef |grep "slave" |grep -v "grep") | awk '{print $2}'`

#for key in ${keys[*]}
#do
#    kill -9 $key
#done


ps -ef | grep 'slave' | grep -v 'grep' | awk '{print $2}' | xargs kill -9

sleep 3

ps -ef | grep 'bossStatus.py' | grep -v 'grep' | awk '{print $2}' | xargs kill -9
