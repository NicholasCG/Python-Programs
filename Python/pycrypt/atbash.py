import string

class Atbash(object):
    def __init__(self):
        self.key = string.ascii_uppercase[::-1]

    def encrypt(self,strings):
        
        strings = strings.upper()

        newString = ""
        
        for x in strings:
            if x not in string.ascii_uppercase:
                newString += x
            else:
                newString += self.key[string.ascii_uppercase.index(x)]
        return newString
        
    def decrypt(self,strings):
    
        strings = strings.upper()

        oldString = ""

        for x in strings:
            if x not in string.ascii_uppercase:
                oldString += x
            else:
                oldString += self.key[string.ascii_uppercase.index(x)]
        return oldString     

