import requests as r
import json

class city_list():
    def __init__(self):
        self.s=set()

    def get_city_list(self):
        with open('a.txt','r') as rfile:
            while 1:
                line = rfile.readline()
                if not line:
                    break
                self.s.add(line)
        return self.s

class get_loc():
    def __init__(self,url):
        self.url=url

    def get(self):
        txt=r.get(self.url,verify=False)
        res=json.loads(txt.text)
        return res['hits'][0]['point']


if __name__=='__main__':
    city_lists=city_list()
    s=city_lists.get_city_list()
    print(s)
    dic={
        'KY':'Kentucky',
        'OH':'Ohio',
        'VA':'Virginia',
        'WV':'West Virginia',
        'PA':'Pennsylvania'
    }
    f=open('b.txt','w')
    num=0
    for i in s:
        try:
            i=i.strip()
            loc=i.split('\t')
            r_state = dic[loc[0]]
            r_country = loc[1]
            url = 'https://graphhopper.com/api/1/geocode?q={state}%20{country}&debug=true&limit=1&key=9af836b6-de77-4b5d-a0c1-ade1208369ae'.format(state=r_state, country=r_country)
            l = get_loc(url)
            lat_lng = l.get()
            li='{}   {}  {}  {}\n'.format(r_state, r_country, lat_lng['lng'], lat_lng['lat'])
            f.write(li)
            print('已爬取{}(/461)项数据,为{} {}'.format(num,r_state,r_country))
            num=num+1
        except:
            print("爬取第"+str(num)+'条数据失败')
            num+=1