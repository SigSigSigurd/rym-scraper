import string
import random
import requests
from requests_html import HTMLSession

class RateYourMusic:
    def __init__(self):
        self.s = HTMLSession()
        pass

    def sArtistTop(self, s: string, n: int):
        r = self.s.get(sURL()+"&searchtype=a&searchterm="+s).html
        res = r.find('.infobox', first=False)
        for l in res[n].absolute_links:
            if "https://rateyourmusic.com/artist/" in l:
                aURL = l
                break
        r = self.s.get(aURL).html
        res = r.find('.artist_info', first=True)
        return res.text

def sURL():
    return "https://rateyourmusic.com/search?bx="+"".join(random.choice(string.ascii_lowercase+string.digits) for i in range(32))
