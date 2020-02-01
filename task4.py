from bs4 import BeautifulSoup
import requests,pprint,string,json
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
	_dict['Link']="https://www.imdb.com"+i.find('a')['href']
	_list.append(_dict)
# pprint.pprint(_list)``
def scrapped_movie(mov_link):
    new_url=requests.get(mov_link).text
    soup=BeautifulSoup(new_url,'html.parser')
    movie_dict={}
    new_data=soup.find('div',class_="title_wrapper").h1.text
    movie_name=''
    for i in new_data:
        if i=='(':
            break
        else:
            movie_name+=i
    movie_Name=movie_name.replace('\xa0','')
    movie_dict['Name']=movie_Name
    Bio=soup.find('div',class_='summary_text').text
    plot=''
    for i in Bio:
        if '\n' in i:
            i.replace('\n','')
        plot+=(i)
    movie_dict['Bio']=plot.strip()
    dire=soup.find('div',class_="credit_summary_item")
    director=dire.find_all('a')
    director_list=[]
    for i in director:
        director_list.append(i.text)
    movie_dict['Director']=director_list
    pic=soup.find('div',class_="poster")
    movie_dict['Poster Url']=pic.find('img')['src']
    genre_list=[]
    gen=soup.find_all('div',class_="see-more inline canwrap")
    for i in gen:
        if 'Genres:' in i.text:
            genre=i
            break
    genres=genre.find_all('a')
    for i in genres:                                
        genre_list.append(i.text)
    movie_dict['Genres']=genre_list
    detail=soup.find_all('div',class_="txt-block")
    for i in detail:
        if 'Country:' in i.text:
            movie_dict['Country']=i.find('a').text
        elif 'Language:' in i.text:
            language=i.find_all('a')
    time=soup.find('div',class_="subtext")
    run=time.find('time').text.strip()
    if len(run)>4:
        if run[4] in string.digits:
            Runtime=(int(run[0])*60)+int(run[3]+run[4])
        else:
            Runtime=(int(run[0])*60)+int(run[3])
    else:
        Runtime=int(run[0])*60
    movie_dict['Runtime']=int(Runtime)
    language_list=[]
    for i in language:
        language_list.append(i.text)
    movie_dict['Language']=language_list
    return(movie_dict)
moviesdetails=[]
for i in  _list:
    moviesdetails.append(scrapped_movie(i['Link']))
full_details=json.dumps(moviesdetails)
json1=open('task4.json','w+')
json1.write(full_details)
