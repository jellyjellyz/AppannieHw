from bs4 import BeautifulSoup
import requests
import random


def get_ip_list():
    print("正在获取代理列表...")
    # url = ' http://www.xicidaili.com/wt/'
    url = 'https://www.sslproxies.org/'
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    html = requests.get(url=url, headers=headers).text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    ips = soup.find(id='list').find_all('tr')
    ip_list = []
    for i in range(1, len(ips)-1):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        # print(tds[1].text)
        # print(tds[2].text)
        ip_list.append(tds[1].text + ':' + tds[2].text)
    print("代理列表抓取成功.")
    return ip_list

def get_random_ip(ip_list):
    print("正在设置随机代理...")
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)  
    proxies = {'http': proxy_ip}
    print("代理设置成功.")
    return proxies

if __name__ == '__main__':
    iplists = get_ip_list()
    theip = get_random_ip(iplists)
    print(get_random_ip(iplists))