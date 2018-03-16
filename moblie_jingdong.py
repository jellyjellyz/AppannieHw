import requests
from bs4 import BeautifulSoup
import proxy_ip
import json
import re
import csv
count = 0
# with open('sumsung.csv', 'w', encoding='utf-8-sig') as csvfile:
#         filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#         filewriter.writerow(['手机名称', '价格(￥)', '运行内存', '电池容量', '机身颜色', '前置摄像头像素', '后置摄像头像素', 'url'])

para = {'Referer': 'https://search.jd.com', \
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

cookies = {'cookies_are':
'__jdu=15119890310602048156812; __jdv=209750407|www.google.com|-|referral|-|1520961015391; PCSYCityID=1; user-key=e6af3e2a-fcc4-453a-a451-4e3b2e03ed2f; cn=0; xtest=1122.cf6b6759; ipLoc-djd=53283-53309-0-0; rkv=V0900; qrsc=3; __jdc=122270672; 3AB9D23F7A4B3C9B=ZEGOZVCO6OHRC3YWODA6WOXRGIFHOZ4TUUKSKRXXNFI5MNWW75AW3OBK2OCHN2V45NBH4P23GQK4TWPQN3K3646QPQ; rodGlobalHis=%7B%22.3.0%22%3A%22%2C906624%22%7D; __jda=122270672.15119890310602048156812.1511989031.1521142177.1521145827.10; __jdb=122270672.1.15119890310602048156812|10.1521145827'
}

# -------- START USING CACHE --------

# CACHE_FNAME = 'page_cache.json'  #cache0
# CACHE_FNAME = 'page_cache1.json'   #cache1
# CACHE_FNAME = 'page_cache2.json'   #cache2
CACHE_FNAME = 'page_cache3.json'   #cache3
# CACHE_FNAME = 'page_cache3.json'   #cache4



try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

except:
    CACHE_DICTION = {}

def make_request_using_cache(url, headers = para, cookies = cookies):
    unique_ident = url
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        pass

    print("Making a request for new data...")
    # Make the request and cache the new data
    iplists = proxy_ip.get_ip_list()
    theip = proxy_ip.get_random_ip(iplists)
    resp = requests.get(url, headers = para, cookies = cookies, proxies=theip)
    try:
        CACHE_DICTION[unique_ident] = str(resp.content, 'utf-8')
    except:
        CACHE_DICTION[unique_ident] = resp.text
    dumped_json_cache = json.dumps(CACHE_DICTION)
    fw = open(CACHE_FNAME,"w")
    fw.write(dumped_json_cache)
    fw.close() # Close the open file
    return CACHE_DICTION[unique_ident]

# -------- END USING CACHE --------

# -------- START the Page CLASS --------
# get the page of first 30 products & the hidden 30 products
# get price for each product

class Page:
    def __init__(self, page_num):
        self.base_url1 = 'https://search.jd.com/Search?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA \
                    &enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=%E4%B8%89%E6%98%9Fshou%20ji \
                    &ev=exbrand_%E4%B8%89%E6%98%9F%EF%BC%88SAMSUNG%EF%BC%89%5E'
        self.base_url2 = 'https://search.jd.com/s_new.php?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA \
                    &enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&suggest=3.def.0.V16&wq=%E4%B8%89%E6%98%9F&ev=exbrand_%E4%B8%89%E6%98%9F%EF%BC%88SAMSUNG%EF%BC%89%5E'     


        self.showurl = self.base_url1 + '&click=0&page={}'.format(page_num)
        self.showedid = [] 
        self.hideurl = ''
        self.page = page_num
        self.Phones = []
        
    def get_info_show(self):
        res_obj = make_request_using_cache(self.showurl)
        soup = BeautifulSoup(res_obj, 'html.parser')
        phone_showed = soup.find_all(class_ = 'gl-i-wrap')
        for aphone in phone_showed:
            thePhone = CellPhone()
            thePhone.detailurl = 'https:' + aphone.find(class_ = 'p-img').find('a')['href'].strip()
            thePhone.price = aphone.find(class_ = 'p-price').find('i').text.strip()
            # thePhone.name = aphone.find(class_ = 'p-name').text.strip()
            # print(thePhone.detailurl)
            # print(thePhone.price)
            # print(thePhone.name)
            self.Phones.append(thePhone)
        a = soup.find('ul', class_ = 'gl-warp')
        tmp = soup.find('ul', class_ = 'gl-warp').children

        for child in tmp:
            try:
                self.showedid.append(child.attrs['data-pid'])
            except:
                continue
        self.hideurl =  self.base_url2+'&page={}&scrolling=y&log_id=1521142881.49033&tpl=3_M&show_items={}'.format(self.page+1, ','.join(self.showedid))

        
        # print(self.hideurl)


    def get_info_hide(self):
        res_obj = make_request_using_cache(self.hideurl)
        soup = BeautifulSoup(res_obj, 'html.parser')
        phone_hide = soup.find_all(class_ = 'gl-i-wrap')
        for aphone in phone_hide:
            thePhone = CellPhone()
            thePhone.detailurl = 'https:' + aphone.find(class_ = 'p-img').find('a')['href'].strip()
            thePhone.price = aphone.find(class_ = 'p-price').find('i').text.strip()
            self.Phones.append(thePhone)

    def get_full_info(self):
        self.get_info_show()
        self.get_info_hide()
        return self.Phones

# -------- END the Page CLASS --------

# -------- START the Phone CLASS --------
class CellPhone():
    def __init__(self):
        self.detailurl = 'N/A'
        self.name = 'N/A'
        self.price = 'N/A'
        self.color = []
        self.infos = []

        self.storage = 'N/A'
        self.battery = 'N/A'
        self.camera_frot = 'N/A'
        self.camera_back = 'N/A'

    def __str__(self):
        global count
        return '''
            Count {}
                手机名称:{}
                价格:{}
                运行内存:{}
                电池容量:{}
                机身颜色:{}
                前置摄像头像素:{}
                后置摄像头像素:{}
        '''.format(count, self.name, self.price, self.storage, self.battery, self.color, self.camera_frot, self.camera_back)

# -------- END the Phone CLASS --------


# -------- START Function for mobile details  --------

def get_mobile_data(phone_obj):
    detail_res = make_request_using_cache(phone_obj.detailurl)
    soup = BeautifulSoup(detail_res, 'html.parser')
    try:
        colors = soup.find(id = 'choose-attr-1').find_all(href="#none")
        for color in colors:
            phone_obj.color.append(color.text.strip())
        phone_obj.color = ','.join(phone_obj.color)
    except:
        phone_obj.color = 'N/A'
        print('NO color detail for {}'.format(phone_obj.detailurl))
    try:
        infos = soup.find(class_ = 'parameter2').find_all('li')
    except:
        print(phone_obj.detailurl)
        return False

    for info in infos:
        try:
            phone_obj.infos.append(info.text)
            theinfo = re.findall(r'\uff1a(.*)$', info.text)[0]
            # print(theinfo)
            if '名称' in info.text:
                if '壳' in info.text or '贴膜' in info.text or '线' in info.text or '头' in info.text \
                    or '耳机' in info.text or '电源' in info.text or '套' in info.text or '优盘' in info.text \
                    or '电池' in info.text or '器' in info.text or '卡' in info.text or '表' in info.text:
                    print('NOT a phone, {}'. format(info.text))
                    return False
                else:
                    phone_obj.name = theinfo
            elif '类别' in info.text:
                if '耳机' in info.text or '其他' in info.text or '组套' in info.tex:
                    print('NOT a phone, {}'. format(info.text)) 
                    return False
            elif '前置摄像头' in info.text:
                phone_obj.camera_frot = theinfo
            elif '后置摄像头' and '后' in info.text:
                phone_obj.camera_back = theinfo
            elif '内存' in info.text:
                phone_obj.storage = theinfo
            elif '电池' in info.text:
                phone_obj.battery = theinfo
            elif '颜色' in info.text and phone_obj.color == 'N/A':
                phone_obj.color = theinfo
            else:
                continue
        except:
            continue

# -------- END Function for mobile details  --------

# -------- START MAIN scraping --------

# for p_num in range(1,20)[::2]:    #cach0
# for p_num in range(21,40)[::2]:   #cach1
# for p_num in range(41,60)[::2]:   #cach2 
for p_num in range(61,80)[::2]:   #cach3
# for p_num in range(81,96)[::2]:   #cach4
    thepage = Page(p_num)
    phones = thepage.get_full_info()
    # print(len(phones))
    for aphone in phones:
        count += 1
        if get_mobile_data(aphone) == False:
            continue
    # print(aphone.detailurl)
    # print(aphone.color)
    # print(aphone.name)
    # print(aphone.price)
    # print(aphone.storage)
    # print(aphone.camera_frot)
    # print(aphone.camera_back)
    # print(aphone.battery)

        print(aphone)
        print('-'*20)
        # with open('sumsung.csv', 'a+', encoding='utf-8-sig') as csvfile:
        #     filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        #     filewriter.writerow([aphone.name, aphone.price, aphone.storage, \
        #                         aphone.battery, aphone.color, aphone.camera_frot, aphone.camera_back, aphone.detailurl])

# -------- END MAIN scraping --------


