import sys
import lexer


class Parser:
    def __init__(self,lexer):
        self.lexer = lexer
