import re
import requests
from bs4 import BeautifulSoup

from utils import *


def get_questions(html):
    result = []
    bsObj = BeautifulSoup(html, 'html.parser')
    tags = bsObj.findAll('div', {'itemprop':'zhihu:question'})
    for tag in tags:
        result.append(tag.get_text())
    return result

if __name__ == '__main__':

    url = 'https://www.zhihu.com/search?type=content&q='
    word = 'python'
    query_url = url + word

    url2 = 'https://www.zhihu.com/api/v4/search_v3?t=general&q=python&correction=1&search_hash_id=106494f9311bd865f0f2487db399de64&offset=5&limit=10'

    foutput = open('../txt/output.txt', 'w')

    html = get_html(query_url)
    print(html, file=foutput)

    search_hash_id = re.findall(r'search_hash_id=(.*?)&amp', html)[0]
    print(search_hash_id)

    questions = get_questions(html)

    url2 = 'https://www.zhihu.com/api/v4/search_v3?t=general&q={}&correction=1&search_hash_id={}&offset=5&limit=10'.format(word, search_hash_id)
    print(url2)
    #html = get_html(url2)

    para = {'t':'general',
            'q':word,
            'correction':1,
            'search_hash_id':search_hash_id,
            'offset':5,
            'limit':10}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Cookie': 'd_c0="AAACOPkv4guPTgpfvxxgUbYXCYeobcPpcaM=|1496937740"; _zap=d4e20633-41ae-4087-ad89-5762c7475604; aliyungf_tc=AQAAADLVtjuE1wwAYTxXbqk2Ia4bOFF5; q_c1=a6edf440be0e481fbdcc32a8537e1bd3|1502865097000|1496937625000; q_c1=a6edf440be0e481fbdcc32a8537e1bd3|1513650741000|1496937625000; __utma=51854390.666145863.1496937740.1513316232.1514186623.5; __utmc=51854390; __utmz=51854390.1514186623.5.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.000--|2=registration_date=20121116=1^3=entry_date=20170609=1; capsion_ticket="2|1:0|10:1514293493|14:capsion_ticket|44:MTQzNzI1YzhiNDEwNGY4ODk2NDUyMWVhM2JjYTc2ZTI=|2c2841f4cff993716dfe04e10d6f2ecad86c23ab2d77ee0e084b0e905cbcacbc"; _xsrf=26383ffb-250b-4528-90f3-4f6014f68012; l_cap_id="OGY2M2YzMjBhYjAxNDAyOTliZDVlMGI3ZDU4MDAwYzQ=|1514298673|5c1c2508f3e935b48ce751de1f6245196fe80d86"; r_cap_id="ZGEwN2JiOGIzNjcyNDE3Njk2ZTUxZmNkYjI2YWFhMDg=|1514298673|80dcb9e0155f669410cfa3434243dd38e7291e3b"; cap_id="YmI3NjIwM2QzNjZlNGJmNDlkOTU4NTI0YjE2ZGE3ODM=|1514298673|6c42a9548774bec5f36fa2710b3f941a60d3de65"',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
        'Cache-Control': 'max-age=0'}

    html = requests.get('https://www.zhihu.com/api/v4/search_v3?', headers=headers, params=para)
    print(html)
    quit()
    questions = get_questions(html)
    for q in questions:
        print(q)



    
