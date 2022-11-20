# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import re


def getIPv6Address():
    output = os.popen("ipconfig /all").read()
    result = re.findall(r"(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})", output, re.I)
    return result[0][0]




def print_hi(name):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',

        'content-encoding': 'gzip',
        'accept': '*/*',

        'accept-encoding': 'gzip, deflate, br',

        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,ru-RU;q=0.7,ru;q=0.6,en-US;q=0.5,ko-KR;q=0.4,ko;q=0.3,ja-JP;q=0.2,ja;q=0.1,fr-FR;q=0.1,fr;q=0.1,fil-PH;q=0.1,fil;q=0.1,ms-MY;q=0.1,ms;q=0.1,hi-IN;q=0.1,hi;q=0.1,my-MM;q=0.1,my;q=0.1',

        'authorization': 'Bearer D7AF67E0F964FC9B4396E1D3DDC8FDA1851AE5599BF272E8CBB0A01DACCB4B43-1',

        'content-type': 'application/grpc-web+proto',

        'origin': 'https://www.wuxiaworld.com',

        'referer': 'https://www.wuxiaworld.com/novel/above-your-head/ayh-chapter-7',

        'x-grpc-web': '1',

        'sec-ch-ua': 'Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105',


        'sec-ch-ua-mobile': '?0',

        'sec-ch-ua-platform': 'empty',
        'sec-fetch-dest': 'cors',

        'sec-fetch-mode': 'cors',

        'sec-fetch-site': 'same-site',
    }
    url = "https://api2.wuxiaworld.com/wuxiaworld.api.v2.Chapters/GetChapter"
    r = requests.post(url= url,headers=header)
   # r.encoding = 'UTF-8'
    print(r.text)

    #
    # soup = BeautifulSoup(r.text,'lxml')
    # print(soup.prettify('UTF-8'))

def getIp():
    ip = urlopen('http://ip.42.pl/raw').read().decode()
    print('ipv4：', ip)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    getIp()
    print('ipv6:'+getIPv6Address())


