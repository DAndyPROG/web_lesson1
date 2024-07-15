import requests

class CurrencyConverter(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://v6.exchangerate-api.com/v6/{}/latest/".format(api_key)


    def get_exchange_rate(self, from_currency, to_currency):
        url = self.base_url + from_currency
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if to_currency in data['conversion_rates']:
                return data['conversion_rates'][to_currency]
            
            else:
                raise ValueError("Invalid currency code")
        
        else:
            raise ConnectionError('Failed to fetch data from the API')
        
    
    def convert_currency(self, amount, from_currency, to_currency):
        rate = self.get_exchange_rate(from_currency, to_currency)
        return amount * rate


def main():
    api_key = "fe36135a6ea9246b7320f832"
    converter = CurrencyConverter(api_key)
    
    from_currency = input('Enter currency code you want to convert: ').upper()
    to_currency = input('Enter currency code you want to convert to: ').upper()
    
    amount = float(input('Enter the amount you want to convert: '))
    
    try:
        converted_amount = converter.convert_currency(amount, from_currency, to_currency)
        print(f'{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}')
    
    except ValueError as e:
        print(e) 
    
    except ConnectionError as e:
        print(e) 


if __name__ == "__main__":
    main()
