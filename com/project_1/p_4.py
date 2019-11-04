import requests

# 声明一个run方法
def run(self,target_url, headers):
    response = requests.get("https://www.meizitu.com/a/4894.html")
    # wb是二进制写入
    with open("meizi.jpg","wb") as f:
        f.write(response.content)
        f.close

if __name__ == "__main__":   #主程序入口
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'HOST': 'https://www.meizitu.com'
    }
    target_url = 'https://www.meizitu.com/a/4894.html'  # 图片集和列表规则
    run(target_url,headers)    #调用上面的run方法