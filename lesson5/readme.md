# python爬虫进阶与文本处理

## 博客园博客文章爬取

博客园[链接](http://www.cnblogs.com/)

任务：爬取某位博主的全部博客文章

### 访问博客网址，进行分析

http://www.cnblogs.com/zhaopei/

观察发现，博主博客首页显示了十来篇文章的摘要，点击文章标题，就进入文章具体页面，而点击右下角的下一页，就会来到第二页的文章列表。

下面我们用代码模拟这些操作。

### 获取博客首页的html

```py
from urllib.request import Request, urlopen

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

def get_html(url):
    """
    请求url，返回html
    """

    req = Request(url, headers=headers)  
    html = urlopen(req).read().decode('utf8')
    return html

def main():
    """
    主程序
    """

    user_name = 'zhaopei'
    start_url = 'http://www.cnblogs.com/' + user_name

    print(get_html(start_url))

if __name__ == '__main__':
    main()
```

### 获取当前页面所有文章的链接

要想获取所有的文章内容，需要获取所有的文章链接，我们先获取当前页面所有文章的链接。

右键点击第一篇文章的标题，选择“审查元素”，可以看到，文章的链接为

```
http://www.cnblogs.com/zhaopei/p/why_write_blog.html
```

通过观察所有文章链接，发现文章的链接有固定的模式

我们可以通过正则表达式来匹配这些链接

```py
import re
from urllib.request import Request, urlopen

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
    return links

def main():
    """
    主程序
    """

    user_name = 'zhaopei'
    start_url = 'http://www.cnblogs.com/' + user_name
    html = get_html(start_url)
    links = get_article_links(html, user_name)
    for link in links:
        print(link)

if __name__ == '__main__':
    main()
```

output

```
http://www.cnblogs.com/zhaopei/p/why_write_blog.html
http://www.cnblogs.com/zhaopei/p/why_write_blog.html
http://www.cnblogs.com/zhaopei/p/4192823.html
http://www.cnblogs.com/zhaopei/p/4192823.html
http://www.cnblogs.com/zhaopei/p/SSO.html
http://www.cnblogs.com/zhaopei/p/SSO.html
http://www.cnblogs.com/zhaopei/p/dispose-on-dbcontext.html
http://www.cnblogs.com/zhaopei/p/dispose-on-dbcontext.html
http://www.cnblogs.com/zhaopei/p/auto-injection.html
http://www.cnblogs.com/zhaopei/p/auto-injection.html
...
```

发现有重复，用```set()```去个重

```py
def get_article_links(html, user_name):
    """
    获取当前页面的所有文章链接
    """

    pattern = r'href="(http://www\.cnblogs\.com/'+user_name+r'/p/.*?\.html)"'
    links = re.findall(pattern, html)
    return list(set(links))
```

### 获取下一页所有文章的链接

先用正则表达式获取下一页的链接

```py
def get_next_page(html):
    pattern = r'<a href="(.*?)">下一页</a>'
    result = re.findall(pattern, html)
    link_next = result[0]
    print(link_next)
```

output

```
http://www.cnblogs.com/zhaopei/default.html?page=2
```

进一步获取下一页的html

```py
def get_next_page(html):
    """
    返回下一页的html
    """

    pattern = r'<a href="(.*?)">下一页</a>'
    result = re.findall(pattern, html)
    link_next = result[0]
    html_next = get_html(link_next)
    
    return html_next
```

然后我们就可以用之前定义的函数```get_article_link(html, user_name)```获取这个页面的所有文章链接

```py
def main():
    """
    主程序
    """

    user_name = 'zhaopei'
    start_url = 'http://www.cnblogs.com/' + user_name
    html = get_html(start_url)
    links = get_article_links(html, user_name)
    for link in links:
        print(link)

    html_next = get_next_page(html)
    links_next = get_article_links(html_next, user_name)
    print("------------------------")
    for link in links_next:
        print(link)
```

output

```
http://www.cnblogs.com/zhaopei/p/download.html
http://www.cnblogs.com/zhaopei/p/netcore.html
http://www.cnblogs.com/zhaopei/p/SSO.html
http://www.cnblogs.com/zhaopei/p/auto-injection.html
http://www.cnblogs.com/zhaopei/p/6922522.html
http://www.cnblogs.com/zhaopei/p/4192823.html
http://www.cnblogs.com/zhaopei/p/upload.html
http://www.cnblogs.com/zhaopei/p/authorize-1.html
http://www.cnblogs.com/zhaopei/p/7397402.html
http://www.cnblogs.com/zhaopei/p/why_write_blog.html
http://www.cnblogs.com/zhaopei/p/dispose-on-dbcontext.html
http://www.cnblogs.com/zhaopei/p/netcore2.html
------------------------
http://www.cnblogs.com/zhaopei/p/async_two.html
http://www.cnblogs.com/zhaopei/p/6623460.html
http://www.cnblogs.com/zhaopei/p/strategy.html
http://www.cnblogs.com/zhaopei/p/async_one.html
http://www.cnblogs.com/zhaopei/p/Single.html
http://www.cnblogs.com/zhaopei/p/IQueryable-IQueryProvider.html
http://www.cnblogs.com/zhaopei/p/Indexes.html
http://www.cnblogs.com/zhaopei/p/UnitTesting.html
http://www.cnblogs.com/zhaopei/p/variability.html
http://www.cnblogs.com/zhaopei/p/6625075.html
```

### 获取所有页面文章的链接

获取所有页面，可以通过不断的获取下一页来办到，就像我们手动点击下一页，一直点到没有下一页为止。这里需要修改一下```get_next_page()```函数，使得没有下一页的时候，返回一个信号。

```py
def get_next_page_with_stop(html):
    """
    返回下一页的html，如果没有下一页，返回False
    """

    pattern = r'<a href="(.*?)">下一页</a>'
    result = re.findall(pattern, html)
    if result == []: # 没有下一页的时候，会返回一个空的list
        return False # 直接返回False，下面不再执行

    link_next = result[0]
    html_next = get_html(link_next)
    
    return html_next
```

然后，就可以获取所有页面的链接

```py
def get_all_article_links(start_url, user_name):
    """
    获取某个用户所有的文章链接
    """
    all_links = []

    url = start_url + user_name
    html = get_html(url)
    links = get_article_links(html, user_name)
    all_links.extend(links) 

    html_next = get_next_page_with_stop(html)
    while html_next:
        links_next = get_article_links(html_next, user_name)
        all_links.extend(links_next)
        html_next = get_next_page_with_stop(html_next)

    return all_links

def main():
    """
    主程序
    """
    start_url = 'http://www.cnblogs.com/'
    user_name = 'zhaopei'

    links = get_all_article_links(start_url, user_name)
    for link in links:
        print(link)

if __name__ == '__main__':
    main()
```

然后，发现报错了

output

```
UnicodeEncodeError: 'ascii' codec can't encode characters in position 34-36: ordinal not in range(128)
```

分析发现，是从```get_next_page_with_stop```的```html_next = get_html(link_next)```开始报错的，我们先看看这个匹配到的下一页链接对不对

```py
def get_next_page_with_stop(html):
    """
    返回下一页的html，如果没有下一页，返回False
    """

    pattern = r'<a href="(.*?)">下一页</a>'
    result = re.findall(pattern, html)
    if result == []: # 没有下一页的时候，会返回一个空的list
        return False # 直接返回False，下面不再执行

    link_next = result[0]
    print(link_next) # 看看这个链接长啥样
    html_next = get_html(link_next) # 这一步报错
    
    return html_next
```

output

```
http://www.cnblogs.com/zhaopei/default.html?page=1">上一页</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=1">1</a>&nbsp;2&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=3">3</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=4">4</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=5">5</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=6">6</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=7">7</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=8">8</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=9">9</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=3
```

原来是我们这里的正则匹配不正确

它完整的字符串是这样的

```
<a href="http://www.cnblogs.com/zhaopei/default.html?page=1">上一页</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=1">1</a>&nbsp;2&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=3">3</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=4">4</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=5">5</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=6">6</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=7">7</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=8">8</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=9">9</a>&nbsp;<a href="http://www.cnblogs.com/zhaopei/default.html?page=3">下一页</a>
```

解决，先匹配所有的```<a>.*?</a>```链接，再去这些链接里去找出下一页的链接

```py
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

def main():
    """
    主程序
    """
    start_url = 'http://www.cnblogs.com/'
    user_name = 'zhaopei'

    links = get_all_article_links(start_url, user_name)
    print("一共有%d个文章链接" % len(links))
    for link in links:
        print(link)
```

output

```
一共有85个文章链接
http://www.cnblogs.com/zhaopei/p/SSO.html
http://www.cnblogs.com/zhaopei/p/7397402.html
http://www.cnblogs.com/zhaopei/p/6922522.html
http://www.cnblogs.com/zhaopei/p/download.html
http://www.cnblogs.com/zhaopei/p/upload.html
http://www.cnblogs.com/zhaopei/p/auto-injection.html
http://www.cnblogs.com/zhaopei/p/netcore2.html
http://www.cnblogs.com/zhaopei/p/authorize-1.html
http://www.cnblogs.com/zhaopei/p/4192823.html
http://www.cnblogs.com/zhaopei/p/why_write_blog.html
...
```

### 获取所有文章的文本

首先，获取文章页面的html

```py
def get_article(url):
    """
    访问文章链接，返回文章标题和内容
    """

    html = get_html(url) 
```

观察发现，文章的标题是在标签```<a id="cb_post_title_url"> </a>```里面，而文章的正文是在标签```<div id="cnblogs_post_body"> </div>```里面。我们可以把html转成BeautifulSoup对象的方式，再通过BeautifulSoup的find方法来获取这些标签里的文本。

我们定义两个函数分别获取文章标题和正文

```py
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
```

对所有的文章链接执行这个操作，然后将文章保存到本地文件

```py
def get_all_articles(start_url, user_name):
    """
    获取所有文章，并保存到本地
    """

    links = get_all_article_links(start_url, user_name)

    with open("articles.txt", 'w', encoding='utf8') as file_output:
        for link in links:
            result = get_article(link)
            string = result['title'] + '\t' + result['body']
            print(string, file=file_output)

    return True

def main():
    """
    主程序
    """
    start_url = 'http://www.cnblogs.com/'
    user_name = 'zhaopei'

    get_all_articles(start_url, user_name)
```

居然报错了

```
AttributeError: 'NoneType' object has no attribute 'get_text'
```

原来是在获取标题或者正文的文本的时候，没有找到对应的标签，也就是说```
bsObj.find(id="cb_post_title_url")```或者```bsObj.find(id='cnblogs_post_body')```没有找到，因此返回了一个```'NoneType' object```，而这个```'NoneType' object```它没有```get_text()```这个方法。

那为什么会没找到呢？

我们把那个链接print出来看看

```py
def get_all_articles(start_url, user_name):
    """
    获取所有文章，并保存到本地
    """

    links = get_all_article_links(start_url, user_name)

    with open("articles.txt", 'w', encoding='utf8') as file_output:
        for link in links:
            try:
                result = get_article(link)
            except:
                print(link)
                continue # 跳过，直接进入下一轮循环
            string = result['title'] + '\t' + result['body']
            print(string, file=file_output)

    return True
```

这里用到了python的异常处理

```py
try:
    #1 do something
except:
    #2 do something else
```

如果```#1```出现异常，则执行```#2```，程序不会终止。

print之后发现出现异常的链接是

```
http://www.cnblogs.com/zhaopei/p/4920147.html
```

到这里，我们就获取了这位博主所有的博客文章

## 简单的文本处理
