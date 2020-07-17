import string
import random
import requests
from requests_html import HTMLSession

class RateYourMusic:
    def __init__(self):
        self.s = HTMLSession()
        pass

    # returns a list with all artists in a search
    def artists(self, s: string):
        i = []
        r = self.s.get(sURL()+"&searchtype=a&searchterm="+s).html
        res = r.find('.infobox', first=False)
        for x in res:
            i.append(x)
        return i

    # returns the profile of an artist based on the order they appear in a search (n argument)
    def artist(self, s: string, n: int):
        r = self.s.get(sURL()+"&searchtype=a&searchterm="+s).html
        res = r.find('.infobox', first=False)
        for l in res[n-1].absolute_links:
            if "https://rateyourmusic.com/artist/" in l:
                aURL = l
                break
        r = self.s.get(aURL).html
        res = r.find('.artist_info', first=True)
        return res.text

def sURL():
    return "https://rateyourmusic.com/search?bx="+"".join(random.choice(string.ascii_lowercase+string.digits) for i in range(32))
