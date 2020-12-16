import enum
import sys


class Token:
    def __init__(self,info,ttype):
        self.info = info
        self.ttype = ttype
    
class Lexer:
    token = None
    def __init__(self,file):
        self.input = file + '\n'
        self.info = ''
        self.location = -1
        self.next()

    def next(self):
        self.location += 1
        if self.location > len(self.input):
            self.info = '\0'
        else:
            self.info = self.input[self.location]

    def nextInfo(self):
        if self.location + 1 > len(self.input):
            return'\0'
        else:
            return self.input[self.location + 1]

    def build(self):
        while self.info == ' ' or self.info == '\t' or self.info == '\r':
            self.next()
        while self.into == '#':
            while self.info != '\n':
                self.next()
        
        if self.info == '\0':
            token = Token(self.info,Tokens.EMP)
            print(self.info)
        elif self.info == '\t':
            start.self.location
            while self.nextInfo() == '\t':
                self.next()
            token = Token(self.info[start: self.location + 1],Tokens.INDENT)
            print(self.info)
        elif self.info == '+':
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.PLUSEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.PLUS)
                print(self.info)
        elif self.info == '-':
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.MINUSEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.MINUS)
                print(self.info)
        elif self.info == '*':
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.TIMESEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.TIMES)
                print(self.info)
        elif self.info == '/':
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.DIVIDEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.DIVID)
                print(self.info)

        elif self.info == '%':
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.REMAINEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.REMAINDER)
                print(self.info)
        elif self.info == '^':
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.EXPEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.EXP)
                print(self.info)
        elif self.info == '<':
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.GREATEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.GREAT)
                print(self.info)
        elif self.info == '>':
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.LESSEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.LESS)
                print(self.info)
        elif self.info == '=':
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.COMEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.EQU)
                print(self.info)

        elif self.info == '!':
            if self.nextInfo() == '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.NOTEQU)
                print(self.info)
            else:
                self.next()
        elif self.info == ':':
            token = Token(self.info,Tokens.COL)
            print(self.info)
        elif self.info == '(':
            token = Token(self.info,Tokens.LP)
            print(self.info)
        elif self.info == ')':
            token = Token(self.info,Tokens.RP)
            print(self.info)
        elif self.info == ',':
            token = Token(self.info,Tokens.COMMA)
            print(self.info)
        elif self.info.is_integer() == True:
            start = self.location
            while self.nextInfo.in_integer() == True:
                self.next()
            if self.nextInfo() == '.':
                self.next()
                while self.nextInfo.is_integer() == True:
                    self.next()
            token = Token(self.info[start: self.location + 1],Tokens.NUMBER)
            print(self.info)
        elif self.info.isalpha() == True:
            start = self.location
            while self.nextInfo().isalnum() == True or self.nextInfo() == '_':
                self.next()
            text = self.info[start: self.location + 1]
            print(self.info)
            if text == 'while':
                token = Token(text, Tokens.WHILE)
                print(self.info)
            if text == 'if':
                token = Token(text, Tokens.IF)
                print(self.info)
            if text == 'else':
                token = Token(text, Tokens.ELSE)
                print(self.info)
            if text == 'ELIF':
                token = Token(text, Tokens.ELIF)
                print(self.info)
        self.next()
        return token
        
        
class Tokens(enum.Enum):
    EMP='\n'      #\0
    PLUS='+'     #+
    MINUS='-'    #-
    TIMES='*'    #*
    DIVID='/'    #/
    REMAINDER='%'#%
    EXP='^'      #^
    EQU='='      #=
    PLASEQU='+='  #+=
    MINUSEQU='-=' #-=
    TIMESEQU='*=' #*=
    DIVIDEQU='/=' #/=
    EXPEQU='^='   #^=
    REMAINEQU='%='#%=
    GREAT='<'    #<
    GREATEQU='<=' #<=
    LESS='>'     #>
    LESSQUE='>='  #>=
    COMEQU='=='   #==
    NOTEQU='!='   #!=
    COL=':'      #:
    LP='('       #(
    RP=')'       #)
    COMMA=','    #,
    IF='if'
    ELSE='else'
    ELIF='elif'
    PRINT='print'
    FOR='for'
    INDENT='    '
    NUMBER=None
    

