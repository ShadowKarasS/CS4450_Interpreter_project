import sys
from lexer import Lexer,Token,Tokens
#import parser

def interpreter():
    if len(sys.argv) != 2: # check for input file exist
        print("Need more information!")
        return
    file = open(sys.argv[1]).read #read input file
    tokens = Lexer(file)
    token = lexer.build()
    while token.ttype != Tokens.EMP: # create tokens
        token = lexer.build()
    print(tokens)
    parser = Parser(tokens) #input tokens into parser

    
interpreter()
