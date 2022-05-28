import time

import execjs
import requests


def get_page(page_num, parameters):
    url = 'https://match.yuanrenxue.com/api/match/2?page={}'.format(
        page_num, parameters)
    headers = {
        "authority": "match.yuanrenxue.com",
        "method": "GET",
        "scheme": "https",
        "accept": "application/json, text/javascript, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN, zh",
        "referer": "https://match.yuanrenxue.com/match/1",
        "user-agent": "yuanrenxue.project",
        "x-requested-with": "XMLHttpRequest",
        "cookie": parameters
    }
    response = requests.get(url=url, headers=headers)
    return response.json()


def calculate_m_value():
    with open(r'2.js', encoding='utf-8', mode='r') as f:
        jsDate = f.read()
    psd = execjs.compile(jsDate).call('request')
    # psd = psd.replace('|', '%E4%B8%A8')
    print("this request parameters is :", psd)
    return psd


if __name__ == '__main__':
    sum_num = 0

    # print(calculate_m_value())
    # a = get_page(page_num='1', parameters=calculate_m_value())
    # print(a)

    for page_num in range(1, 6):
        res = get_page(page_num=page_num, parameters=calculate_m_value())
        data = [__['value'] for __ in res['data']]
        print(data)
        sum_num += sum(data)
        time.sleep(1)

    print("the answer is :", sum_num)
