import urllib.request
from bs4 import BeautifulSoup
import re

def resapce(word):
    return word.replace('\n','').replace('\r','').replace('\t','').replace(' ','').replace('\xa0','').replace('&nbsp;','')
def get_text(url1):
    html1=urllib.request.urlopen(url1).read().decode('utf-8')
    soup1=BeautifulSoup(html1,"html.parser")
    pattern = soup1.find_all('a', 'c189399')
    for id in pattern:
        rel = r'href="../../(.*?)"'
        url2 = 'http://lib.zut.edu.cn/'+re.findall(rel, str(id), re.S)[0]
        print(url2)
        with open('zhongyuangongxueyuan.txt', 'a+', encoding='utf-8') as f:
            f.write(url2 + '\n')
        html2=urllib.request.urlopen(url2).read().decode('utf-8')
        soup2=BeautifulSoup(html2,"html.parser")
        title=soup2.find_all('h1',attrs={'align':'center'})
        for t1 in title:
            tit=resapce(t1.get_text())
            print(tit)
            with open('zhongyuangongxueyuan.txt','a+', encoding='utf-8') as f:
                f.write(tit+'')
        with open('zhongyuangongxueyuan.txt', 'a+', encoding='utf-8') as f:
            f.write('\n')
        content=soup2.find_all('div','v_news_content')
        for c1 in content:
            con =resapce(c1.get_text())
            with open('zhongyuangongxueyuan.txt', 'a+', encoding='utf-8') as f:
                f.write(con+'\n')

def main(id):
    url ='http://lib.zut.edu.cn/xwzx/xw/'+str(id)+'.htm'
    html = get_text(url)
if __name__=='__main__':
    for i in range(1,54):
        main(i)