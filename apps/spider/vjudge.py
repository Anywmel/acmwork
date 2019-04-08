import requests
import json

session = requests.Session()


def crawl():
    None


def login(username, password):
    url = "https://vjudge.net/user/login"
    headers = {
        'authority': 'vjudge.net',
        'method': 'POST',
        'path': '/user/login',
        'scheme': 'https',
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
        'content-length': "33",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'cookie': "_ga=GA1.2.875729057.1541660225; _gid=GA1.2.1325865481.1544165094; JSESSIONID=0BFD3364480A9F4E0AD8FEAB56571D79",
        'origin': "https://vjudge.net",
        'referer': "https://vjudge.net/",
        'user-agent': "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'x-requested-with': "XMLHttpRequest",
    }
    data = {
        'username': username,
        'password': password
    }
    response = session.request("POST", url, data=data, headers=headers)
    print(response)


if __name__ == '__main__':
    login('ky25390', 'ky25390')
