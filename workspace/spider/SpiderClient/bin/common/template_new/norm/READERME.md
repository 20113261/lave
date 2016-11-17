
解析标准化说明：

0：默认模式，默认值未NULL

c1：有关获取数字（price, tax, rest........）

c2：货币符号

c3：（未占用）

flight_no：1、MU123_CA768_HU213
           2、airchina 123_hainan airaways 6756
           3、中国国际航空 123_东风航空 434
           4、......


flight_corp：1、MU1214_HU3232
             2、air china_hainan airaways


bus/train(dept_id, dest_id, stop_id):
    1、'_'.原始站字符串列表


*time：1、......
       2、......


flight(dept_id, dest_id, stop_id):
    1、无需处理
    2、

dur：1、23h22min、1h3m_23h4min
     2、机场或城市三字码 + dept_ip, dest_id + ('city' or 'airport')


