from bs4 import BeautifulSoup
import pprint,json

with open('/home/bijusrt/Desktop/biju/webscrapping/250movies.json','r') as movie_details:
    details=json.load(movie_details)
    _genre=[]
    for i in details:
        for k in i['Genres']:
            if k not in _genre:
                _genre.append(k)
    _by_genre={}
    for i in _genre:
        _by_genre[i]=0
    for j in _by_genre:
        for i in details:
            for k in i['Genres']:
                if k==j:
                    _by_genre[j]+=1
    pprint.pprint(_by_genre)




