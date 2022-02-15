import json
import requests
from pprint import pprint
import csv


user_token_file = 'token.txt'
with open(user_token_file, 'r') as f:
    user_token = f.readline()


keyword = '刷夜'


def search(keywords):
    global user_token
    search_result = []
    params = {
        'action': 'search',
        'pagesize': 50,
        'page': 1,
        'keywords': keywords,
        'PKUHelperAPI': 3.0,
        'jsapiver': '201027113050-456920',
        'user_token': user_token
    }
    response = requests.get('https://pkuhelper.pku.edu.cn/services/pkuhole/api.php', params=params)
    page_result = json.loads(response.text)['data']
    pprint(page_result)
    search_result += page_result
    while page_result != []:
        params['page'] += 1
        response = requests.get('https://pkuhelper.pku.edu.cn/services/pkuhole/api.php', params=params)
        page_result = json.loads(response.text)['data']
        pprint(page_result)
        search_result += page_result
    pprint(search_result)
    return search_result


def writecsv(keyword, data):
    with open(keyword + '.csv', 'w', encoding='utf-8-sig') as f:
        cw = csv.DictWriter(f, fieldnames=data[1].keys(), lineterminator = '\n', dialect=csv.excel)
        cw.writeheader()
        cw.writerows(data)

def main():
    writecsv(keyword, search(keyword))


if __name__ == '__main__':
    main()