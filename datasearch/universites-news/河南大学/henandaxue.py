import urllib.request
from bs4 import BeautifulSoup
import re


def resapce(word):
    return word.replace('\n','').replace('\r','').replace('\t','').replace(' ','').replace('\xa0','').replace('&nbsp;','')
def get_text(url1):
    html1=urllib.request.urlopen(url1).read()
    soup1=BeautifulSoup(html1)
    pattern=soup1.find_all('a','c17990')
    for id in pattern:
        rel = r'href="(.*?)"'
        ur=re.findall(rel,str(id),re.S)[0]
        url2='http://lib.henu.edu.cn/'+ur
        print(url2)
        with open('henandaxue.txt','a+',encoding='utf-8') as f:
            f.write(url2+'\n')
        html2=urllib.request.urlopen(url2).read().decode('utf-8')
        soup2=BeautifulSoup(html2)
        title=soup2.find_all('h1')
        for t1 in title:
            tit=resapce(t1.get_text())
            with open('henandaxue.txt', 'a+', encoding='utf-8') as f:
                f.write(tit + '\n')
        time=soup2.find_all('div',attrs={"style":"font-size:10pt; line-height:180%"})
        for t2 in time:
            tim = resapce(t2.get_text())
            with open('henandaxue.txt', 'a+', encoding='utf-8') as f:
                f.write(tim + '')
        with open('henandaxue.txt', 'a+', encoding='utf-8') as f:
            f.write('\n')
        content=soup2.find_all('div',attrs={"style":"line-height:2em"})
        for c1 in content:
            con = resapce(c1.get_text())
            with open('henandaxue.txt', 'a+', encoding='utf-8') as f:
                f.write( con+ '\n')

def main(id):
    url = 'http://lib.henu.edu.cn/list.jsp?a4t=40&a4p='+str(id)+'&a4c=15&urltype=tree.TreeTempUrl&wbtreeid=1017'
    html = get_text(url)
if __name__=='__main__':
    for i in range(1,41):
        main(i)