import json
import re
from utils import *

url = "https://movie.douban.com/chart"

def get_movies():
    """
    查看输出结果，会发现，没有电影信息
    """
    type_url = "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action="
    html = get_html(base_url)
    foutput = open('../txt/output.txt', 'w')
    print(html, file=foutput)

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
    result = []
    for movie in movies:
        data = json.loads(movie)
        title = data['title']
        rating = data['rating'][0]
        #print(title,rating)
        result.append((title, rating))
    return result

def get_movies3():
    """
    后来发现json可以直接解析这种格式，我函数名写错了
    json.loads(html) loads是正确的，直接解析json字符串
    json.load(file) load用来解析json格式的文件
    """
    base_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'

    html = get_html(base_url)
    foutput = open('../txt/output.txt', 'w')
    print(html, file=foutput)
    movies = json.loads(html)
    result = []
    for movie in movies:
        title = movie['title']
        rating = movie['rating'][0]
        #print(title,rating)
        result.append((title, rating))
    return result

if __name__ == '__main__':

    for title, rating in get_movies3():
        print(title, rating)


