#-*-coding:utf-8-*-2
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from coupon_spider import CouponSpider

def coupon_spider_job():
	spider = CouponSpider()
	spider.start_spider()
	print ('== 爬取完成 {}=='.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

scheduler = BlockingScheduler()
scheduler.add_job(coupon_spider_job, 'interval', minutes=5)
scheduler.start()