import requests
from bs4 import BeautifulSoup

# url : http://credit.stu.edu.cn/Info/DisplayKkb.aspx?ClassID=113658

# classId = input('请输入开课班号：')
# print(classId)

classInfoUrl = 'http://credit.stu.edu.cn/Info/DisplayKkb.aspx?ClassID=113658'

classmates = []

def getHTML(url):
	try:
		r = requests.get(url)
		r.raise_for_status
		r.encodeing = 'gb2312'
		return r.text
	except Exception as e:
		return 'error'
	else:
		pass
	finally:
		pass

def excavateClassmates(soup):
	data = soup.find_all('tr')
	for classmate in data:
		info = classmate.find_all('td')
		if len(info) == 0:
			continue
		singleClassmate = []
		for td in info:
			singleClassmate.append(td.string)
		classmates.append(singleClassmate)

def main():
	soup = BeautifulSoup(getHTML(classInfoUrl), "html.parser")
	excavateClassmates(soup)
	print(classmates)

main()
