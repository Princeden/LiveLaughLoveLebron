import urllib.request
import urllib.parse
import json
import zlib
from .api import *


def getCards():
    data = getNeededCards(52)
    cardData = []
    for card in data:
        cardData.append({"value": card["value"], "suit": card["suit"]})
    return cardData
