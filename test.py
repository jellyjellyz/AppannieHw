import requests
from bs4 import BeautifulSoup
import proxy_ip
iplists = proxy_ip.get_ip_list()
theip = proxy_ip.get_random_ip(iplists)

# para = {'Referer': 'https://search.jd.com', \
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
# 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

para = {'Referer': 'https://search.jd.com', \
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

cookies = {'cookies_are':
'__jdu=15119890310602048156812; __jdv=209750407|www.google.com|-|referral|-|1520961015391; PCSYCityID=1; user-key=e6af3e2a-fcc4-453a-a451-4e3b2e03ed2f; cn=0; xtest=1122.cf6b6759; ipLoc-djd=53283-53309-0-0; rkv=V0900; qrsc=3; __jdc=122270672; 3AB9D23F7A4B3C9B=ZEGOZVCO6OHRC3YWODA6WOXRGIFHOZ4TUUKSKRXXNFI5MNWW75AW3OBK2OCHN2V45NBH4P23GQK4TWPQN3K3646QPQ; rodGlobalHis=%7B%22.3.0%22%3A%22%2C906624%22%7D; __jda=122270672.15119890310602048156812.1511989031.1521142177.1521145827.10; __jdb=122270672.1.15119890310602048156812|10.1521145827'
}

proxies = theip
#可以不加cookie; 需要referer(不变), user-agent(不变)
# res_obj2 = requests.get('https://search.jd.com/s_new.php?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=%E4%B8%89%E6%98%9Fshou%20ji&ev=exbrand_%E4%B8%89%E6%98%9F%EF%BC%88SAMSUNG%EF%BC%89%5E&page=2&s=31&scrolling=y&log_id=1521086720.10784&tpl=3_M&show_items=4120319,4938584,5424574,2895156,5005703,2868437,1898117,2348849,3712625,4934609,4934649,4938578,5273371,4938580,519836,4791010,1814629,2268226,2455672,4176193,5004277,5569415,5004251,4176197,3153436,4083885,4083889,2455670,1829876,4083883'\
# , headers = para, cookies = cookies, proxies=proxies).text
# res_obj2 = requests.get('https://search.jd.com/s_new.php?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&suggest=3.def.0.V16&wq=%E4%B8%89%E6%98%9F&ev=exbrand_%E4%B8%89%E6%98%9F%EF%BC%88SAMSUNG%EF%BC%89%5E&page=2&s=31&scrolling=y&log_id=1521145825.46397&tpl=3_M&show_items=6577495,6577477,4120319,6405876,6577511,4938584,5424574,2895156,5005703,1898117,2348849,3712625,4934609,2868437,4934649,5273371,4938578,4938580,6828189,6405876,6577495,6577477,1814629,2268226,4791010,2455672,4176193,519836,5004277,5569415'\
# , headers = para, cookies = cookies, proxies=proxies).text
res_obj2 = requests.get('https://search.jd.com/s_new.php?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&suggest=3.def.0.V16&wq=%E4%B8%89%E6%98%9F&ev=exbrand_%E4%B8%89%E6%98%9F%EF%BC%88SAMSUNG%EF%BC%89%5E&page=4&scrolling=y&log_id=1521142881.49033&tpl=3_M&show_items=1592577,4157994,787517,1028493,6512234,6489426,11028131173,16801540657,10557763553,14452086044,21947234219,11250648644,6027984,14113503977,16178936267,11633379784,22922724696,17147636619,24203858466,11693728804,12096454138,11263699823,14276207185,16635824783,14734721426,11376736984,11620230247,18850488548,16278287611,25669964375'\
, headers = para, cookies = cookies, proxies=proxies).text

r2 = BeautifulSoup(res_obj2, 'html.parser')
mobiles2 = r2.find_all(class_ = 'p-name')
print(mobiles2)

# res_obj1 = requests.get('https://search.jd.com/Search?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&enc=utf-8& \
# wq=%E4%B8%89%E6%98%9Fshou%20ji&pvid=4e8acc4e89a24dfc96580a9e862f0f88')
# res_obj1 = res_obj1.content.decode("utf8","ignore").encode("gbk","ignore")
# r1 = BeautifulSoup(res_obj1, 'html.parser')
# mobiles1 = r1.find_all(class_ = 'p-name')

# # soup = BeautifulSoup(res_obj, 'html.parser')



# for am in mobiles1:
#     print(am.find('em').text)


for am in mobiles2:
    print(am.find('em').text)




