import re
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime
import random
from spider import scheduler

url = 'http://m.huim.com/ajax/GetIndex?id=2017-07-28+11%3A35%3A03&tags='
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')

a = soup.find_all('a')[7]
img = ''
if a.find('img').has_attr('data-original'):
	img = a.find('img')['data-original']
else:
	img = a.find('img')['src']
print (img)

# matchObj = re.search(r'activityId=(\w+)&pid',url)
# if matchObj:
# 	print (matchObj.group(1))

# host = '127.0.0.1'
# port = 27017
# client = MongoClient(host,port)
# coupon_db = client['coupon_db']
# coupon = coupon_db['coupon']

# print (coupon.find({'num_receive':{'$gte':100}}).count())

# result = coupon.find_one({'activityId':'1234'})
# if result == None:
# 	print ('no data')

# api_url = 'http://m.huim.com/ajax/GetIndex?id=2017-07-23+23%3A32%3A24&tags='
# re = requests.get(api_url)
# soup = BeautifulSoup(re.text,'lxml')
# tag_a = soup.find('a')

# img = tag_a.find('img')['src']
# print (img)
# tag_p = tag_a.find('p',class_='goods_coupon')
# tag_span = tag_p.find_all('span')
# print (tag_span[1].text)

# tag_p = tag_a.find('p',class_='goods_num')
# num = tag_p.find_all('span')[1].text
# print (num)

# 爬取IP代理
# url_list = ['http://www.kuaidaili.com/free/inha/{}/'.format(i) for i in range(1,5)]
# print (url_list)
# host = '127.0.0.1'
# port = 27017
# client = MongoClient(host,port)
# coupon_db = client['coupon_db']
# ip_pool = coupon_db['ip_pool']
# # 构造ip池
# ip_list = ip_pool.find({'created_tiem':'2017-07-26'})
# print (ip_list)
# for item in ip_pool.find({'created_time':'2017-07-26'}):
# 	ip_list.append(item['ip'])
# print (ip_list)

# for url in url_list:
# 	try:
# 		ip = random.choice(ip_list)
# 		proxies={'http':ip}
# 		resp = requests.get(url,proxies=proxies,timeout=3)
# 	except:
# 		print ('connect wrong')
# 	else:
# 		soup = BeautifulSoup(resp.text,'lxml')
# 		ip_tag = soup.find_all(attrs={'data-title':'IP'})
# 		ip_list = [item.text for item in ip_tag]
# 		print (ip_list)

# 验证IP是否可用
# 将有效的IP写入到数据库
# host = '127.0.0.1'
# port = 27017
# client = MongoClient(host,port)
# coupon_db = client['coupon_db']
# ip_pool = coupon_db['ip_pool']
# for ip in ip_list:
# 	proxies = {'http':ip}
# 	try :
# 		resp = requests.get('https://www.douban.com/',proxies=proxies, timeout=3)
# 	except : 
# 		print ('ip not valid:',ip)
# 	else:
# 		date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 		date_now = date_now.split(' ')[0]
# 		ip = {
# 			'ip':ip,
# 			'created_time':date_now
# 		}
# 		ip_pool.insert_one(ip)


