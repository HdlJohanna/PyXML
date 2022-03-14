from urllib.request import urlopen

class XMLDocument:
    def __init__(self):
        self.code = ""

    def match(self,text):
        return text in self.code
    
    def load(self,fp):
        self.code = fp.read()

    def loadf(self,filename,url:bool=False):
        if url:
            req = urlopen(filename)
            self.code = req.read().decode('utf-8')
        else:
            self.code = open(filename).read()

    def loads(self,code):
        self.code = code
