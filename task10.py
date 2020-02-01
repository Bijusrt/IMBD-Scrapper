from bs4 import BeautifulSoup
import pprint,json

with open('250movies.json','r+') as movie_details:
    details=json.load(movie_details)
    director={}
    language={}
    for i in details:
        dir_var=i['Director']
        if len(dir_var)>1:
            for j in dir_var:
                dir_var1=''.join(j)
                director[dir_var1]={}
        else:
            dir_var2=''.join(dir_var)
            director[dir_var2]={}
    director.pop("1 more credit")
    for i in director:
        for  j in details:
            if i in j['Director']:
                for k in j['Language']:
                    if k not in director[i]:
                        director[i][k]=1
                    else:
                        director[i][k]=director[i][k]+1
    pprint.pprint(director)

