import json
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def testloop():

    # for i in range(300000, 21124826):
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    minVal = 20000000
    maxVal = 21000000

    for i in range(minVal, maxVal):
        response = session.get(f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty')
        getjson = response.json()
        #use this to open
        if getjson is None:
            print([i])
            print('missing title')
            pass

        elif 'title' in getjson:
            gettitle = response.json()['title']
            f = open(f'HN{minVal}-{maxVal}.txt', "a", encoding="utf-8")
            f.write(gettitle + "\r\n" + "<|endoftext|>\r\n")
            f.close
            print([i])
            print(response.json()['title'])

        else:
            pass


testloop()
