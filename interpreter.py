import sys
from lexer import Lexer,Token,Tokens
#import parser

def interpreter():
    if len(sys.argv) != 2:
        print("Need more information!")
        return
    file = open(sys.argv[1]).read
    tokens = Lexer(file)
    token = lexer.build()
    while token.ttype != Tokens.EMP:
        token = lexer.build()
    print(tokens)
    parser = Parser(tokens)

    
interpreter()
