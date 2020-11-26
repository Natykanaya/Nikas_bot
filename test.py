from bs4 import BeautifulSoup as bs
import requests
import time

def test():
    #вытащила подписчиков
    r = requests.get("https://www.facebook.com/ProgresstechUA/")
    # the script extracts all website andbo return in
    soup = bs(r.text, "html.parser")
    #podsp_p=[]
    # проверяем существование вакансий по запросу (если есть этот тег, то значит вакансий нет)
    podsp = soup.find_all('div', class_="_4bl9")
    #podsp_p=podsp.find('div')
    # for i in podsp:
    #    print(i.get_text())
    podsp_p=podsp[2]
    #print(podsp_p.get_text())
    return podsp_p.get_text()

    # r = requests.get("https://www.instagram.com/progresstech.ua/?hl=ru")
    # # the script extracts all website andbo return in
    # soup = bs(r.text, "html.parser")
    # podsp_pa=[]
    # # проверяем существование вакансий по запросу (если есть этот тег, то значит вакансий нет)
    # podpis = soup.find_all('span', class_="g47SY  ")
    # if podpis==None:
    #     print("Nooonee")
    # else:
    #     print("no none!")
    # print(podpis)
    # print(time.ctime())
    # for i in podsp:
    #     print(i.get_text())



    # r = requests.get("https://www.instagram.com/progresstech.ua/?hl=ru")
    # # the script extracts all website andbo return in
    # soup = bs(r.text, "html.parser")
    # names=[]
    # # проверяем существование вакансий по запросу (если есть этот тег, то значит вакансий нет)
    # podsp = soup.find_all('span', class_="g47SY lOXF2")
    # print(podsp)
    # for name in podsp:
    #     names.append(name['title'])
    #     print(names)
test()