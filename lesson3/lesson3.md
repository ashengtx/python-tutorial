## 3 python 网络爬虫介绍

**什么是网络爬虫？**

简单的讲，就是能够自动抓取网页信息的程序。

主要过程：

- 向服务器发送请求
- 请求数据  
- 解析数据
- 提取信息


### 3.1 糗事百科笑话爬取

总体效果，执行

```
python get_jokes.py
```

#### 3.1.1 get html

**urlopen**

```py
from urllib.request import urlopen

def get_html(url):
    """
    请求url，返回html
    """
    html = urlopen(url).read().decode('utf8')
    return html

if __name__ == "__main__":

    url = "https://baike.baidu.com/item/Python/407313"
    foutput = open('../txt/output.txt', 'w')
    print(get_html(url), file=foutput) 
    foutput.close()
```

**使用Request带上headers**

有些网站需要在headers里设置User-Agent，模拟浏览器请求。

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

if __name__ == "__main__":

    url = "https://www.qiushibaike.com/hot/page/1/"
    foutput = open('../txt/output.txt', 'w')
    print(get_html(url), file=foutput)
    foutput.close()
```

#### 3.1.2 BeautifulSoup-html解析

安装BeautifulSoup

```
pip install beautifulsoup4
```

测试是否安装成功，在python shell执行

```py
>>> from bs4 import BeautifulSoup
```

将html转成BeautifulSoup对象

```py
html = get_html(url)
bsObj = BeautifulSoup(html, 'html.parser')
print(bsObj.h1) # 如果有相同的标签，只返回第一个
```

output
```
<h1>糗事百科</h1>
```

html文档由一系列标记标签组成，这些标签构成一个树形结构，根结点是```<html>```标签。

文件```html/basic.html```给出了一个简单的例子。

还可以将文档输出到本地文件观察。
```py
foutput = open('../txt/output.txt', 'w')
html = get_html(url)
bsObj = BeautifulSoup(html, 'html.parser')
print(html, file=foutput)
```

我们现在获得了返回的html文档，如何获取笑话的文本内容？
方法一： 通过html标签的class属性或id属性
方法二： 正则表达式

先介绍方法一

#### 3.1.3 find() and findAll() with BeautifulSoup

每个html标签都所有一系列属性，id属性是唯一的，class属性不唯一，但是有很强的类别特征，常用来定位。

通过观察，发现笑话文本都在class="content"的div标签内。
```
<div class="content">
<span>
通过关系，在一家售楼处做一些零散工作。就刚刚，前台小月不知道范了哪根神经，对着镜子画了一副自画像。恰巧门口的保安进来喝水，高高帅帅的那种，小月搭讪，帅哥，看我的自画像，逼真吗？保安一笑，真的明明在你身上，画像上哪来真的。小月一愣神，反应过来对着保安裆下就是一记佛山无影脚，还好不是很着实，小哥急忙捂住说到：幸亏今天是个好日子。月红着脸问是啥好日子。‘剩蛋啊，不然我的蛋真的要保不住了！哄笑……’

</span>

</div>
```

我们可以通过BeautifulSoup的findAll()方法找到所有这样的标签
```py
html = get_html(url)
bsObj = BeautifulSoup(html, 'html.parser')
jokes = bsObj.find_all('div', {"class":"content")})
print("这个页面总共有%d个笑话。" % len(jokes))
print("第一个div标签对象\n\n", jokes[0])
print("对象类型： ", type(jokes[0]))
```

output:
```
这个页面总共有25个笑话。
第一个div标签对象

 <div class="content">
<span>


