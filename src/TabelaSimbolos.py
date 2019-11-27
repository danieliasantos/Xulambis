#!/usr/bin/python
#-*- coding: utf-8 -*-

import platform

if platform.sys.platform.__contains__("linux"):
    from src.Token import Token
else:
    from Token import Token

class TabelaSimbolos(object):

    __hashTokens = {
        "int": Token('int', 'int'),
        "float": Token('float', 'float'),
        "bool": Token('bool', 'bool'),
        "double": Token('double', 'double'),
        "string": Token('string', 'string'),
        "true": Token('true', 'true'),
        "false": Token('false', 'false'),
        "if": Token('if', 'if'),
        "else": Token('else', 'else'),
        "while": Token('while', 'while'),
        "break": Token('break', 'break'),
        "{": Token('{', '{'),
        "}": Token('}', '}'),
        "(": Token('(', '('),
        ")": Token(')', ')'),
        "[": Token('[', '['),
        "]": Token(']', ']'),
        ";": Token(';', ';'),
        "=": Token('=', '='),
        "+": Token('+', '+'),
        "-": Token('-', '-'),
        "*": Token('*', '*'),
        "/": Token('/', '/'),
        "<": Token('<', '<'),
        ">": Token('>', '>'),
        ">=": Token('>=', '>='),
        "<=": Token('<=', '<='),
        "!=": Token('!=', '!='),
        "==": Token('==', '=='),
        "&&": Token('&&', '&&'),
        "||": Token('||', '||'),
        "!": Token('!', '!')
    }

    def isToken (self, lexema):
        return lexema in self.__hashTokens

    def getSimbolo(self, lexema):
        return self.__hashTokens[lexema]
