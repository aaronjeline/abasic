class Keyword():
    def __init__(self,keyword):
        self.keyword = keyword

    def __str__(self):
        return ("KEYWORD("+self.keyword+")")

class Comma():
    def __str__(self):
        return "COMMA"

class Number():
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Operator():
    def __init__(self,op):
        self.op = op

    def __str__(self):
        return op

class Seperator():
    def __str__(self):
        return 'SEPERATOR'


class String():
    def __init__(self,string):
        self.string = string

    def __str__(self):
        return self.string

class Identifier():
    def __init__(self, i):
        self.i = i

    def __str__(self):
        return self.i

digits = ('1','2','3','4','5','6','7','8','9')
quote = '"'
comma = ','
bang = '!'
whitespace = (' ', '    ')
operators = ('+', '-','=','*','/','<','>')
keywords = ('PRINT','IF','THEN')

def tokenize(line):
    tokens = []
    cur = ""
    inString = False
    inNumber = False
    for c in line:
        if inNumber:
            if c in digits:
                cur += c
        else:
                tokens.append(Number(int(cur)))
                inNumber = False
                cur = ""
        if inString:
            if c == quote:
                inString = False
                tokens.append(String(cur))
                cur = ""
            else:
                cur += c
        elif inNumber:
            if c in digits:
                cur += c
            else:
                tokens.append(Number(int(cur)))
                inNumber = False
                cur = ""
        elif c in operators:
            #Clear the cur
            if cur != "":
                tokens.append(Identifier(cur))
                cur = ""
            tokens.append(Operator(c))
        elif c == quote:
            if cur != "":
                tokens.append(Identifier(cur))
                cur = ""
            inString = True
        elif c in digits:
            cur += c
            inNumber = True
        elif c == comma:
            if cur != "":
                tokens.append(Identifier(cur))
                cur = ""
            tokens.append(Comma())
        elif c == comma:
            if cur != "":
                tokens.append(Identifier(cur))
                cur = ""
            tokens.append(Seperator())
        elif c in whitespace:
            if cur != "":
                tokens.append(Identifier(cur))
                cur = ""
        else:
            #It's a character
            cur += c
            if cur in keywords:
                tokens.append(Keyword(cur))
                cur = ""
    if cur!= '':
        if inNumber:
            tokens.append(Number(int(cur)))
        else:
            raise Exception('Invalid Line Ending!')

    return tokens








