import random
import pyqrcode
import png
from pyqrcode import QRCode
from django.conf import settings


def generateNin(digits):
    """Method that generate NIN"""

    lower = 10 ** (digits - 1)
    upper = 10**digits - 1
    return random.randint(lower, upper)


def create_qrcode(email):
    s = "Email: {} and Password: {}".format(email, settings.DEFAULT_PASSWORD)
    url = pyqrcode.create(s)
    return url.png("{}-barcode.png".format(email), scale=6)
