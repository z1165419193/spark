import urllib.request
from bs4 import BeautifulSoup
import re


def resapce(word):
    return word.replace('\n','').replace('\r','').replace('\t','').replace(' ','').replace('\xa0','').replace('&nbsp;','')
def get_text(url1):
    html1=urllib.request.urlopen(url1).read().decode('utf-8')
    soup1=BeautifulSoup(html1,"html.parser")
    pattern=soup1.find_all('ul',attrs={'id':'list_hrm'})
    rel = r'href="(.*?)"'
    for id in pattern:
        url2='http://www.hactcm.edu.cn'+re.findall(rel,str(id),re.S)[0]
        print(url2)
        with open('henanzhongyiyao.txt','a+',encoding='utf-8') as f:
            f.write(url2+'\n')
        html2=urllib.request.urlopen(url2).read().decode('utf-8')
        soup2=BeautifulSoup(html2)
        title=soup2.find_all('span','c57536_title')
        for t1 in title:
            tit=resapce(t1.get_text())
            with open('henanzhongyiyao.txt', 'a+', encoding='utf-8') as f:
                f.write(tit + '\n')
        time=soup2.find_all('span','c57536_date')
        for t2 in time:
            tim = resapce(t2.get_text())
            with open('henanzhongyiyao.txt', 'a+', encoding='utf-8') as f:
                f.write(tim + '')
        with open('henanzhongyiyao.txt', 'a+', encoding='utf-8') as f:
            f.write('\n')
        content=soup2.find_all('div','c57536_content')
        for c1 in content:
            con = resapce(c1.get_text())
            with open('henanzhongyiyao.txt', 'a+', encoding='utf-8') as f:
                f.write( con+ '\n')

def main(id):
    url = 'http://www.hactcm.edu.cn/list.jsp?a57535t=234&a57535p='+str(id)+'&a57535c=20&urltype=tree.TreeTempUrl&wbtreeid=1014'
    html = get_text(url)

if __name__=='__main__':
    for i in range(1,235):
        main(i)