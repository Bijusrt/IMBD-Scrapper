from bs4 import BeautifulSoup
import requests,pprint
url=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=8a7876cd-2844-4017-846a-2c0876945b7b&pf_rd_r=C6ZKX5N78115F6BM14Y3&pf_rd_s=right-5&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_india_tr_rhs_1")
soup=BeautifulSoup(url.text,'lxml')
table=soup.find('tbody',class_='lister-list')
body=table.find_all('tr')
_list=[]
for i in body:
	_dict={}
	data=i.find('td',class_="titleColumn")
	no=''
	for j in data.text:
		no+=j
		if j=='.':
			break
	_dict['No']=no.strip()
	_dict['Movie']=data.find('a').text
	_dict['Year']=int(data.find('span').text.strip('(').strip(')'))
	_dict['Rating']=i.find('strong').text
	_dict['Link']="https://www.imdb.com/"+i.find('a')['href']
	_list.append(_dict)
pprint.pprint(_list)