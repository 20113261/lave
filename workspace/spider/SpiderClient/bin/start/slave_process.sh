#!/bin/bash

function get_cpu_count(){
    cpu_count=`cat /proc/cpuinfo| grep 'physical id'| sort| uniq| wc -l`
    echo "cup count is ${cpu_count}"
    return ${cpu_count}
}

function get_process_size(){
    slave_group=$1
    echo "slave_group is ${slave_group}"
    get_cpu_count
    cpu_count=$?
    return ${cpu_count}
}
