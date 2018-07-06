import urllib.request
from bs4 import BeautifulSoup
import re


def resapce(word):
    return word.replace('\n','').replace('\r','').replace('\t','').replace(' ','').replace('\xa0','').replace('&nbsp;','')
def get_text(url1):
    html1=urllib.request.urlopen(url1).read().decode('utf-8')
    soup1=BeautifulSoup(html1,"html.parser")
    pattern=soup1.find_all('div',attrs={'class':'xinxilist'})
    rel = r'href="(.*?)"'
    for id in pattern:
      for i in range(2,26):
        url2=re.findall(rel,str(id),re.S)[i]
        print(url2)
        with open('huabeishuilishuidian.txt','a+',encoding='utf-8') as f:
            f.write(url2+'\n')
        html2=urllib.request.urlopen(url2).read().decode('utf-8')
        soup2=BeautifulSoup(html2)
        title=soup2.find_all('h3')
        for t1 in title:
            tit=resapce(t1.get_text())
            with open('huabeishuilishuidian.txt', 'a+', encoding='utf-8') as f:
                f.write(tit + '\n')
        content=soup2.find_all('div','xinxi_con')
        for c1 in content:
            con = resapce(c1.get_text())
            with open('huabeishuilishuidian.txt', 'a+', encoding='utf-8') as f:
                f.write( con+ '\n')

def main(id):
    url = 'http://www5.ncwu.edu.cn/channels/2766_'+str(id)+'.html'
    html = get_text(url)

if __name__=='__main__':
    for i in range(2,23):
        main(i)