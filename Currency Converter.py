import requests

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    api_key = 'your_api_key_here'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}'
    response = requests.get(url)
    data = response.json()
    converted_amount = data['conversion_result']
    return converted_amount

# Main program
if __name__ == '__main__':
    amount = float(input('Enter the amount to convert: '))
    from_currency = input('Enter the currency to convert from (e.g. USD): ').upper()
    to_currency = input('Enter the currency to convert to (e.g. EUR): ').upper()
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f'{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}')
