import requests
from .utils.encoders import ObjectJsonSerializable


class GalaxPayClient(ObjectJsonSerializable):
    def __init__(self, sale, auth):
        self.sale = None
        self.auth = None

    def createPaymentBill(self):
        pass
        #url = 'https://app.galaxpay.com.br/webservice/createPaymentBill'

        #payload = sale.toJSON()
        #r = requests.post(url, data=payload)
        # print(r.json)
