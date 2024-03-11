#!/usr/bin/env python
# coding:utf8

from urllib import request
from urllib.parse import quote
import string
import json
from bs4 import BeautifulSoup
import codecs
from get_character import get_character_arr
import os

if not os.path.exists("./images"):
    os.mkdir("./images")

headers = {}
headers[
    "User-Agent"
] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"


# 对于每一个人物，查百度百科，收集基础信息，还有图片，将数据存储在data.json中
def get_json(character_arr):
    data = {}
    for i in set(character_arr):
        print("正在抓取[" + i + "]的人物信息")
        url = r"https://baike.baidu.com/item/" + i
        url = quote(url, safe=string.printable)
        req = request.Request(url, headers=headers)
        response = request.urlopen(req, timeout=20)

        try:
            html = response.read().decode("utf-8")
            soup = BeautifulSoup(
                html,
                "html.parser",
            )
            # 当前在images文件夹下
            pic_name = str(i) + ".jpg"
            res = soup.find(class_="abstractAlbum_ZqtVr")
            img_src = res.find("img").get("src")
            request.urlretrieve(img_src, pic_name)
        except:
            print("找不到图片")
        character_info = soup.find_all(class_="itemWrapper_OC3qU")
        item = {}
        for div in character_info:
            key = div.find("dt").get_text().replace("\xa0", "")
            spans = div.find_all("span")
            value = ""
            for span in spans:
                if span.find("sup"):
                    continue
                elif span.find("a"):
                    value = value + span.find("a").get_text()
                else:
                    value = value + span.get_text()
            item[key] = value

        data[str(i)] = item

    f = codecs.open("../data/character_intro.json", "w", "utf-8")
    f.write(json.dumps(data, ensure_ascii=False))


if __name__ == "__main__":
    character_arr = get_character_arr()
    os.chdir(os.path.join(os.getcwd(), "./images"))
    get_json(character_arr)


