import json
import requests
import urllib.error
import urllib.request
from bs4 import BeautifulSoup
import pymysql


def get_page(headers, url):
    try:
        respons = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(respons)
        result = html.read().decode('utf-8')
        soup = BeautifulSoup(result, 'lxml')
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "1", "test")
        for i in soup.find_all('',style='color:white; font-size:18px;  font-weight:bold;line-height:30px; padding-right:8px;'):
            print(i.string)
            conDb(i.string,db)

        # 关闭数据库连接
        db.close()



    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print('错误原因是' + str(e.reason))
    except urllib.error.HTTPError as e:
        if hasattr(e, 'code'):
            print('错误状态码是' + str(e.code))
    else:
        print('请求成功通过。')

# 数据库操作
def conDb(msg,db):

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 插入语句
    sql = "insert into test_p1(msg) values('%s')" %(msg)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


if __name__ == '__main__':
    headers = {
        'User_Agent': 'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    for i in range(1,11):
        url = 'http://www.2140000.com/mu.asp?n=' + str(i)
        get_page(headers, url)

