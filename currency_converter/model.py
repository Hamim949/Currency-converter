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

currencies = get_currencies()
default_from = get_currency_string("usd")
default_to = get_currency_string("eur")

if __name__ == "__main__":
    get_currencies()
    print(get_currency_string())

