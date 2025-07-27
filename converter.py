import requests

def get_exchange_rates():
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    response = requests.get(url)
    data = response.json()

    rates = {}
    for item in data:
        if item['Ccy'] in ['USD', 'EUR']:
            rates[item['Ccy']] = {
                'rate': float(item['Rate'].replace(",", "")),
                'date': item['Date']
            }

    return rates

def get_user_input():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Son kiriting!")
        return None, None, None

    from_currency = input("From currency (USD, EUR, UZS): ").upper()
    to_currency = input("To currency (USD, EUR, UZS): ").upper()
    return amount, from_currency, to_currency

def convert_currency(amount, from_cur, to_cur, rates):
    usd_rate = rates['USD']['rate']
    eur_rate = rates['EUR']['rate']

    if from_cur == to_cur:
        return amount

    if from_cur == 'USD':
        amount_uzs = amount * usd_rate
    elif from_cur == 'EUR':
        amount_uzs = amount * eur_rate
    elif from_cur == 'UZS':
        amount_uzs = amount
    else:
        raise ValueError("Noto'g'ri valyuta turi (from)")

    if to_cur == 'USD':
        return amount_uzs / usd_rate
    elif to_cur == 'EUR':
        return amount_uzs / eur_rate
    elif to_cur == 'UZS':
        return amount_uzs
    else:
        raise ValueError("Noto'g'ri valyuta turi (to)")

def main():
    rates = get_exchange_rates()
    amount, from_cur, to_cur = get_user_input()
    
    if None in (amount, from_cur, to_cur):
        return

    try:
        result = convert_currency(amount, from_cur, to_cur, rates)
        date = rates['USD']['date']
        print(f"{amount} {from_cur} = {result:,.2f} {to_cur} ({date})")
    except ValueError as e:
        print(str(e))

