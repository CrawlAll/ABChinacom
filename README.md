目标网站
http://app.abchina.com/branch/

省份 名字Name 和 编号ID  -->json格式
http://app.abchina.com/branch/common/BranchService.svc/District

地市 名字Name 和 编号ID  更换url后的省份ID-->json格式
http://app.abchina.com/branch/common/BranchService.svc/District/省份ID

区县 名字Name 和 编号ID  更换url后的地市ID-->json格式
http://app.abchina.com/branch/common/BranchService.svc/District/Any/地市ID

数据接口
```
base_url = http://app.abchina.com/branch/common/BranchService.svc/Branch

params共计7个
p(province)
c(city)
b(district)
q(关键字查询的字段)
t
z(选择信用卡面签的字段，默认0)
i(页码，每页显示20条)
```

- 比如
- 河南省           410000
- 河南新乡市       410700
- 河南新乡市卫滨区 410703

数据接口

base_url = 'http://app.abchina.com/branch/common/BranchService.svc/Branch?p={}&c={}&b={}&q=&t=1&z=0&i={}'