（很长很真实也很有感情。）<br/>记得八年前，我上小学五年级，全家一起来到了开封县。这是个陌生的城市。爸爸怕影响我学习，给我报了英语补习班。每天最开心的事情就是，晚上补习班放学，看见妈妈在门口笑着等我。然后回家的路上，妈妈都会带我到一个打烧饼的阿姨那里。五毛钱一个烧饼，一块钱一个牛排。买给我吃……（在哪个时候，可是难得的美味）<br/>第一开始，我都会没良心的吃独食，吃完还想吃。后来有一天，我刚拿到烧饼要咬第一口，抬头看见妈妈在看我吃。<br/>我问妈妈要不要吃。妈妈说“宝贝，妈妈看你吃就很开心。”<br/>我把烧饼全是芝
…
</span>
<span class="contentForAll">查看全文</span>
</div>
对象类型：  <class 'bs4.element.Tag'>
```

这里的jokes是找到的div标签对象组成的list.

```py
findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)
```

二者的区别：

- findAll是找到所有标签
- find只找到第一个标签

用法：

第一个参数tag是要找的标签名，传入对应字符串，比如这里的```’div‘```
第二个参数attributes是要找的标签的属性，传入一个dict。也就是说，理论上我们可以指定多个属性。
其他参数有需要的时候再去查文档。

（题外话：掌握常用的就行，毕竟，学海无涯...）


#### 3.1.4 get_text()

获取对应标签之后，只想要里面的文本，可以用标签对象的get_text()方法

```py
joke_text = jokes[0].get_text().strip()
print(joke_text)
```

output
```
（很长很真实也很有感情。）记得八年前，我上小学五年级，全家一起来到了开封县。这是个陌生的城市。爸爸怕影响我学习，给我报了英语补习班。每天最开心的事情就是，晚上补习班放学，看见妈妈在门口笑着等我。然后回家的路上，妈妈都会带我到一个打烧饼的阿姨那里。五毛钱一个烧饼，一块钱一个牛排。买给我吃……（在哪个时候，可是难得的美味）第一开始，我都会没良心的吃独食，吃完还想吃。后来有一天，我刚拿到烧饼要咬第一口，抬头看见妈妈在看我吃。我问妈妈要不要吃。妈妈说“宝贝，妈妈看你吃就很开心。”我把烧饼全是芝
…
```

关于get_text()的使用：
在标签下操作永远比处理纯文本要容易，因此，尽量在最后一个用get_text()，因为它会去除该标签下的子标签，比如这里，div标签下的span标签被去掉了。

最后，我们可以将笑话文本保存到本地文件

```py
url = "https://www.qiushibaike.com/hot/page/1/"
foutput = open('../txt/jokes1.txt', 'w')
jokes = get_jokes(url)
n = 1
for joke in jokes:
    print("joke ", n, file=foutput)
    print(joke, file=foutput)
    n += 1
foutput.close()
```

#### 3.1.5 正则表达式

除了用BeautifulSoup解析html文档来获得我们想要的内容，还有一种文本处理的常用方法，就是正则表达式。

这有个[正则表达式30分钟入门教程](https://deerchao.net/tutorials/regex/regex.htm)

简单的讲，正则表达式就是用来匹配具有某种规则文本的代码。

我们先看看用正则表达式获取笑话文本如何操作

```py
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
```

[跨行匹配问题](http://www.lfhacks.com/tech/python-re-single-multiline)

### 3.2 豆瓣电影排行爬取

比如，我们点开[豆瓣电影排行榜](https://movie.douban.com/chart)，右边有许多分类，我们选择第一个剧情分类点开。出现按评分从高到低排序的电影。

我们想要获取这些电影相关信息以及评分。

根据前面所学，本能的想拿url试一下

```py
from utils import *

def get_movies():
    """
    查看输出结果，会发现，没有电影信息
    """
    type_url = "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action="
    html = get_html(base_url)
    foutput = open('../txt/output.txt', 'w')
    print(html, file=foutput)

if __name__ == '__main__':
    
    get_movies()

```

说明电影信息不是由请求这个url产生的

这时候可以使用chrome的开发者工具来分析具体是哪个请求，按F12打开开发者工具。

分析出实际返回电影信息的请求其实是
```
https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20
```

试一下这个新的url

```py
from utils import *

def get_movies2():
    """
    获得电影信息
    """
    base_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'

    html = get_html(base_url)
    foutput = open('../txt/output.txt', 'w')
    print(html, file=foutput)

if __name__ == '__main__':

    get_movies2()
```

如果返回的是json格式的字符串，可以直接用python的json模块解析，但是这个返回的比较特殊，它是多个json格式字符串在一个列表里，然后一整个列表又是字符串。

暂时没找到优雅的解析方法，不过可以用正则表达式解析出单独的json字符串，再解析json.

```py
import re, json
from utils import *

def get_movies2():
    """
    获得电影信息
    """
    base_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'

    html = get_html(base_url)
    foutput = open('../txt/output.txt', 'w')
    print(html, file=foutput)
    pattern = r'(\{"rating.*?\})[(,\{)\]]'
    movies = re.findall(pattern, html) 
    for movie in movies:
        print(json.loads(movie))
    print(len(movies))


if __name__ == '__main__':

    get_movies2()

```

将json样式的字符串解析成json对象之后，就可以通过dict的方式来访问。

```py
import re, json
from utils import *

def get_movies2():
    """
    """
    base_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'

    html = get_html(base_url)
    foutput = open('../txt/output.txt', 'w')
    print(html, file=foutput)
    pattern = r'(\{"rating.*?\})[(,\{)\]]'
    movies = re.findall(pattern, html) 
    result = []
    for movie in movies:
        data = json.loads(movie)
        title = data['title']
        rating = data['rating'][0]
        #print(title,rating)
        result.append((title, rating))
    return result

if __name__ == '__main__':

    for title, rating in get_movies2():
        print(title, rating)
```
