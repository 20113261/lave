#! /usr/bin/env
#coding=utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

mt_ip_dict = {
    "172.16.12.196": "43.241.214.233", 
    "172.16.12.198": "43.241.223.210", 
    "172.16.25.127": "43.241.214.239", 
    "172.16.13.168": "43.241.210.73", 
    "172.16.25.89": "43.241.215.249", 
    "172.16.19.101": "103.37.166.248", 
    "172.16.19.100": "43.241.214.249", 
    "172.16.181.105": "103.37.161.249", 
    "172.16.181.103": "43.241.223.234", 
    "172.16.8.249": "43.241.212.98", 
    "172.16.16.86": "43.241.221.237", 
    "172.16.16.87": "103.37.151.245", 
    "172.16.17.111": "103.37.147.231", 
    "172.16.19.199": "43.241.221.174", 
    "172.16.13.221": "103.37.147.243", 
    "172.16.18.202": "103.37.149.119", 
    "172.16.18.201": "43.241.216.206", 
    "172.16.22.121": "43.241.217.205", 
    "172.16.22.122": "103.37.150.145", 
    "172.16.14.153": "103.37.151.63", 
    "172.16.9.158": "103.37.162.244", 
    "172.16.19.116": "103.37.149.232", 
    "172.16.24.122": "43.241.211.198", 
    "172.16.18.93": "103.37.149.247", 
    "172.16.18.92": "43.241.218.231", 
    "172.16.11.203": "103.37.146.157", 
    "172.16.11.201": "43.241.219.43", 
    "172.16.17.198": "43.241.213.157", 
    "172.16.17.199": "43.241.222.224", 
    "172.16.184.211": "43.241.220.121", 
    "172.16.15.94": "103.37.148.243", 
    "172.16.20.225": "103.37.145.150", 
    "172.16.20.220": "43.241.220.147", 
    "172.16.15.93": "43.241.217.223", 
    "172.16.17.93": "43.241.212.248", 
    "172.16.13.202": "43.241.218.176", 
    "172.16.17.96": "103.37.164.251", 
    "172.16.10.216": "43.241.213.74", 
    "172.16.10.218": "43.241.221.133", 
    "172.16.23.90": "43.241.213.248", 
    "172.16.16.198": "103.37.151.59", 
    "172.16.16.193": "43.241.215.86", 
    "172.16.181.131": "103.37.145.248", 
    "172.16.15.193": "43.241.215.37", 
    "172.16.15.213": "103.37.148.156", 
    "172.16.14.203": "103.37.150.227", 
    "172.16.14.201": "43.241.208.39", 
    "172.16.7.110": "103.37.144.252", 
    "172.16.184.85": "43.241.214.250", 
    "172.16.182.86": "103.37.150.245", 
    "172.16.182.85": "43.241.219.246", 
    "172.16.12.99": "103.37.163.250", 
    "172.16.12.98": "43.241.211.250", 
    "172.16.23.91": "103.37.165.250", 
    "172.16.10.104": "103.37.146.238", 
    "172.16.10.103": "103.37.147.249", 
    "172.16.9.202": "103.37.162.97", 
    "172.16.18.173": "43.241.216.68", 
    "172.16.7.184": "103.37.161.202", 
    "172.16.18.175": "103.37.149.106", 
    "172.16.184.208": "103.37.145.235", 
    "172.16.15.202": "43.241.217.145", 
    "172.16.21.96": "43.241.208.251", 
    "172.16.7.109": "103.37.160.246", 
    "172.16.14.213": "103.37.144.76", 
    "172.16.7.107": "43.241.222.226", 
    "172.16.24.92": "43.241.211.251", 
    "172.16.24.93": "103.37.144.245", 
    "172.16.12.149": "103.37.163.115", 
    "172.16.9.112": "43.241.210.249", 
    "172.16.22.88": "43.241.220.244", 
    "172.16.8.127": "43.241.212.250", 
    "172.16.16.138": "103.37.160.45", 
    "172.16.11.90": "43.241.209.250", 
    "172.16.20.97": "103.37.167.247", 
    "172.16.6.128": "43.241.216.249", 
    "172.16.21.151": "43.241.208.57", 
    "172.16.23.108": "103.37.148.222", 
    "172.16.13.96": "43.241.210.248", 
    "172.16.13.95": "43.241.210.247", 
    "172.16.19.207": "103.37.166.162", 
    "172.16.11.156": "43.241.209.108", 
    "172.16.16.129": "43.241.219.96", 
    "172.16.12.100": "103.37.146.216", 
    "172.16.183.85": "43.241.213.249", 
    "172.16.183.86": "103.37.144.246", 
    "172.16.23.130": "103.37.165.153", 
    "172.16.14.148": "43.241.218.187", 
    "172.16.17.183": "103.37.164.23", 
    "172.16.20.166": "103.37.167.239",
    "10.135.58.0":"123.207.97.71",
    "10.105.114.152":"115.159.99.237",
    "10.105.106.70":"115.159.29.69",
    "10.105.115.153":"182.254.152.109",
    "10.141.126.207":"123.206.52.187",
    "10.135.27.188":"119.29.217.80",
    "10.135.30.103":"123.207.85.153",
    "10.135.37.5":"119.29.205.37",
    "10.105.105.249":"115.159.148.30",
    "10.135.37.34":"119.29.239.203",
    "10.141.139.247":"123.206.61.230",
    "10.105.47.33":"182.254.246.206",
    "10.135.42.156":"119.29.161.208",
    "10.105.108.217":"115.159.185.26",
    "10.135.36.196":"123.207.98.220",
    "10.135.30.75":"119.29.181.191",
    "10.141.112.177":"123.206.49.153",
    "10.135.42.86":"123.207.89.44",
    "10.135.47.221":"123.207.95.238",
    "10.135.31.25":"123.207.120.211",
    "10.135.19.61":"123.207.99.180",
    "10.135.27.118":"123.207.87.183",
    "10.105.65.88":"115.159.47.68",
    "10.141.139.203":"123.206.78.98",
    "10.141.140.78":"123.206.56.150",
    "10.141.140.143":"123.206.21.232",
    "10.141.140.26":"123.206.95.51",
    "10.141.139.252":"123.206.87.20",
    "10.105.69.194":"182.254.136.206",
    "10.135.34.242":"119.29.38.76",
    "10.135.42.54":"123.207.101.244",
    "10.105.91.105":"115.159.155.196",
    "10.135.62.160":"123.207.89.48",
    "10.141.140.164":"123.206.74.113",
    "10.141.140.50":"123.206.65.123",
    "10.105.96.58":"182.254.210.116",
    "10.135.36.232":"123.207.82.132",
    "10.135.45.75":"123.207.89.88",
    "10.135.37.142":"119.29.239.37",
    "10.141.139.255":"123.206.22.170",
    "10.141.112.99":"123.206.53.97",
    "10.135.25.153":"123.207.100.224",
    "10.135.47.20":"123.207.99.32",
    "10.105.67.75":"182.254.139.123",
    "10.141.139.207":"123.206.78.77",
    "10.135.36.68":"119.29.27.32",
    "10.135.30.71":"123.207.101.91",
    "10.135.28.38":"119.29.120.61",
    "10.141.140.152":"123.206.17.217",
    "10.105.122.2":"115.159.84.184",
    "10.135.40.250":"119.29.230.123",
    "10.135.31.239":"123.207.99.62",
    "10.105.98.153":"115.159.145.167",
    "10.105.119.21":"182.254.158.118",
    "10.135.50.118":"119.29.234.106",
    "10.141.140.172":"123.206.91.234",
    "10.105.77.224":"115.159.117.62",
    "10.135.37.10":"123.207.122.35",
    "10.135.42.12":"119.29.87.16",
    "10.141.140.118":"123.206.61.55",
    "10.105.79.85":"115.159.148.45",
    "10.135.31.236":"119.29.8.183",
    "10.141.140.19":"123.206.68.61",
    "10.141.140.72":"123.206.75.147",
    "10.141.140.95":"123.206.23.230",
    "10.135.35.244":"123.207.89.229",
    "10.135.29.168":"119.29.229.243",
    "10.141.140.155":"123.206.80.147",
    "10.135.57.151":"123.207.119.50",
    "10.135.38.117":"119.29.74.92",
    "10.135.33.243":"119.29.190.151",
    "10.135.39.138":"123.207.118.114",
    "10.141.83.191":"123.206.69.95",
    "10.141.140.11":"123.206.94.151",
    "10.135.43.144":"123.207.101.37",
    "10.135.60.42":"119.29.218.222",
    "10.105.95.32":"115.159.84.227",
    "10.135.31.108":"123.207.118.42",
    "10.105.100.76":"115.159.72.195",
    "10.141.140.29":"123.206.41.212",
    "10.135.10.129":"123.207.118.164",
    "10.135.22.114":"123.207.121.127",
    "10.135.30.183":"123.207.91.140",
    "10.135.38.103":"123.207.82.19",
    "10.105.101.178":"115.159.64.188",
    "10.141.139.202":"123.206.64.228",
    "10.135.39.236":"119.29.218.83",
    "10.135.20.129":"123.207.99.210",
    "10.135.46.137":"119.29.194.25",
    "10.135.34.49":"123.207.98.63",
    "10.141.139.190":"123.206.60.146",
    "10.141.140.122":"123.206.58.69",
    "10.135.4.135":"119.29.99.72",
    "10.105.125.248":"115.159.180.243",
    "10.135.32.231":"123.207.87.92",
    "10.141.97.10":"123.207.138.15",
    "10.135.31.78":"119.29.174.72",
    "10.105.96.241":"115.159.59.77",
    "10.135.40.29":"123.207.117.246",
    "10.135.34.88":"123.207.92.81",
    "10.135.3.24":"119.29.160.236",
    "10.141.140.9":"123.206.68.54",
    "10.135.1.145":"123.207.84.77",
    "10.105.69.51":"115.159.82.107",
    "10.105.78.134":"115.159.50.132",
    "10.141.108.92":"123.206.80.249",
    "10.105.101.63":"115.159.85.42",
    "10.135.29.249":"123.207.87.201",
    "10.135.47.55":"119.29.241.158",
    "10.135.39.201":"123.207.101.41",
    "10.141.78.142":"123.206.65.155",
    "10.105.102.72":"115.159.115.17",
    "10.105.64.166":"115.159.97.206",
    "10.141.140.111":"123.206.45.158",
    "10.135.37.221":"119.29.216.205",
    "10.135.3.62":"123.207.121.68",
    "10.141.140.70":"123.207.137.226",
    "10.135.35.152":"119.29.101.32",
    "10.105.91.179":"182.254.244.210",
    "10.135.0.56":"123.207.85.172",
    "10.141.140.12":"123.206.50.146",
    "10.105.95.44":"115.159.160.201",
    "10.141.140.42":"123.206.63.187",
    "10.141.122.19":"123.206.20.136",
    "10.141.64.62":"123.206.46.109",
    "10.135.36.215":"119.29.232.217",
    "10.135.2.67":"119.29.143.196",
    "10.135.22.238":"123.207.117.24",
    "10.135.30.120":"119.29.181.23",
    "10.141.139.191":"123.206.61.154",
    "10.135.50.112":"123.207.93.206",
    "10.141.121.253":"123.206.51.209",
    "10.105.114.141":"182.254.220.214",
    "10.135.42.60":"123.207.97.240",
    "10.105.107.57":"115.159.190.100",
    "10.135.28.96":"119.29.243.93",
    "10.105.70.150":"115.159.181.21",
    "10.135.37.32":"123.207.119.159",
    "10.135.32.16":"119.29.57.196",
    "10.135.28.78":"119.29.245.77",
    "10.135.45.25":"123.207.98.216",
    "10.135.33.202":"123.207.117.57",
    "10.135.44.190":"123.207.117.76",
    "10.135.38.166":"119.29.57.19",
    "10.135.2.34":"119.29.206.226",
    "10.135.34.125":"119.29.229.125",
    "10.135.38.156":"119.29.176.45",
    "10.105.125.196":"115.159.146.80",
    "10.135.45.209":"119.29.8.89",
    "10.141.139.210":"123.206.66.229",
    "10.141.139.229":"123.206.32.177",
    "10.135.46.75":"119.29.203.20",
    "10.135.20.160":"119.29.229.138",
    "10.105.75.43":"115.159.156.97",
    "10.135.25.235":"119.29.236.43",
    "10.105.19.155":"115.159.127.87",
    "10.141.140.73":"123.206.19.113",
    "10.141.140.99":"123.206.53.30",
    "10.135.24.71":"123.207.121.56",
    "10.105.98.78":"182.254.147.82",
    "10.105.118.89":"182.254.218.97",
    "10.141.139.248":"123.206.45.39",
    "10.105.91.27":"182.254.213.61",
    "10.135.36.82":"119.29.157.31",
    "10.135.63.42":"119.29.141.60",
    "10.105.117.38":"115.159.180.57",
    "10.135.63.49":"119.29.217.197",
    "10.135.36.229":"123.207.119.119",
    "10.135.61.168":"123.207.89.227",
    "10.135.27.192":"119.29.213.203",
    "10.105.80.75":"115.159.74.60",
    "10.105.116.118":"115.159.152.82",
    "10.105.85.79":"115.159.151.232",
    "10.105.78.144":"182.254.240.127",
    "10.135.31.203":"119.29.28.44",
    "10.141.113.221":"123.206.13.184",
    "10.135.2.149":"119.29.114.198",
    "10.135.44.202":"123.207.98.106",
    "10.135.27.94":"119.29.204.80",
    "10.105.91.60":"182.254.244.248",
    "10.105.124.97":"115.159.6.30",
    "10.135.28.201":"123.207.117.44",
    "10.105.118.253":"115.159.158.179",
    "10.105.107.171":"115.159.39.157",
    "10.105.111.158":"115.159.4.217",
    "10.135.53.8":"119.29.91.17",
    "10.135.36.10":"119.29.213.12",
    "10.141.140.0":"123.206.28.196",
    "10.105.65.78":"115.159.74.95",
    "10.135.31.209":"123.207.87.80",
    "10.141.140.104":"123.206.47.48",
    "10.141.140.7":"123.206.80.171",
    "10.135.46.228":"119.29.241.84",
    "10.141.139.237":"123.206.13.17",
    "10.141.86.154":"123.206.51.231",
    "10.105.78.195":"115.159.93.31",
    "10.135.33.128":"119.29.142.220",
    "10.135.46.159":"123.207.84.180",
    "10.105.117.239":"182.254.221.161",
    "10.141.139.245":"123.206.74.107"
    }