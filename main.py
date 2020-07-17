import re
import string

from rymscraper.rateyourmusic import RateYourMusic

#RYM object
rym = RateYourMusic()

def sub(arg: string, comm: string):
    return arg[len(comm):len(arg)]

def artist(arg: string):
    a = sub(arg,"artist ")
    print(rym.sArtistTop(a, 0))

def null():
    pass

#handles inputs
def comm(arg: string):
    d = {
        "artist": artist
    }
    y = None
    for i in d.keys():
        r = r'^'+re.escape(i)
        x = re.search(r, arg)
        if x!=None:
            c = d.get(x.group())
            return c

class Main:

    def main():
        while True:
            i = input(">")
            c = comm(i)
            if c!=None:
                c(i)

    if __name__ == "__main__":
        main()
