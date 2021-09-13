import requests
from datetime import date, timedelta, datetime
from bs4 import BeautifulSoup

today = date.today()

d1 = today.strftime("%Y-%m-%d")
d2 = (datetime.now()-timedelta(days=3)).strftime("%Y-%m-%d")
banxico_token = '7f173d0010a6cb8928274ceafdbc88a3b58f92884a3c10692af96ab3ade02317'
banxico = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/%s/%s?token=%s'%(d2, d1, banxico_token)
fixer_token = '2c066554135853cc1c3f9da49b832b62'
fixer_url = 'http://data.fixer.io/api/latest?access_key=%s&symbols=MXN,USD&format=1'%(fixer_token)
diario = 'https://www.banxico.org.mx/tipcamb/tipCamMIAction.do'

def get_exchange_rate_banxico():
    print(banxico)
    resp = requests.get(
        banxico
    )
    if resp.status_code != 200:
        # This means something went wrong.
        raise Exception('GET banxico {}'.format(resp.status_code))
    print("response")
    print(resp)
    r = resp.json()
    print(r)
    r['bmx']['series'][0]['datos'].sort(key=lambda d: d['fecha'], reverse=True)
    datos =  r['bmx']['series'][0]['datos']
    latest = datos[0]['dato']
    fecha = datos[0]['fecha']
    formated_date = datetime.strptime(fecha, "%d/%m/%Y")
    res = {'last_updated': formated_date, 'value': latest}
    return res

def get_exchange_rate_fixer():
    resp = requests.get(
        fixer_url
    )
    if resp.status_code != 200:
        raise Exception('GET fixer {}'.format(resp.status_code))
    print(resp.json())
    obj = resp.json()
    rates = obj['rates']
    fecha = obj['date']
    formated_date = datetime.strptime(fecha, "%Y-%m-%d")
    return {'last_updated': formated_date, 'value': rates['MXN']/rates['USD']}

def get_exchange_rate_diario():
    page = requests.get(diario)
    soup = BeautifulSoup(page.content, 'html.parser')
    rate = soup.find_all('tr', class_='renglonNon')[0]
    data = rate.find_all('td')
    fecha = data[0].get_text().strip()
    last_rate = data[2].get_text().strip()
    formated_date = datetime.strptime(fecha, "%d/%m/%Y")
    #fix = rate.find_all('td')[1]
    return {'last_updated': formated_date, 'value': last_rate}

def get_exchange_rate():
    resp = requests.get(
        banxico,
        headers={'Bmx-Token':'7f173d0010a6cb8928274ceafdbc88a3b58f92884a3c10692af96ab3ade02317'}
    )
    if resp.status_code != 200:
        # This means something went wrong.
        raise Exception('GET banxico {}'.format(resp.status_code))
    print(resp.json())
    for todo_item in resp.json():
        print(todo_item)
