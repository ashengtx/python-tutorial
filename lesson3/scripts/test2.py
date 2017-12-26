works = ['解忧杂货铺', '白夜行', '嫌疑人X的献身', '放学后', '秘密', '流星之绊', '梦幻花', '祈祷落幕时']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',\
    'Cookie': 'd_c0="AAACOPkv4guPTgpfvxxgUbYXCYeobcPpcaM=|1496937740"; _zap=d4e20633-41ae-4087-ad89-5762c7475604; aliyungf_tc=AQAAADLVtjuE1wwAYTxXbqk2Ia4bOFF5; q_c1=a6edf440be0e481fbdcc32a8537e1bd3|1502865097000|1496937625000; q_c1=a6edf440be0e481fbdcc32a8537e1bd3|1513650741000|1496937625000; __utma=51854390.666145863.1496937740.1513316232.1514186623.5; __utmc=51854390; __utmz=51854390.1514186623.5.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.000--|2=registration_date=20121116=1^3=entry_date=20170609=1; capsion_ticket="2|1:0|10:1514293493|14:capsion_ticket|44:MTQzNzI1YzhiNDEwNGY4ODk2NDUyMWVhM2JjYTc2ZTI=|2c2841f4cff993716dfe04e10d6f2ecad86c23ab2d77ee0e084b0e905cbcacbc"; _xsrf=26383ffb-250b-4528-90f3-4f6014f68012; l_cap_id="OGY2M2YzMjBhYjAxNDAyOTliZDVlMGI3ZDU4MDAwYzQ=|1514298673|5c1c2508f3e935b48ce751de1f6245196fe80d86"; r_cap_id="ZGEwN2JiOGIzNjcyNDE3Njk2ZTUxZmNkYjI2YWFhMDg=|1514298673|80dcb9e0155f669410cfa3434243dd38e7291e3b"; cap_id="YmI3NjIwM2QzNjZlNGJmNDlkOTU4NTI0YjE2ZGE3ODM=|1514298673|6c42a9548774bec5f36fa2710b3f941a60d3de65"',\
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',\
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',\
    'Cache-Control': 'max-age=0'}
para = {'t':'general','q':'解忧杂货铺','correction':'1','search_hash_id':'4f6c83f37717c6bd8a4f339f08fbac89','offset':'5','limit':'10'}
para2 = {'include':'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,upvoted_followees;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=best_answerer)].topics',\
        'offset':'2',\
        'limit':'20',\
        'sort_by':'default'}
testDict={'解忧杂货铺里你明白什么道理？': 'https://www.zhihu.com/question/46397802', '《解忧杂货铺》的主线到底是几条呢？': 'https://www.zhihu.com/question/29138975'}
articleLogPath='/home/sheng/data/test/articleLog.txt'
questionLogPath='/home/sheng/data/test/question'
projectPath='/home/sheng/data/test'

def collectQ(name,url,filename,limit=20):
    with open(filename,'a') as f:
        try:
            f.write(name+'\r\n')
        except:
            f.write(url+'\r\n')
    r = requests.get(url, headers=headers)
    soup=bs4.BeautifulSoup(r.content,'lxml')
    answers=soup.find_all('span',{'itemprop':'text','class':"RichText CopyrightRichText-richText"})
    pat_html=r'<[\s\S]*?>'
    answer2=''
    for answer in answers:
        answer=''.join(str(answer.contents))
        answer=re.sub(pat_html,'',answer)
        answer2+=answer.replace(',','').replace("'",'')
        answer2+='\r\n====================\r\n'
    with open(filename,'a') as f:
        try:
            f.write(answer2)
        except:
            logging.warning(name+'      '+url+'1')
    for i in range(int(limit/20)):
        para2['offset']=i*20+2
        r = requests.get('https://www.zhihu.com/api/v4/questions/'+url[-8:]+'/answers?', headers=headers, params=para2)
        try:
            new_question=r.json()
            for answer in new_question['data']:
                answer=re.sub(pat_html,'',answer['content'])
                answer2=answer+'\r\n====================\r\n'
                with open(filename,'a') as f:
                    try:
                        f.write(answer2)
                    except:
                        # logging.warning(name+'      '+url+answer['content'])
                        pass
        except:
            pass

