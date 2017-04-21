README

```
usage: ip2locationdemo [-h] [-s IP] [-i IPS] [-o OUT]

IP address to location

optional arguments:
  -h, --help  show this help message and exit
  -s IP       search ip to location.
  -i IPS      search ip to location from file.
  -o OUT      search ip to location from file and store result to file.

```

IPS File LIKE 多个IP保存在文本文件里，格式如下:

  ```
80.82.78.38
120.55.242.159
121.196.225.104
94.102.49.174
47.90.92.26
118.178.228.154
116.62.176.205
59.110.6.177
  ```

Show on Screen 屏幕输出：

  ```
80.82.78.38     塞舌尔群岛(geoip)       荷兰,荷兰(ipip) 荷兰,阿姆斯特丹Ecatel公司(cz88)
116.62.176.205  中国,北京市,北京(geoip) 中国,浙江,杭州(ipip)    辽宁省,铁通(cz88)
121.196.225.104 中国,浙江省,杭州(geoip) 中国,浙江,杭州(ipip)    浙江省杭州市,阿里巴巴网络有限公司(cz88)
120.55.242.159  中国,浙江省,杭州(geoip) 中国,浙江,杭州(ipip)    浙江省杭州市,阿里云BGP数据中心(cz88)
94.102.49.174   塞舌尔群岛(geoip)       荷兰,荷兰(ipip) 荷兰, CZ88.NET(cz88)
118.178.228.154 中国,浙江省,杭州(geoip) 中国,浙江,杭州(ipip)    浙江省杭州市,阿里云计算有限公司(cz88)
59.110.6.177    中国,浙江省,杭州(geoip) 中国,北京,北京(ipip)    广东省深圳市,英达通信(cz88)
47.90.92.26     香港(geoip)     中国,香港(ipip) 香港,阿里云数据中心(cz88)
  ```

Save to CSV File 保存为CSV文件：

```
IP,geoip,ipip,cz88
80.82.78.38,塞舌尔群岛,荷兰荷兰,荷兰阿姆斯特丹Ecatel公司,
116.62.176.205,中国北京市北京,中国浙江杭州,辽宁省铁通,
121.196.225.104,中国浙江省杭州,中国浙江杭州,浙江省杭州市阿里巴巴网络有限公司,
120.55.242.159,中国浙江省杭州,中国浙江杭州,浙江省杭州市阿里云BGP数据中心,
94.102.49.174,塞舌尔群岛,荷兰荷兰,荷兰 CZ88.NET,
118.178.228.154,中国浙江省杭州,中国浙江杭州,浙江省杭州市阿里云计算有限公司,
59.110.6.177,中国浙江省杭州,中国北京北京,广东省深圳市英达通信,
47.90.92.26,香港,中国香港,香港阿里云数据中心,
```