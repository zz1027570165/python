import json
import re

import requests
from bs4 import BeautifulSoup


def main(page):
    url = 'http://e.dangdang.com/list-ZTXYTL-dd_sale-0-' + str(page) + '.html'
    html = request_dandan(url)
    items = parse_result(html)  # 解析过滤我们想要的信息
    for item in items:
        write_item_to_file(item)

# 对该网站进行分析，如果返回200，也就返回html内容
def request_dandan(url):
   try:
       response = requests.get(url)
       if response.status_code == 200:
           return response.text
   except requests.RequestException:
       return None


def parse_result(html):
    soup = BeautifulSoup(html, 'lxml')
 #  pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
 #  items = re.findall(pattern,html)
 #   for item in items:
 #       yield {
 #           'range': item[0],
 #           'iamge': item[1],
 #           'title': item[2],
 #           'recommend': item[3],
 #           'author': item[4],
 #           'times': item[5],
 #           'price': item[6]
 #       }
 #       print(item)
    items = soup.find(id = 'book_list').find_all(class_ = 'bookinfo')
    for item in items:
        yield {
            'title' : item.find(class_='title').string,
            'author' : item.find(class_='author').string,
            'now' : item.find(class_='now').string,
            'des' : item.find(class_='des').string
        }
        print(item)

def write_item_to_file(item):
   print('开始写入数据 ====> ' + str(item))
   with open('book2.txt', 'a', encoding='UTF-8') as f:
       f.write(json.dumps(item, ensure_ascii=False) + '\n')
       f.close()


if __name__ == "__main__":
  # for i in range(1,26):
       main(1)

