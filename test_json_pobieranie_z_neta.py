import json
import requests as re
from pydantic import BaseModel

# response = re.get('http://api.weatherapi.com/v1/current.json?key=d863af85e8fa43618f682810220812&q=Lublin&aqi=no')
response = re.get('http://api.nbp.pl/api/exchangerates/rates/A/EUR/')

# 200 - ok
# 3 ...
# 4 ... błąd odpowiedzi 404 - strona nie istnieje
# 5 .. bład serwer
dane = response.json()
print(dane)
print(type(dane))
print(dane['rates'][0]['mid'])

date_to_json = json.dumps(dane)

with open('waluta.json', 'w') as f:
    json.dump(dane, f, indent=4, sort_keys=False)

with open('waluta.json', 'r') as f:
    pogoda = json.load(f)

# print(pogoda['location']['name'])

json_dict = {'table': 'A', 'currency': 'euro', 'code': 'EUR',
             'rates': [{'no': '068/A/NBP/2023', 'effectiveDate': '2023-04-06', 'mid': 4.6902}]}
json_string = json.dumps(json_dict)


class Rate(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class CurrencyData(BaseModel):
    table: str
    currency: str
    code: str
    rates: list[Rate]


currency_data = CurrencyData.parse_raw(json_string)
print(currency_data)
print(currency_data.code)
print(currency_data.rates[0].mid)
# 15:00