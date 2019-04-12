#!/usr/bin/env python3
# encoding:utf-8
import requests
from requests import RequestException
from bs4 import BeautifulSoup as bs
import time, random, re
import sys

class GuaziTraker:

    def get_ip_list(self, url, headers):
        web_data = requests.get(url, headers=headers)
        soup = bs(web_data.text, 'lxml')
        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[0].text + ':' + tds[1].text)
        return ip_list

    def get_httpsip_list(self, url, headers):
        web_data = requests.get(url, headers=headers)
        soup = bs(web_data.text, 'lxml')
        ips = soup.find_all('tr')
        httpsip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            httpsip_list.append(tds[1].text + ':' + tds[2].text)
        return httpsip_list

    def get_random_ip(self, ip_list,httpsip_list):
        proxy_list = []
        for ip in ip_list:
            proxy_list.append('http://' + ip)
        proxy_ip = random.choice(proxy_list)
        https_proxy_list = []
        for ip in httpsip_list:
            https_proxy_list.append('https://' + ip)
        proxy_ips = random.choice(https_proxy_list)
        proxies = {'http': proxy_ip,'https': proxy_ips}
        return proxies

    def get_proxies(self, url_http,url_https):
        ip_list = self.get_ip_list(url_http, self.headers)
        ips_list = self.get_httpsip_list(url_https, self.headers)
        proxies = self.get_random_ip(ip_list,ips_list)
        return proxies

    def __init__(self, area):
        self.area = area
        self.link = "https://www.guazi.com/" + area + "/buy/o"
        # 请求头 cookie 必须需要加上
        self.headers = {
            'Cookie': '_gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A67347575325%7D;cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22%25e7%2593%259c%25e5%25ad%2590%2520%25e4%25ba%258c%25e6%2589%258b%25e8%25bd%25a6%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_i%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22c8dda799-7600-40e5-a020-2d28e308ee40%22%2C%22sessionid%22%3A%2274fcd60e-6f05-42e0-c6fa-a59a54ec5666%22%7D;cityDomain=bj;clueSourceCode=10103000312%2300;ganji_uuid=9450925418870829074157;lg=1;preTime=%7B%22last%22%3A1554172686%2C%22this%22%3A1554115250%2C%22pre%22%3A1554115250%7D;sessionid=74fcd60e-6f05-42e0-c6fa-a59a54ec5666;user_city_id=12;uuid=c8dda799-7600-40e5-a020-2d28e308ee40;antipas=V74531896215Q6su1212o76O0p;',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        proxy_url = "https://www.kuaidaili.com/free/inha/1/"
        url_https="http://31f.cn/https-proxy/"
        self.proxies = self.get_proxies(proxy_url,url_https)

    def get_page_text(self, url):
        try:
            resp = requests.get(url, headers=self.headers, proxies=self.proxies)
            resp.raise_for_status
            resp.encoding = resp.apparent_encoding
            return resp.text
        except RequestException:
            print('Can not get the page')
            pass

    def get_car_info(self, html):
        soup = bs(html, 'lxml')
        result = soup.select('div.list-wrap.js-post > ul > li ')
        filename = "guazi_car_" + self.area + ".txt"
        with open(filename, "a", encoding="utf-8-sig") as wf:
            for i in result:
                car_name = i.a.h2.text
                year_thing = i.select('a div[class="t-i"]')[0].text
                now_price = i.select('a div[class="t-price"]')[0].p.text
                strict_list = i.select('a div[class="t-price"] i[class="i-blue"]')
                if len(strict_list) > 0:
                    is_strict = i.select('a div[class="t-price"] i[class="i-blue"]')[0].text
                else:
                    is_strict = "非严选"
                original_list = i.select('a div[class="t-price"] em[class="line-through"]')
                if len(original_list) > 0:
                    guiding_price = i.select('a div[class="t-price"] em[class="line-through"]')[0].text
                else:
                    a = 'https://www.guazi.com' + i.a['href']
                    resp = self.get_page_text(a)
                    content = self.get_detail(resp)
                    guiding_price = content['guiding_price']
                wf.write(car_name + "|" + year_thing + "|" + now_price + "|" + is_strict + "|" + guiding_price + "\n")
            #     print(i)

    def get_link(self, html):
        soup = bs(html, 'lxml')
        result = soup.select('div.list-wrap.js-post > ul > li > a')
        detail_url = ['https://www.guazi.com' + i['href'] for i in result]
        return detail_url

    def get_attr_text(self, currTag, attr_path):
        try:
            attr_tag = currTag.select_one(attr_path)
        except AttributeError:
            return ''
        else:
            return attr_tag.get_text()

    def get_detail(self, html):
        try:
            detail = bs(html, 'lxml')
            title = detail.select_one('div.infor-main.clearfix > div.product-textbox > h2').get_text()
            title = re.sub(r'[\r\n]', '', title)
            is_strict = self.get_attr_text(detail,
                                           'div.infor-main.clearfix > div.product-textbox > h2 span[class="labels baomai"]')
            time = detail.select_one('div.product-textbox > ul > li.one > span').get_text()
            used_distance = detail.select_one('div.product-textbox > ul > li.two > span').get_text()
            displacement = ''
            city = ''
            if "排量" in detail.select('div.product-textbox > ul > li.three')[0].get_text():
                ##排量
                displacement = detail.select('div.product-textbox > ul > li.three > span')[0].get_text()
            if "上牌地" in detail.select('div.product-textbox > ul > li.three ')[0].get_text():
                city = detail.select('div.product-textbox > ul > li.three > span')[0].get_text()
            if len(detail.select('div.product-textbox > ul > li.three')) > 1:
                if "上牌地" in detail.select('div.product-textbox > ul > li.three')[1].get_text():
                    ##排量
                    city = detail.select('div.product-textbox > ul > li.three > span')[1].get_text()
                if "排量" in detail.select('div.product-textbox > ul > li.three ')[1].get_text():
                    displacement = detail.select('div.product-textbox > ul > li.three > span')[1].get_text()

            transmission = detail.select_one('div.product-textbox > ul > li.last > span').get_text()
            price = detail.select_one('div.product-textbox > div.pricebox.js-disprice > span.pricestype').get_text()
            guiding_price = detail.select_one('div.product-textbox > div.pricebox.js-disprice > '
                                              'span.newcarprice').get_text()
            guiding_price = re.sub(r'[\r\n ]', '', guiding_price)

            title = title.strip().replace('                    ', ' ')
            price = price.replace(' ', '')
            result = {
                'title': title,
                'is_strict': is_strict,
                'time': time,
                'used_distance': used_distance,
                'displacement': displacement,
                'city': city,
                'transmission': transmission,
                'price': price,
                'guiding_price': guiding_price
            }
            # result = "|" + title + "|" + is_strict + "|" + time + "|" + used_distance + "|" + displacement + "|" + city \
            #          + "|" + transmission + "|" + price \
            #          + "|" + guiding_price + "|"
        except:
            return {
                'title': title,
                'is_strict': '',
                'time': '',
                'used_distance': '',
                'displacement': '',
                'city': '',
                'transmission': '',
                'price': '',
                'guiding_price': ''
            }
        else:
            return result

    def main_detail(self):
        with open("guazi_car_detail.txt", "a", encoding="utf-8-sig") as wf:
            for i in range(1, 101, 1):
                print("第" + str(i) + "页。。。。")
                url = self.link + str(i)
                html = self.get_page_text(url)
                result = self.get_link(html)
                time.sleep(random.randint(5, 7))
                for i in result:
                    resp = self.get_page_text(i)
                    content = self.get_detail(resp)
                    if content:
                        wf.write(content + "\n")
        wf.close()

    def main_list(self):
        print("proxies=http="+self.proxies.get("http")+"=https="+self.proxies.get("https"))
        for i in range(1, 101, 1):
            print("第" + str(i) + "页。。。。")
            url = self.link + str(i)
            html = self.get_page_text(url)
            self.get_car_info(html)
            time.sleep(random.randint(5, 7))


if __name__ == '__main__':
    if len(sys.argv)-1 <1:
        exit(200)
    else:
        areaStr = str(sys.argv[1])
        t = GuaziTraker(areaStr)
        t.main_list()
