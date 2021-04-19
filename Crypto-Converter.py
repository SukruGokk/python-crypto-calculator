# @date: 19.04.2021
# @author: Şükrü Erdem Gök
# @version: Python 3.8
# @os: Windows 10
# @github: https://github.com/SukruGokk

# Crypto Converter

# Lib
from requests import Session
from json import loads

# Coinmarketcap api url
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Add headers(specifiy app type and add api key)
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': YOUR_COINMARKETCAP_API_KEY,
}

session = Session()
session.headers.update(headers)

# Get inputs
inputType = input('Input Type: ').upper()
amount = input('Amount: ')
outputType = input('Output Type: ').upper()

# Parameters about "what we want"
parameters = {
      'start':'1',
      'limit':'500',
      'convert': outputType
    }

response = session.get(url, params=parameters)# req
data = loads(response.text)# json

for crypto in data['data']:# find target type
    if crypto['symbol'] == inputType:
        result = round(crypto['quote'][outputType]['price'], 5) *float(amount)

        if result == 0:# If output is smaller than 1, dont round
            result = crypto['quote'][outputType]['price'] * float(amount)

        inputName = crypto['name']
        
    if crypto['symbol'] == outputType:
        outputName = crypto['name']
try:
  print('{} {}({}) = {} {}({})'.format(amount, inputType, inputName, result, outputType, outputName))
except:
  print('Invalid crypto or network error !')