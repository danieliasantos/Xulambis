#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import platform

if platform.sys.platform.__contains__("win"):
    from TabelaSimbolos import TabelaSimbolos
    from Token import Token
else:
    from src.TabelaSimbolos import TabelaSimbolos
    from src.Token import Token

class AnaliseLexica(object):

    __listTokens = []
    __listaCodigo = []

    def __init__(self, lista):
        __regex = re.compile('[{]|'
                             '([a-zA-Z]+[\s]+(([a-zA-Z]+[\s]*[\;])|(([a-zA-Z]+[\s]+)*[\=]+[\s]+(([0-9]+([\.][0-9]+)*[\;]*)|'
                             '([a-zA-Z]+[\s]*[\;])|(([a-zA-Z]+|[0-9]+([\.][0-9]+)*)[\s]*([\+]|[\-]|[\*]|[\/])[\s]*([a-zA-Z]+|[0-9]+([\.][0-9]+)*)[\;]*)))))|'
                             '([a-zA-Z]+[\s]+[\(]+[\s](([a-zA-Z]+[\s][\)])|([a-zA-Z]+[\s]([<]|[>]|[>=]|[<=]|[!=]|[==])[\s]([a-zA-Z]+|[0-9]+)[\s][\)]))[\s]([\{]|[a-zA-Z]+[\;]*))|'
                             '([a-zA-Z]+[\;]*)|'
                             '[\}]')
        if len(lista) > 0:
            self.__listaCodigo = lista

    def regexTest(self, linha):
        self.__regex.match(linha)

    def analyseLexems(self):
        tokens = TabelaSimbolos()
        for i in self.__listaCodigo:
            line = i
            v = line.__str__().split(';')
            for j in v:
                l = j
                if self.regexTest(l):
                    if tokens.lexExists(l):
                        self.__listTokens.append(l)
                    else:
                        self.__listTokens.append(Token('id', l))

    def printTokens(self):
        print(self.__listTokens)