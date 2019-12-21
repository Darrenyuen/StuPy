# -*- coding: utf-8 -*-
import requests

url = 'http://1.1.1.2/ac_portal/userflux'

headers = {
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection' : 'keep-alive',
	'Content-Length': '0',
	'Host': '1.1.1.2',
	'Origin': 'http://1.1.1.2',
	'Referer': 'http://1.1.1.2/ac_portal/20170602150308/pc.html?template=20170602150308&tabs=pwd&vlanid=0&_ID_=0&switch_url=&url=',
	'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest'	
}

try:
	r = requests.post(url, headers = headers)
except Exception as e:
	print(e)
else:
	print(r.status_code)
	print(r.text)
finally:
	pass