import os
import requests
import json
import re


def get_lol_image():
    url = "https://lol.qq.com/biz/hero/champion.js"
    ht = requests.get(url)

    regex = '"keys":(.*?),"data"'

    list_a = re.findall(regex, ht.text)
    print(list_a[0])
    dict_a = json.loads(list_a[0])

    list_b = []
    for hero_id in dict_a:

        for i in range(20):
            i = str(i)
            if len(i) == 1:
                hero_n = "00" + i
            elif len(i) == 2:
                hero_n = "0" + i
            hero_s = hero_id + hero_n
            hero_u = 'https://game.gtimg.cn/images/lol/act/img/skin/big' + hero_s + '.jpg'

            list_b.append(hero_u)

    root = "D:/lol/images/"
    for a in dict_a:
        if not os.path.exists(root):
            os.makedirs(str(root) + str(dict_a[a]) + '/')
        list_c = []
    for a in dict_a:
        for j in range(20):
            filename = "D:/lol/images/" + dict_a[a] + "/" + dict_a[a] + str(j) + ".jpg"
            list_c.append(filename)

    n = 0;
    for b in list_b:
        r = requests.get(b)
        n += 1
        if r.status_code == 200:
            print("ÕýÔÚÏÂÔØ%s" % list_c[n])

            with open(list_c[n], "wb") as f:
                f.write(r.content)
    f.close()


get_lol_image()
