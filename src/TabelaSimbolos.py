#!/usr/bin/python
#-*- coding: utf-8 -*-

class TabelaSimbolos(object):
    __hashSymbols = [
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
    ]

    def lexExists (self, lexema):
        return lexema in self.__hashSymbols
