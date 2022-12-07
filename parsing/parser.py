import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://systema.kg/'

HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='thumbnail-container')
    systema_goods = []

    for item in items:
        systema_goods.append(
            {
                'title': URL + item.find('a').get('href'),
                'title_text': item.find('div', class_='product-description').get_text(),
                'image': item.find('div', class_='thumbnail-top').find('a', class_='thumbnail product-thumbnail').find('img').get('src'),
                'price': item.find('div', class_='product-price-and-shipping').find('span').get_text(),
            }
        )
    return systema_goods

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        systema_goods_1 = []
        for page in range(0, 1):
            html = get_html(f'https://systema.kg/16-cpu-processora', params=page)
            systema_goods_1.extend(get_data(html.text))
        return systema_goods_1
    else:
        raise Exception('Error in parser func........')