import requests
import json

data = {}
data['Auth'] = {}
data['Auth']['galaxId'] = "4858"
data['Auth']['galaxHash'] = "20T12zXtOoV2XjNlDrImSdI7OsWmSoFbC3GrIsIt"
data['Request'] = {}
data['Request']['internalId'] = "8"
print(json.dumps(data, sort_keys=False, indent=4))

url = 'https://app.galaxpay.com.br/webservice/getPaymentBillInfo'

r = requests.get(url, json=data)
data_json = r.json()
print(data_json.get('paymentBill').get('transactions')[0].get('internalId'))
print(json.dumps(r.json(), indent=4))
