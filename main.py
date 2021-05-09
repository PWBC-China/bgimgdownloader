import requests
import json
import os

url = 'https://www.quanjing.com/Handler/SearchUrl.ashx'
user_word = input('请输入您要查询下载的图片关键词：')
print('正在设置网址请求格式……')
for i in range(1,10):
    params={
        'q': user_word
    }
    headers={
        'Referer':'https://www.quanjing.com/search.aspx?q=%E6%9C%88%E4%BA%AE',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    print('设置完毕！')
    html = requests.get(url,params=params,headers=headers).text
    start = html.find('{"pageindex')
    end = html.find('}]}')+len('}]}')
    data = json.loads(html[start:end])['imglist']
    print('已经请求到数据包！')
    print('开始解析……')
    for d in data:
        pic_id = d['pic_id']
        pic_url = d['imgurl']
        print('开始下载……')

        if not os.path.exists('下载的图片'):
            os.mkdir('下载的图片')
        with open('下载的图片/{}.jpg'.format(pic_id),'wb') as f:
            f.write(requests.get(pic_url).content)

        print('下载完成，请至程序运行目录下的【下载的图片】文件夹查看！共要下载100张图片，请稍等……')