from requests import Session
from json import loads

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': YOUR_COINMARKETCAP_API_KEY,
}

session = Session()
session.headers.update(headers)

inputType = input('Input Type: ').upper()
amount = input('Amount: ')
outputType = input('Output Type: ').upper()

parameters = {
      'start':'1',
      'limit':'500',
      'convert': outputType
    }

response = session.get(url, params=parameters)
data = loads(response.text)
for crypto in data['data']:
    if crypto['symbol'] == inputType:
        result = round(crypto['quote'][outputType]['price'], 5) *float(amount)
        if result == 0:
            result = crypto['quote'][outputType]['price'] * float(amount)
        inputName = crypto['name']
    if crypto['symbol'] == outputType:
        outputName = crypto['name']
try:
  print('{} {}({}) = {} {}({})'.format(amount, inputType, inputName, result, outputType, outputName))
except:
  print('Invalid crypto or network error !')