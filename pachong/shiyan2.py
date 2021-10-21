import requests
import parsel
import os

# ua伪装
headers = {

    'User-Agent': 'asfasf'
}


# 指定url
def xiaoshuo(url1):
    # 发起请求,接受返回对象.
    response = requests.get(url=url1, headers=headers)
    # 对指定的url发起请求对应的url时携带参数的,并且请求过程中处理了内容
    response.encoding = 'utf-8'
    response = response.text
    nei = parsel.Selector(response)  # 解析
    title = nei.css('h1::text').get()  # 抓取标题
    title1 = nei.css('span.c9::text').get()  # 章节标题（这里可以自己找一个小说主题，现在我用的是书号来写文件夹。）
    print('正在下载:', title)
    xiaoshuo = nei.css('p::text').getall()  # 抓取内容
    print('获取小说内容完成')
    text = ''
    for i in xiaoshuo:
        text += i + '\n'
    # 存储持久化数据
    # 通过try防止报错停止爬取
    try:
        os.makedirs(title1, exist_ok=True)  # 写入文件夹
        with open(os.path.join(title1, title + '.txt'), 'w', encoding='utf') as f:
            f.write(text)
        print('写入成功')
        print('\n')
    except:
        pass


# 进行全部文本爬取
if __name__ == '__main__':
    for i in range(0, 500):
        url = 'https://www.17k.com/all/book/2_24_0______1.html'
    url.replace('_1', '_%d' % (i))
    response = requests.get(url=url, headers=headers)
    html = response.text
    jiexi = parsel.Selector(html)  # 解析网页
    # 获得每一本小说的目录
    huodelianjie = jiexi.css('dl>dt>a::attr(href)').getall()  # 这里获得链接有缺漏，在这里补一些前缀
    print('获得小说链接成功')
    https = 'https:'
    for i in huodelianjie:
        a = https + i
        response2 = requests.get(a, headers=headers)
        response2.encoding = 'utf-8'
        response2 = response2.text
        nei = parsel.Selector(response2)
        mulu = nei.css('dt.read>a::attr(href)').getall()  # 这里也是有缺漏
        https1 = 'https://www.17k.com'
        for url1 in mulu:
            b = https1 + url1
            # 解析小说里面目录的网页
            response3 = requests.get(b, headers=headers)
            response3.encoding = 'utf-8'
            response3 = response3.text
            t = parsel.Selector(response3)  # 解析网页
            zhangjie = t.css('dl.Volume>dd>a::attr(href)').getall()  # 还有这里也有缺漏
            https1 = 'https://www.17k.com'
            for url1 in zhangjie:
                c = https1 + url1
                xiaoshuo(c)  # 返回小说每一个章节链接
