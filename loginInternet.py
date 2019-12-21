# -*- coding: utf-8 -*-
import requests

# url http://1.1.1.2/ac_portal/login.php
#opr:pwdLogin
#userName:17sfyuan
#pwd:hahahaha
#//ipv4or6:2001:250:3003:a600:bd2a:e589:3991:1836
#rememberPwd:0

url = 'http://1.1.1.2/ac_portal/login.php'

#消息头
headers = {
	'Content-Type': 'application/x-www-form-urlencoded'
}

params = {
	'opr':'pwdLogin',
	'userName':'17sfyuan',
	'pwd':'hahahaha',
	'rememberPwd':0
}

try:
	r = requests.post(url, data = params, headers = headers, verify = False)
except Exception as e:
	print(e)
else:
	print(r.status_code)
	print(r.text)
finally:
	pass