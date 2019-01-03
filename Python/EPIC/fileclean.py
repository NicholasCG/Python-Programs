class _Fileclean(object):
    def __init__(self, original):
        self.origin = original
    def bfclean(self):
        text = open(self.origin,"r")
        w = text.readlines()
        newtext = ""
        for line in w:
            for x in line:
                if x in ['<','>','+','-',',','.','[',']']:
                    newtext += x
        return newtext