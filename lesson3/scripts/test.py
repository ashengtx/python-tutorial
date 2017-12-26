import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

def get_html(url):
    """
    请求url，返回html
    """
    req = Request(url, headers=headers)  
    html = urlopen(req).read().decode('utf8')
    return html

douban_url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='

def test(url):
    foutput = open('../txt/output.txt', 'w')

    html = get_html(url)
    #bsObj = BeautifulSoup(html, 'html.parser')
    print(html, file=foutput)
    #print(bsObj.h1)
    #print(bsObj.h2)
    #jokes = bsObj.findAll('div', {"class":"content"})

    pattern = r'<div class="content">(.*?)</div>'
    jokes = re.findall(pattern, html, flags = re.DOTALL)
    #print(jokes)
    print(len(jokes))
    for joke in jokes:
        joke = re.findall(r'<span.*?>(.*?)</span>', joke, flags = re.DOTALL)
        print(joke[0].strip())
    quit()
    print("这个页面总共有%d个笑话。" % len(jokes))
    print("第一个div标签对象\n\n", jokes[0])
    print("对象类型： ", type(jokes[0]))
    joke_text = jokes[0].get_text().strip()
    print(joke_text)


if __name__ == '__main__':
    url = "https://www.qiushibaike.com/hot/page/1/"
    test(url)
    
