import requests
import json

data = {}
data['Auth'] = {}
data['Auth']['galaxId'] = ""
data['Auth']['galaxHash'] = ""
data['Request'] = {}
data['Request']['internalId'] = "8"
print(json.dumps(data, sort_keys=False, indent=4))

url = 'https://app.galaxpay.com.br/webservice/getPaymentBillInfo'

r = requests.get(url, json=data)
data_json = r.json()
print(data_json.get('paymentBill').get('transactions')[0].get('internalId'))
print(json.dumps(r.json(), indent=4))