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

    ret = podpp[0] +" "+ podpp[1].replace(',','')
    # for i in ret:
    #print(ret)
    return ret
    #текущее время
    #print(time.ctime())
def vk():
    print("try")

    # proxies = {
    #     'http': 'http://10.10.1.10:3128',
    #     'https': 'http://10.10.1.10:1080',
    # }



    # proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}




    # r = requests.get("https://vk.com/progresstech_ukraine",
    #                  proxies={"http": "http://61.233.25.166:80"})


    # s = requests.Session()
    # s.proxies = {"http": "http://61.233.25.166:80"}
    #
    # r = s.get("https://vk.com/progresstech_ukraine")
    # print(r.text)
    #print(r.text)


    #r=requests.get('https://vk.com/progresstech_ukraine', proxies=proxies)
    # soup = bs(r.text, "html.parser")
    # print (soup)
vk()