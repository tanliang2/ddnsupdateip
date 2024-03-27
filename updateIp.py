import requests
from urllib.request import urlopen
import os
import re
import json
import socket

#windows
# def get_ipv6():
#     try:
#         output = os.popen("ipconfig /all").read()
#         result = re.findall(r"(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})", output, re.I)
#         return result[0][0]
#     except:
#         return ''
#ubantu
def get_ipv6_address():
    """
    获取本机IPv6地址
    """
    try:
        # 获取所有接口的IPv6地址列表
        sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        sock.connect(('::1', 80))  # 连接到本地IPv6环回地址，端口号随意
        result = sock.getsockname()[0]
        sock.close()
        return result
    except OSError:
        return None


def get_ipv4():
    ipv4 = urlopen('http://ip.42.pl/raw').read().decode()
    return ipv4


def get_record_ipv4():
    try:
        f = open('/home/tanliang/PycharmProjects/ddnsupdateip/ip.json', 'r')
        content = f.read()
        print("read content:" + str(content))
        a = json.loads(content)
        f.close()
        return a
    except:
        print("get_record_ipv4 error")
        return ""


def save_ipv4(ipv4):
    try:
        b = json.dumps(ipv4)
        f2 = open('/home/tanliang/PycharmProjects/ddnsupdateip/ip.json', 'w')
        f2.write(b)
        f2.close()
    except:
        print("save_ipv4 error")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ip = get_ipv4()
    print(ip)
    save_ip = get_record_ipv4()
    if save_ip == ip:
        print("same")
    else:
        ipv6 = get_ipv6_address()
        print(ipv6)
        url = 'http://162.216.242.253/nic/update?myip=' + ip + '&myipv6=' + ipv6 + '&username=tanliangddns2&password=3ad200dd64e135c194a3516bda7bd6a8'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'Authorization': 'Basic [BASE64-ENCODED-USERNAME:PASSWORD-PAIR]',
        }
        print(url)
        r = requests.get(url=url, headers=header)
        if r.status_code == 200 and r.text.__contains__('good'):
            print('update successful')
            save_ipv4(ip)
        print(r.status_code)
        print(r.text)
