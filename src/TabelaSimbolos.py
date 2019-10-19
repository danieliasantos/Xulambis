#!/usr/bin/python
#-*- coding: utf-8 -*-

import platform

if platform.sys.platform.__contains__("win"):
    from Token import Token
else:
    from src.Token import Token

class TabelaSimbolos(object):
    __hashSymbols = {
        "int",
        "float",
        "bool",
        "double",
        "true",
        "false",
        "if",
        "while",
        "break",
        "{",
        "}",
        "(",
        ")",
        "[",
        "]",
        ";",
        "=",
        "+",
        "<",
        ">",
        ">=",
        "<=",
        "!=",
        "==",
    }
    def lexExists (self, lexema):
        return lexema in self.__hashSymbols

    def getToken(self, lexema):
        return self.__hashSymbols[lexema]