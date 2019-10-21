#!/usr/bin/python
#-*- coding: utf-8 -*-

if platform.sys.platform.__contains__("win"):
    from Token import Token
else:
    from src.Token import Token

class TabelaSimbolos(object):

    __hashTokens = {
        "int": Token('int', 'keyword'),
        "float": Token('float', 'keyword'),
        "bool": Token('bool', 'keyword'),
        "double": Token('double', 'keyword'),
        "string": Token('string', 'keyword'),
        "true": Token('double', 'keyword'),
        "false": Token('false', 'keyword'),
        "if": Token('if', 'keyword'),
        "else": Token('else', 'keyword'),
        "while": Token('while', 'keyword'),
        "break": Token('break', 'keyword'),
        "{": Token('{', 'delimiter'),
        "}": Token('{', 'delimiter'),
        "(": Token('{', 'delimiter'),
        ")": Token('{', 'delimiter'),
        "[": Token('{', 'delimiter'),
        "]": Token('{', 'delimiter'),
        ";": Token('{', 'delimiter'),
        "=": Token('=', 'operation'),
        "+": Token('+', 'operation'),
        "-": Token('-', 'operation'),
        "*": Token('*', 'operation'),
        "/": Token('/', 'operation'),
        "<": Token('<', 'logical'),
        ">": Token('>', 'logical'),
        ">=": Token('>=', 'logical'),
        "<=": Token('<=', 'logical'),
        "!=": Token('!=', 'logical'),
        "==": Token('==', 'logical')
    }

    def lexExists (self, lexema):
        return lexema in self.__hashSymbols

    def getToken(self, lexema):
        return self.__hashTokens[lexema]
