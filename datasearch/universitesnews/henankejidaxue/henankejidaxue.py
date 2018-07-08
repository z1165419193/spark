import urllib.request
from bs4 import BeautifulSoup
import re


def resapce(word):
    return word.replace('\n','').replace('\r','').replace('\t','').replace(' ','').replace('\xa0','').replace('&nbsp;','')
def get_text(url1):
    headers = {
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache - Control': 'max - age = 0',
        'Connection': 'keep - alive',
        'Cookie': 'td_cookie=3615363546; JSESSIONID=291525C93525A077BFB1706F222B51D8',
        'Host': 'lib.haust.edu.cn',
        'Upgrade - Insecure - Requests': ' 1',
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36',
    }
    req = urllib.request.Request(url1, headers=headers)
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    soup1=BeautifulSoup(html)
    pattern = soup1.find_all('li','sconimg', 'a')
    for id in pattern:
        rel = r'href="(.*?)"'
        ur = re.findall(rel, str(id), re.S)[0]
        print(ur)
        url2= 'http://lib.haust.edu.cn'+ ur
        print(url2)
        with open('henankejidaxue.txt','a+',encoding='utf-8') as f:
            f.write(url2+'\n')
        req1 = urllib.request.Request(url2, headers=headers)
        page = urllib.request.urlopen(req1)
        html = page.read().decode('utf-8')
        soup2=BeautifulSoup(html)
        title=soup2.find_all('h1')
        for t1 in title:
            tit=resapce(t1.get_text())
            with open('henankejidaxue.txt', 'a+', encoding='utf-8') as f:
                f.write(tit + '\n')
        time=soup2.find_all('div','list_cont_menu')
        for t2 in time:
            tim = resapce(t2.get_text())
            with open('henankejidaxue.txt', 'a+', encoding='utf-8') as f:
                f.write(tim + '\n')
        content=soup2.find_all('div','list_cont_content')
        for c1 in content:
            con = resapce(c1.get_text())
            with open('henankejidaxue.txt', 'a+', encoding='utf-8') as f:
                f.write( con+ '\n')

def main(id):
    url = 'http://lib.haust.edu.cn/haust/include/annmessage.jsp?id=104&pager.offset='+str(id)
    html = get_text(url)
if __name__=='__main__':
    for i in range(0,60,10):
        main(i)