import urllib.request
from bs4 import BeautifulSoup
import re


def resapce(word):
    return word.replace('\n','').replace('\r','').replace('\t','').replace(' ','').replace('\xa0','').replace('&nbsp;','')
def get_text(url1):
    html1=urllib.request.urlopen(url1).read().decode('utf-8')
    soup1=BeautifulSoup(html1,"html.parser")
    pattern=soup1.find_all('table','columnStyle')
    rel = r'href="(.*?)"'
    for id in pattern:
        url2='http://www.xxmu.edu.cn'+re.findall(rel,str(id),re.S)[0]
        print(url2)
        with open('xinxiangyixueyuan.txt','a+',encoding='utf-8') as f:
            f.write(url2+'\n')
        html2=urllib.request.urlopen(url2).read().decode('utf-8')
        soup2=BeautifulSoup(html2)
        title=soup2.find_all('td','tit_pop')
        for t1 in title:
            tit=resapce(t1.get_text())
            with open('xinxiangyixueyuan.txt', 'a+', encoding='utf-8') as f:
                f.write(tit + '\n')
        time=soup2.find_all('td','padding_top')
        for t2 in time:
            tim = resapce(t2.get_text())
            with open('xinxiangyixueyuan.txt', 'a+', encoding='utf-8') as f:
                f.write(tim + '')
        with open('xinxiangyixueyuan.txt', 'a+', encoding='utf-8') as f:
            f.write('\n')


def main(id):
    url = 'http://www.xxmu.edu.cn/s/25/t/1763/p/22/i/'+str(id)+'/list.htm'
    html = get_text(url)

if __name__=='__main__':
    for i in range(1,4):
        main(i)