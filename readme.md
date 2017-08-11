# 爬虫的业务逻辑
1. 

http://uland.taobao.com/coupon/edetail?activityId=308006b6af6d4828bc532ba3e5703895&pid=mm_40490058_11180430_56318467&itemId=543663994934&dx=1&numiid=numiid543663994934

https://uland.taobao.com/coupon/edetail?activityId=c1eb37f1eedc4e1eaee29256ad54bcd9&pid=mm_40490058_11180430_56318467&itemId=18007475010

1.每间隔10分钟爬去一次
2.查询的参数设置为当前时间，请求返回的结果是html
3.

http://tzx119wade:61142304@ddns.oray.com/ph/update?hostname=http://177m57v297.iask.in&myip=192.168.3.128

# 微信里需要监听的事件
1. 当添加新好友的时候，按照当日的领取人数返回10条信息
2. 自动回复：通过消息关键词查找数据库中的商品，拼接商品链接返回
3. 定时任务：每天的早中晚，推送

# 微信机器人
1. 机器人捕获发送的消息，然后通过这个关键词拼成一个查询请求，比如http://search_key?=筷子,类似于向搜索页面传递一个关键词