import enum
import sys


class Token: #set and save information for the tokens
    def __init__(self,info,ttype):
        self.info = info
        self.ttype = ttype
class Tokens(enum.Enum): #tokens enum class
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
    INDENT='\t'
    NUMBER=None
class Lexer:
    token = None
    def __init__(self,file): #set the starting loaction of the reading
        self.input = file
        self.info = '\0'
        self.location = -1
        self.next()
    def next(self):    #iteration of the next location
        self.location += 1
        if self.location > len(self.input): # check the end of line
            self.info = '\0'
        else:
            self.info = self.input[self.location]
    def nextInfo(self): # check the info stored in the next location
        if self.location + 1 > len(self.input):
            return'\0'
        else:
            return self.input[self.location + 1]
    def build(self): # compare the information to get the token
        while self.info == ' ' or self.info == '\t' or self.info == '\r':
            self.next()
        while self.into == '#': #skip all comment
            while self.info != '\n':
                self.next()
        if self.info == '\0': #check the if it is the end
            token = Token(self.info,Tokens.EMP)
            print(self.info)
        elif self.info == '\t': # check to indentation
            start.self.location
            while self.nextInfo() == '\t':
                self.next()
            token = Token(self.info[start: self.location + 1],Tokens.INDENT)
            print(self.info)
        elif self.info == '+': #check for + or +=
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.PLUSEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.PLUS)
                print(self.info)
        elif self.info == '-': #check for - or-=
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.MINUSEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.MINUS)
                print(self.info)
        elif self.info == '*': #check for * or *=
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.TIMESEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.TIMES)
                print(self.info)
        elif self.info == '/': #check for / or /=
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.DIVIDEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.DIVID)
                print(self.info)
        elif self.info == '%': # check for % or %=
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.REMAINEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.REMAINDER)
                print(self.info)
        elif self.info == '^': #check for ^ or ^=
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.EXPEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.EXP)
                print(self.info)
        elif self.info == '<': #check for < or <=
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.GREATEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.GREAT)
                print(self.info)
        elif self.info == '>': #check for > or >=
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.LESSEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.LESS)
                print(self.info)
        elif self.info == '=': #check for = or ==
            if self.nextInfo()== '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.COMEQU)
                print(self.info)
            else:
                token = Token(self.info, Tokens.EQU)
                print(self.info)
        elif self.info == '!': #check for !=
            if self.nextInfo() == '=':
                inf = self.info
                self.next()
                token = Token(inf + self.info, Tokens.NOTEQU)
                print(self.info)
            else:
                self.next()
        elif self.info == ':': #check for :
            token = Token(self.info,Tokens.COL)
            print(self.info)
        elif self.info == '(': #check for (
            token = Token(self.info,Tokens.LP)
            print(self.info)
        elif self.info == ')': #check for )
            token = Token(self.info,Tokens.RP)
            print(self.info)
        elif self.info == ',': #check for ,
            token = Token(self.info,Tokens.COMMA)
            print(self.info)
        elif self.info.is_integer() == True: #check for numbers
            start = self.location
            while self.nextInfo.in_integer() == True:
                self.next()
            if self.nextInfo() == '.':
                self.next()
                while self.nextInfo.is_integer() == True:
                    self.next()
            token = Token(self.info[start: self.location + 1],Tokens.NUMBER)
            print(self.info)
        elif self.info.isalpha() == True: #check for words
            start = self.location
            while self.nextInfo().isalnum() == True or self.nextInfo() == '_':
                self.next()
            text = self.info[start: self.location + 1]
            print(self.info)
            if text == 'while': #check if words is keyword while
                token = Token(text, Tokens.WHILE)
                print(self.info)
            if text == 'if': #check if words is keyword if
                token = Token(text, Tokens.IF)
                print(self.info)
            if text == 'else': #check if words is keyword else
                token = Token(text, Tokens.ELSE)
                print(self.info)
            if text == 'ELIF': #check if words is keyword elif
                token = Token(text, Tokens.ELIF)
                print(self.info)
        self.next()
        return token
