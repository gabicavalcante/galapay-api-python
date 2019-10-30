import re
from .utils.encoders import ObjectJsonSerializable

BRAND_VISA = "visa"
BRAND_MASTERCARD = "mastercard"
BRAND_AMEX = "american express"
BRAND_DISCOVER = "discover"
BRAND_DANKORT = "dankort"
BRAND_MAESTRO = "maestro"
BRAND_DINERS = "diners club"

BRANDS = {
    BRAND_VISA: re.compile(r"^4\d{12}(\d{3})?$"),
    BRAND_MASTERCARD: re.compile(
        r"""
        ^(5[1-5]\d{4}|677189)\d{10}$|
        ^(222[1-9]|2[3-6]\d{2}|27[0-1]\d|2720)\d{12}$
    """,
        re.VERBOSE,
    ),
    BRAND_AMEX: re.compile(r"^3[47]\d{13}$"),
    BRAND_DISCOVER: re.compile(r"^(6011|65\d{2})\d{12}$"),
    BRAND_DANKORT: re.compile(r"^(5019)\d{12}$"),
    BRAND_MAESTRO: re.compile(r"^(?:5[0678]\d\d|6304|6390|67\d\d)\d{8,15}$"),
    BRAND_DINERS: re.compile(r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$"),
}


class CreditCard(ObjectJsonSerializable):
    def __init__(self):
        self.number = None
        self.holder = None
        self.expiryMonth = None
        self.expiryYear = None
        self.cvv = None
        self.brand = None

    @staticmethod
    def get_brand(number):
        number = number.replace(" ", "")
        for brand, regexp in BRANDS.items():
            if regexp.match(number):
                return brand
        return None
