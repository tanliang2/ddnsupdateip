import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import re
import json


def getIPv6():
    output = os.popen("ipconfig /all").read()
    result = re.findall(r"(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})", output, re.I)
    return result[0][0]


def getIpv4():
    ipv4 = urlopen('http://ip.42.pl/raw').read().decode()
    return ipv4


def getRecordIpv4():
    try:
        f = open('ip.json', 'r')
        content = f.read()
        a = json.loads(content)
        f.close()
        return a
    except:
        print("open error")
        return ""


def saveIpv4(ipv4):
    b = json.dumps(ipv4)
    f2 = open('ip.json', 'w')
    f2.write(b)
    f2.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ip = getIpv4()
    print(ip)
    ip = '113.111.244.82'
    save_ip = getRecordIpv4()
    if save_ip == ip:
        print("same")
    else:
        ipv6 = getIPv6()
        print(ipv6)
        url = 'http://api.dynu.com/nic/update?myip=' + ip +'&myipv6='+ipv6+ '&username=tanliangddns2&password=3ad200dd64e135c194a3516bda7bd6a8'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'Authorization': 'Basic [BASE64-ENCODED-USERNAME:PASSWORD-PAIR]',
        }
        print(url)

        r = requests.get(url=url, headers=header)
        if r.status_code == 200 and r.text.__contains__('good'):
            print('update successful')
            saveIpv4(ip)
        print(r.status_code)
        print(r.text)
