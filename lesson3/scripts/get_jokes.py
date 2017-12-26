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

def get_html2(url):
    """
    请求url，返回html
    """
    html = urlopen(url).read().decode('utf8')
    return html

def get_jokes(url):
    """
    获取当前页面下的所有笑话文本
    """
    html = get_html(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    jokes = bsObj.find_all('div', class_="content")
    print("这个页面总共有%d个笑话。" % len(jokes))
    print("第一个div标签对象\n\n", jokes[0])
    print("对象类型： ", type(jokes[0]))
    result = []
    for joke in jokes:
        result.append(joke.get_text().strip())
    return result

def get_jokes_re(url):
    """
    用正则表达式获取当前页面下的所有笑话文本
    """
    html = get_html(url)
    pattern = r'<div class="content">(.*?)</div>'
    jokes = re.findall(pattern, html, flags = re.DOTALL) # flags = re.DOTALL，跨行匹配，让.可以匹配换行符
    result = []
    for joke in jokes:
        joke = re.findall(r'<span.*?>(.*?)</span>', joke, flags = re.DOTALL)
        joke_text = joke[0].strip()
        joke_text = re.sub('<.*?>', '', joke_text) # 去掉标签
        result.append(joke_text)
    return result

if __name__ == "__main__":

    url = "https://www.qiushibaike.com/hot/page/1/"

    '''
    foutput = open('../txt/jokes1.txt', 'w')
    jokes = get_jokes(url)
    n = 1
    for joke in jokes:
        print("joke ", n, file=foutput)
        print(joke, file=foutput)
        n += 1
    foutput.close()'''

    foutput2 = open('../txt/jokes2.txt', 'w')
    jokes = get_jokes_re(url)
    n = 1
    for joke in jokes:
        print("joke ", n, file=foutput2)
        print(joke, file=foutput2)
        n += 1
    foutput2.close()

