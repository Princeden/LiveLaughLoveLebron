import urllib.request
import urllib.parse
import json
import zlib
from .api import *
from project import *


def getCards():
    n = getUsers()
    data = getNeededCards(n)
    cardData = []
    for card in data:
        cardData.append({"value": card["value"], "suit": card["suit"]})
    return cardData
