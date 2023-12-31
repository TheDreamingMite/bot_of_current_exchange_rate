import requests
from cachetools import TTLCache
from datetime import date

URL_API_ADDRESS = {
    1: 'https://www.cbr-xml-daily.ru/daily_json.js',
    2: 'https://open.er-api.com/v6/latest/USD',
    3: 'https://api.exchangerate-api.com/v4/latest/usd'}

cache = TTLCache(maxsize=100, ttl=600)

def api_data(api_url, key):
    response = requests.get(api_url)
    if response.ok:
        data = response.json()
        if key == 1:
            rate = data['Valute']['USD']['Value']
        elif key == 2:
            rate = data['rates']['RUB']
        elif key == 3:
            rate = data['rates']['RUB']
        # Происходит запись в данные кэша
        cache[key] = rate
        return rate

def calc_rate():
    for n in range(1, 3):
        rate = cache.get(n)
        if rate is not None:
            # Смотрим в кэш
            return  (f"Курс доллара на {date.today()}: {rate:.1f} руб.")


        rate = api_data(URL_API_ADDRESS[n], n)

        if rate is not None:
            return (f"Курс доллара на {date.today()}: {rate:.1f} руб.")
        else:
            return ("Ошибка, источники неверны")

def calc_with_comission(amount):
    comission = 0.05
    rate = 0
    for n in range(1, 3):
        rate = cache.get(n)
        if rate is not None:
            return [rate * amount * (1 + comission), comission, rate]

        rate = api_data(URL_API_ADDRESS[n], n)
        if rate is not None:
            return [rate * amount * (1 + comission), comission, rate]
        else:
            return [0,0,0]