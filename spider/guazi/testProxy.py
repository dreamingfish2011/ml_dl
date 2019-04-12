import requests

link = "https://www.guazi.com/sh/buy/o"
# 请求头 cookie 必须需要加上
headers = {
    'Cookie': '_gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A67347575325%7D;cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22%25e7%2593%259c%25e5%25ad%2590%2520%25e4%25ba%258c%25e6%2589%258b%25e8%25bd%25a6%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_i%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22c8dda799-7600-40e5-a020-2d28e308ee40%22%2C%22sessionid%22%3A%2274fcd60e-6f05-42e0-c6fa-a59a54ec5666%22%7D;cityDomain=bj;clueSourceCode=10103000312%2300;ganji_uuid=9450925418870829074157;lg=1;preTime=%7B%22last%22%3A1554172686%2C%22this%22%3A1554115250%2C%22pre%22%3A1554115250%7D;sessionid=74fcd60e-6f05-42e0-c6fa-a59a54ec5666;user_city_id=13;uuid=c8dda799-7600-40e5-a020-2d28e308ee40;antipas=V74531896215Q6su1212o76O0p;',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
# proxies = {'https':'122.136.212.132:53281'}
resp = requests.get(link, headers=headers )
resp.raise_for_status
resp.encoding = resp.apparent_encoding
print(resp.text)
