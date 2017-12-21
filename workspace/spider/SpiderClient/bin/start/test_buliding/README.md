该文件路径 slave_develop_new/workspace/spider/SpiderClient/bin/start
机器路径  /home/SpiderClient/bin/start

该文件入口文件
运行  test.sh文件   即可调用测试工具，测试工具所运行爬虫均为该机器上的代码，确认更新后可以测试

测试工具需要运行四个参数
1.源名 source_name   类似于ctrip,expedia,igola等
2.类型 type 参数集[flight,roundflight,multiflight,hotel]
3.种类 参数集[ota,api]目前分为 ota源 和 api源，需要主动给出
4.任务类型 参数集[1，2，3] 飞机源支持 城市三字码任务可在ctrip的任务中取任务，参数 1
                   机场三字码任务可在expedia任务中取任务，参数 2
          酒店源  各自源有各自的任务  hotel任务  参数 3,即取上面所给source_name查找任务

该测试工具所用的代理工具不是机器上的代理，在Mini_test.py中有设置获取代理方法，后续可以统一修改。

所有源会在source表中检测，支持所有test环境开启的源，每次运行都会去source表中获取，如api源会自动获取测试环境auth信息

目前测试工具任务发送方式为并行方式。

获取任务流程
通过参数判断所需任务类型，获取10个任务，若任务数不足10个，则是当前源8天内所有任务去重后不足10个。

输出结果
输出结果最后会以CSV格式生成到当前文件内


