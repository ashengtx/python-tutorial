import re, jieba
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from collections import defaultdict

import jieba.analyse

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

def get_html(url):
    """
    请求url，返回html
    """

    req = Request(url, headers=headers)  
    html = urlopen(req).read().decode('utf8')
    return html

def get_article_links(html, user_name):
    """
    获取当前页面的所有文章链接
    """

    pattern = r'href="(http://www\.cnblogs\.com/'+user_name+r'/p/.*?\.html)"'
    links = re.findall(pattern, html)
    return list(set(links))

def get_next_page(html):
    """
    返回下一页的html
    """

    pattern = r'<a href="(.*?)">下一页</a>'
    result = re.findall(pattern, html)
    link_next = result[0]
    html_next = get_html(link_next)
    
    return html_next

def get_next_page_with_stop(html):
    """
    返回下一页的html，如果没有下一页，返回False
    """

    pattern = r';?<a href="(.*?)">下一页</a>'
    result = re.findall(pattern, html)
    if result == []: # 没有下一页的时候，会返回一个空的list
        print("没有下一页了")
        return False # 直接返回False，下面不再执行

    link_next = result[0]
    print(link_next)
    html_next = get_html(link_next)
    
    return html_next

def get_next_page_with_stop2(html):
    """
    先匹配所有tag a，再去这些tag里找出下一页的链接

    返回下一页的html，如果没有下一页，返回False
    """
    pattern1 = r'<a.*?>.*?</a>'
    all_links = re.findall(pattern1, html)
    
    pattern2 = r'<a href="(.*)">下一页</a>'
    result = []
    for link in all_links:
        find_result = re.findall(pattern2, link)
        if find_result:
            result = find_result
            break # 停止循环

    if result == []: # 没有下一页的时候，会返回一个空的list
        #print("没有下一页了")
        return False # 直接返回False，下面不再执行

    link_next = result[0]
    html_next = get_html(link_next)
    
    return html_next

def get_all_article_links(start_url, user_name):
    """
    获取某个用户所有的文章链接
    """
    all_links = []

    url = start_url + user_name
    html = get_html(url)
    links = get_article_links(html, user_name)
    all_links.extend(links)

    html_next = get_next_page_with_stop2(html)
    while html_next:
        links_next = get_article_links(html_next, user_name)
        all_links.extend(links_next)
        html_next = get_next_page_with_stop2(html_next)

    return all_links

def get_post_title(bsObj):
    return bsObj.find(id="cb_post_title_url").get_text()

def get_post_body(bsObj):
    return bsObj.find(id='cnblogs_post_body').get_text()

def get_article(url):
    """
    访问文章链接，返回文章标题和内容
    """

    html = get_html(url) 
    bsObj = BeautifulSoup(html, 'html.parser')

    title = get_post_title(bsObj)
    body = get_post_body(bsObj)

    result = {}
    result['title'] = title
    result['body'] = body

    return result # 以词典的形式返回

def get_all_articles(start_url, user_name):
    """
    获取所有文章，并保存到本地
    """

    links = get_all_article_links(start_url, user_name)

    with open("../txt/articles.txt", 'w', encoding='utf8') as file_output:
        n = 0
        for link in links:
            try:
                result = get_article(link)
            except:
                print("异常链接： ", link)
                continue
            n += 1
            print("article ", n, file=file_output)
            print("title: " + result['title'], file=file_output)
            print("body: \n" + result['body'], file=file_output)

    return n

def scrap_article():
    """
    文章爬取
    """
    start_url = 'http://www.cnblogs.com/'
    user_name = 'zhaopei'

    n = get_all_articles(start_url, user_name)
    print("从博客%s上一共爬取%d篇文章" % (start_url+user_name, n))

def load_stop_words():
    """
    载入停用词
    """
    stop_words = []
    with open('../dict/stop_words.txt', 'r', encoding='utf8') as f:
        for line in f:
            stop_words.append(line.strip())
    return stop_words

def get_word_freq():
    """
    统计词频
    """
    stop_words = load_stop_words()
    word_freq = defaultdict(int) # 这个dict的value默认为0
    with open('../txt/articles.txt', 'r', encoding='utf8') as f:
        for line in f:
            if line.startswith('article') or line.startswith('body:'):
                continue
            if line.startswith('title:'):
                line = line.replace('title:', '')
            # 对句子分词
            result = jieba.cut(line.strip())
            for word in result:
                # 去掉停用词
                if word in stop_words:
                    continue
                word_freq[word] += 1
    return word_freq

def show_word_freq(word_freq, min_freq=0):
    """
    将词频排序，并从高到低输入
    """
    word_freq_sorted = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    for word, freq in word_freq_sorted:
        print(word, freq)
        if freq < min_freq:
            break

    return True

def save_word_freq_to_csv(word_freq, min_freq=0):
    """
    将词频排序，并从高到低，保存到csv文件
    """
    word_freq_sorted = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    with open('../csv/word_freq.csv', 'w', encoding='utf8') as f_csv:
        for word, freq in word_freq_sorted:
            print(word, ',', freq, file=f_csv)
            if freq < min_freq:
                break
    return True

def preprocess():
    """
    """
    stop_words = load_stop_words()
    file_output = open('../txt/articles_seg.txt', 'w', encoding='utf8')
    with open('../txt/articles.txt', 'r', encoding='utf8') as f:
        for line in f:
            if line.startswith('article') or line.startswith('body:'):
                continue
            if line.startswith('title:'):
                line = line.replace('title:', '')
            # 对句子分词
            result = jieba.cut(line.strip())
            result = [word for word in result if word not in stop_words]
            # 可能一整行都是停用词，跳过
            if len(result) == 0:
                continue
            print(' '.join(list(result)), file=file_output)
    file_output.close()
    return True

def get_key_word_base_tfidf():
    """
    基于 TF-IDF 算法的关键词抽取
    """
    content = open('../txt/articles_seg.txt', 'r', encoding='utf8').read()

    tags = jieba.analyse.extract_tags(content, topK=20)

    for tag in tags:
        print(tag)

def analyse_each_article(start_url, user_name):
    """
    分析每篇文章的关键词
    """

    links = get_all_article_links(start_url, user_name)

    stop_words = load_stop_words()
    with open("../txt/articles_analyse.txt", 'w', encoding='utf8') as file_output:
        n = 0
        for link in links:
            try:
                result = get_article(link)
            except:
                print("异常链接： ", link)
                continue
            sentences = []
            for line in result['body'].split('\n'):
                sent = [word for word in jieba.cut(line) \
                             if word not in stop_words]
                if len(sent) > 0:
                    sentences.append(' '.join(sent))
            tags = jieba.analyse.extract_tags('\n'.join(sentences), topK=20)
            n += 1
            print('title %d: %s' % (n, result['title']), file=file_output)
            print('，'.join(tags), file=file_output)

    return True

def main():
    """
    主程序
    """
    #scrap_article()
    #word_freq = get_word_freq()
    #print(word_freq)
    #show_word_freq(word_freq, min_freq=15)
    #save_word_freq_to_csv(word_freq, min_freq=15)
    #preprocess()
    #get_key_word_base_tfidf()

    start_url = 'http://www.cnblogs.com/'
    user_name = 'zhaopei'
    analyse_each_article(start_url, user_name)

if __name__ == '__main__':
    main()
