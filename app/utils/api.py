import urllib.request
import urllib.parse
import json
import zlib


def getNeededCards(n):
    url = f"https://deckofcardsapi.com/api/deck/new/draw/?count={n}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data.get("cards", [])     
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}, {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