def collectZL(name,url,LogPath):
    r = requests.get(url, headers=headers)
    soup=bs4.BeautifulSoup(r.content,'lxml')
    article=soup.find_all('textarea',{'id':'preloadedState'})
    pat_content=r'"content":"[\s\S]*?","updated"'
    pat_html=r'<[\s\S]*?>'
    # print(article)
    try:
        result=re.findall(pat_content,article[0].contents[0])
        tmp=re.findall(pat_content,result[0][11:])
        if len(tmp)!=0:
            result=tmp
        result=result[0][11:-11].replace('\\u003C','<').replace('\\u003E','>')
        result=name+'\r\n'+re.sub(pat_html,'',result)+'\r\n==============\r\n'
        # print(re.sub(pat_html,'',result))
        with open(LogPath+'\\article.txt','a') as f:
            try:
                f.write(result)
            except:
                logging.warning(name+'      '+url)
                pass
    except:
        logging.warning(name+'===>null')

def findresult(work,num=10):
    questionDict={}
    articleDict={}
    url = 'https://www.zhihu.com/search?type=content&q=' + work

    r = requests.get(url, headers=headers)
    content=r.content
    pat=r'hash_id=.{32}'
    hashID=re.findall(pat, str(content))
    # print(hashID[0][8:40])
    para['search_hash_id']=hashID[0][8:40]

    soup = bs4.BeautifulSoup(content, 'lxml')
    questions=soup.find_all('div',{'itemprop':'zhihu:question'})
    pat_content=r'content="(.*?)"'
    for question in questions:
        soup2=bs4.BeautifulSoup(str(question),'lxml')
        title=soup2.find_all('meta',{'itemprop':'name'})
        title=re.findall(pat_content,str(title))
        title=title[0].replace('<em>','').replace('</em>','')
        title_url=soup2.find_all('meta',{'itemprop':'url'})
        title_url=re.findall(pat_content,str(title_url))
        questionDict[title]=title_url[0]
        # questionDict.setdefault(title,title_url[0])
        # print(title[0].replace('<em>','').replace('</em>',''),'    ',title_url[0])
    articles=soup.find_all('div',{'itemprop':'article'})
    # print(articles)
    for article in articles:
        soup2 = bs4.BeautifulSoup(str(article).replace('<em>','').replace('</em>',''), 'lxml')
        title=soup2.span
        title=title.contents
        title_url=soup2.a
        title_url=title_url['href']
        articleDict[title[0]]='https:'+str(title_url)
    for i in range(int(num/10)):
        para['offset']=i*10+5
        r = requests.get('https://www.zhihu.com/api/v4/search_v3?t=general&q='+work, headers=headers, params=para)
        print(r)
        quit()
        new_question=r.json()
        # print(new_question)
        for question in new_question['data']:
            try:
                title=question['object']['question']['name'].replace('<em>','').replace('</em>','')
                title_url=question['object']['question']['url'].replace('api','www').replace('questions','question')
                # print(title,title_url)
                questionDict[title]=title_url
            except:
                title=question['highlight']['title'].replace('<em>','').replace('</em>','')
                title_url=question['object']['url'].replace('api','zhuanlan').replace('articles','p')
                # print(title,title_url)
                articleDict[title]=title_url
                pass
    # print(new_question['data'][0][])
    return questionDict,articleDict


def main():
    for work in works[5:]:
        print(work)
        workPath=projectPath+work
        os.mkdir(workPath)
        questionDict, articleDict = findresult(work,80)
        with open(workPath+'\\dict.txt','w') as f:
            for name,url in articleDict.items():
                try:
                    f.write(name+'     '+url+'\r\n')
                except:
                    logging.warning(url)
            f.write('==========================\r\n')
            for name,url in questionDict.items():
                try:
                    f.write(name+'     '+url+'\r\n')
                except:
                    logging.warning(url)
        # print(questionDict)
        # print(articleDict)
        for name,url in articleDict.items():
            collectZL(name,url,workPath)
            time.sleep(0.1)
        questionNum=0
        for name,url in questionDict.items():
            filename=workPath+'\\question'+str(questionNum)+'.txt'
            print(questionNum)
            collectQ(name,url,filename,60)
            questionNum+=1
            time.sleep(0.1)

if __name__ == '__main__':
    import requests
    import bs4
    import re
    import logging,os,time
    #logging.basicConfig(filename='G:\study\研一\数据挖掘\\failLog.log', level=logging.DEBUG, filemode='w')
    main()
