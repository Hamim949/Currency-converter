import requests

currency_code_map = {
    "cad": "canadian curency",
    "eur": "Euro",
    "usd": "United states dollar",
    "mxn": "Mexican peso",
    "btc": "Bitcoin",
}

def get_currencies():
    currency_string = []
    for code in currency_code_map.keys():
        str = currency_code_map[code]
        currency_string.append(code + " - " + str)
    return currency_string

def get_currency_from_code(code):
    return currency_code_map[code]


def get_currency_string(code):
    return code + " - " + get_currency_from_code(code)

url_host = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.min.json"
response = requests.get(url_host)
sample_json = response.json()

def get_exchange_rate(from_code, to_code):
    url_host = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/"
    endpoint = from_code + "/" + to_code
    ext = ".json"
    url = url_host + endpoint + ext
    response = requests.get(url)
    if response.ok:
        exchange = response.json()
        rate = exchange[to_code]
    else:
        rate = 0
    return response.ok, rate



def get_currency_string(code):
    return code + " - " + get_currency_from_code(code)


currencies = get_currencies()
default_from = get_currency_string("usd")
default_to = get_currency_string("eur")

if __name__ == "__main__":
    get_currencies()
    print(get_currency_string())

    success, rate = get_exchange_rate("usd", "eur")
    print(rate)

