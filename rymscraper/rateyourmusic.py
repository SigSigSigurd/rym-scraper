import string
import random
import requests
from requests_html import HTMLSession

class RateYourMusic:
    def __init__(self):
        self.s = HTMLSession()
        pass

    def sArtist(self, s: string):
        r = self.s.get(sURL()+"&searchtype=a&searchterm="+s).html
        res =list(r.find('.infobox', first=False))
        return res[0].text


def sURL():
    return "https://rateyourmusic.com/search?bx="+"".join(random.choice(string.ascii_lowercase+string.digits) for i in range(32))
