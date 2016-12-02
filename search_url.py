import re

def search_url(path):

    with open(path,"rb") as file:
        #return re.findall(r'(https?|ftp|file)://.+',file.read())
        
        return re.findall(r'https?://[^;]+',file.read())

if __name__ == '__main__':
    print "Find %d URLs." % len(search_url("test.txt"))
    for item in search_url("test.txt"):
        print item
