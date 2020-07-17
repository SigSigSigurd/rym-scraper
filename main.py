import re
import string

from rymscraper.rateyourmusic import RateYourMusic

#RYM object
rym = RateYourMusic()

def sub(arg: string, comm: string):
    return arg[len(comm):len(arg)]

def artist(arg: string):
    a = sub(arg,"artist ")
    n = re.search(r'\-\d*', a)
    if re.sub(r'\s', '', a)=="":
        print("Filler!")
    else:
        if n==None:
            x = 0
            b = rym.artists(a)
            if len(b)>1:
                print("Did you mean:")
                i = 0
                for y in b:
                    i+=1
                    z = y.find('b', first=True)
                    print(str(i)+". "+z.text)
                print ("Specify with -# flag!")
        else:
            x = int(n.group()[1:len(n.group())])
            print(rym.artist(a, x))

def null(arg):
    print("The command: \'"+arg+"\' does not exist!")

#handles inputs
def comm(arg: string):
    d = {
        "artist": artist
    }
    y = None
    for i in d.keys():
        r = r'^'+re.escape(i)
        x = re.search(r, arg)
        c = d.get(x.group()) if x!=None else null
        return c

class Main:

    def main():
        #main loop
        print("RYM Scraper built by Tatsu Eliason")
        while True:
            i = input("\n>")
            c = comm(i)
            c(i)

    if __name__ == "__main__":
        main()
