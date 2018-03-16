1. 第一次运行时，line8-10注释(用于写入表头，清空csv)；
2. 之后运行时**注释**掉8-10行。
3. 选择相应的cache文件(line22-26)，以及页数。

共分五次抓取 



待改进：

加入多线程(单线速度慢)；

IP是否需要每次都更改；

存入数据时加上手机的uniqid可能会更好；

存入csv file，还是.db file；

逻辑可以精炼，再清晰一点；

如何用python requests 请求java script数据，(详情页面的手机价格被隐藏，无法通过requests.get直接得到)；

学习爬虫其他框架，scrapy，spider等。

