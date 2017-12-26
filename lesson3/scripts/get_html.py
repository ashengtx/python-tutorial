from urllib.request import Request, urlopen

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


if __name__ == "__main__":

    url = "https://www.qiushibaike.com/hot/page/1/"
    #url = "https://baike.baidu.com/item/Python/407313"
    foutput = open('../txt/output.txt', 'w')
    print(get_html2(url), file=foutput) # 会报错，换get_html试试
    foutput.close()

