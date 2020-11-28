from bs4 import BeautifulSoup as bs
import requests
import time

def fcbook():
    r = requests.get("https://www.facebook.com/ProgresstechUA/")
    soup = bs(r.text, "html.parser")
    podsp = soup.find_all('div', class_="_4bl9")
    #podsp_p=podsp.find('div')
    # for i in podsp:
    #    print(i.get_text())
    podsp_p=podsp[2]
    return podsp_p.get_text()

def inst():
    r = requests.get("https://www.instagram.com/progresstech.ua/?hl=ru")
    soup = bs(r.text, "html.parser")
    podpis = soup.find('meta',property="og:description")
    #
    podp=podpis["content"]
    podpp=podp.split()

    print(podpp[0],podpp[1])
    #текущее время
    #print(time.ctime())

inst()