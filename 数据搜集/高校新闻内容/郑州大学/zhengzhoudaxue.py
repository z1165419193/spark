import urllib.request
from bs4 import BeautifulSoup
import re


def resapce(word):
    return word.replace('\n','').replace('\r','').replace('\t','').replace(' ','').replace('\xa0','').replace('&nbsp;','')
def get_text(url1):
    html1=urllib.request.urlopen(url1).read().decode('utf-8')
    soup1=BeautifulSoup(html1,"html.parser")
    pattern=soup1.find_all('div','zzj_5a','a')
    for id in pattern:
        rel = r'href="(.*?)"'
        url2=re.findall(rel,str(id),re.S)[0]
        print(url2)
        with open('zhengzhoudaxue.txt','a+',encoding='utf-8') as f:
            f.write(url2+'\n')
        html2=urllib.request.urlopen(url2).read().decode('utf-8')
        soup2=BeautifulSoup(html2)
        title=soup2.find_all('div','zzj_3')
        for t1 in title:
            tit=resapce(t1.get_text())
            with open('zhengzhoudaxue.txt', 'a+', encoding='utf-8') as f:
                f.write(tit + '\n')
        time=soup2.find_all('span','zzj_f2')
        for t2 in time:
            tim = resapce(t2.get_text())
            with open('zhengzhoudaxue.txt', 'a+', encoding='utf-8') as f:
                f.write(tim + '')
        with open('zhengzhoudaxue.txt', 'a+', encoding='utf-8') as f:
            f.write('\n')
        content=soup2.find_all('div','zzj_5')
        for c1 in content:
            con = resapce(c1.get_text())
            with open('zhengzhoudaxue.txt', 'a+', encoding='utf-8') as f:
                f.write( con+ '\n')

def main(id):
    url = 'http://www16.zzu.edu.cn/msgs/vmsgisapi.dll/vmsglist?mtype=x&lan=205&tts=&tops=&pn='+str(id)
    html = get_text(url)

if __name__=='__main__':
    for i in range(1,12):
        main(i)