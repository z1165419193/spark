import urllib.request
from bs4 import BeautifulSoup
import re

def resapce(word):
    return word.replace('\n','').replace('\r','').replace('\t','').replace(' ','').replace('\xa0','').replace('&nbsp;','')
def get_text(url1):
    html1=urllib.request.urlopen(url1).read().decode('utf-8')
    soup1=BeautifulSoup(html1)
    pattern=r'<a href="/news/detail/aid/(.*?)" title="'
    urlid=re.findall(pattern,html1,re.S)
    for id in urlid:
        url2= 'http://lib.zut.edu.cn/news/detail/aid/'+str(id)
        print(url2)
        with open('zhongyuangongxueyuan.txt','a+',encoding='utf-8') as f:
            f.writelines(url2+'\n')
        html2=urllib.request.urlopen(url2).read().decode('utf-8')
        soup2=BeautifulSoup(html2)
        title=soup2.find_all('div','cont-title','h2')
        for t1 in title:
            tit=resapce(t1.get_text())
            print(title)
            with open('zhongyuangongxueyuan.txt' ,'a+', encoding='utf-8') as f:
                f.writelines(tit+' ')
        with open('zhongyuangongxueyuan.txt', 'a+', encoding='utf-8') as f:
            f.writelines( '\n ')
        content=soup2.find_all('div','cont-main','p')
        for c1 in content:
            con =resapce(c1.get_text())
            with open('zhongyuangongxueyuan.txt', 'a+', encoding='utf-8') as f:
                f.writelines(con+'\n')

def main(id):
    url = 'http://lib.zut.edu.cn/news/listNew/cid/10/page/'+str(id)
    html = get_text(url)
if __name__=='__main__':
    for i in range(1,41):
        main(i)