import urllib.request
from bs4 import BeautifulSoup
import re


def resapce(word):
    return word.replace('\n','').replace('\r','').replace('\t','').replace(' ','').replace('\xa0','').replace('&nbsp;','')
def get_text(url1,idd1):
    html1=urllib.request.urlopen(url1).read().decode('utf-8')
    soup1=BeautifulSoup(html1,"html.parser")
    pattern=soup1.find_all( 'span',attrs={'class':'Article_Title'},limit=14)
    rel = r'href="(.*?)"'
    idd=idd1
    for id in pattern:
        idd = idd + 1
        with open('henanshifandaxue.txt', 'a+', encoding='utf-8') as f:
            f.write(str(idd) + '====')
        url2='http://www.htu.edu.cn'+re.findall(rel,str(id),re.S)[0]
        print(url2)
        html2=urllib.request.urlopen(url2).read().decode('utf-8')
        soup2=BeautifulSoup(html2)
        title=soup2.find_all('span','Article_Title')
        for t1 in title:
            tit=resapce(t1.get_text())
            with open('henanshifandaxue.txt', 'a+', encoding='utf-8') as f:
                f.write(tit + '====')
        content=soup2.find_all('div','Article_Content')
        for c1 in content:
            con = resapce(c1.get_text())
            with open('henanshifandaxue.txt', 'a+', encoding='utf-8') as f:
                f.write( con+ '\n')

def main(id):
    url = 'http://www.htu.edu.cn/8956/list'+ str(id)+'.htm'
    idd1 = 21520100+14*(id-1)
    html = get_text(url,idd1)


if __name__=='__main__':
    for i in range(1,48):
        main(i)