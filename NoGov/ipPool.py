import requests
import time
from threading import Thread

from lxml import etree
from multiprocessing.dummy import Pool

ALL_PROXIES = []

def timecost(func):
	def wrapper():
		start_time = time.time()
		func()
		end_time = time.time()
		print(f"cost {end_time-start_time} sec")

	return wrapper

def ip3366():
	UA = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0"}

	def getting(num):
		proxy_list = []

		r = requests.get("http://www.ip3366.net/free/?stype=%s" % str(num),headers=UA)
		r.encoding = "utf-8"

		page = r.text

		ee = etree.HTML(page)

		for tr in ee.xpath("//div[@id='list']//tr"):
			
			try:
				if tr.xpath("td[4]/text()")[0] == "HTTP":
					proxy_list.append((tr.xpath("td[1]/text()")[0],tr.xpath("td[2]/text()")[0]))
			except:
				pass

		print(ALL_PROXIES)

	for i in range(10):
		t = Thread(target=getting,args=(i,))
		t.start()


ip3366()
