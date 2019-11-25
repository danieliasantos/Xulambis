#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import platform
import sys

if platform.sys.platform.__contains__("linux"):
    from src.TabelaSimbolos import TabelaSimbolos
    from src.Token import Token
else:
    from TabelaSimbolos import TabelaSimbolos
    from Token import Token



class AnaliseLexica(object):
    __listaCodigo = []

    def __init__(self, lista):
        self.__lexemas = re.compile('[a-z]|[0-9]+|[\{]|[\}]|[\(]|[\)]|[\[]|[\]]|[\;]|[\=]|[\+]|[\-]|[\*]|[\/]|[\<]|[\>]|[\!]|[\&]|[\|]|[\.]|[\s]')
        if len(lista) > 0:
            self.__listaCodigo = lista

    def isFloat(self, str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    def analisaTokens(self, lista):
        tokens = TabelaSimbolos()
        whiteSpace = ' '
        lexema = ''
        for l, linha in enumerate(self.__listaCodigo):
            for c, char in enumerate(linha):
                if self.__lexemas.search(char) is None:
                    print('%s %.2d: \"%s\" %s \"%s\"' % ('Erro léxico na linha', l, linha, '=> Lexema desconhecido:', char))
                    break
                else:
                    if tokens.isToken(char):
                        lexema += char
                        if c + 1 < len(linha):
                            if tokens.isToken(lexema + linha[c + 1]):
                                c += 1
                                lexema += linha[c]
                        lista.append(tokens.getSimbolo(lexema))
                        lexema = ''
                    else:
                        if char is not whiteSpace:
                            lexema += char
                            if c + 1 < len(linha):
                                if tokens.isToken((linha[c + 1])) or linha[c + 1] is whiteSpace:
                                    if tokens.isToken(lexema):
                                        lista.append(tokens.getSimbolo(lexema))
                                        c += 1
                                        lexema = ''
                                    else:
                                        if lexema.__str__().isnumeric() or self.isFloat(lexema):
                                            lista.append(Token(lexema, 'number'))
                                        else:
                                            lista.append(Token(lexema, 'id'))
                                        lexema = ''
            else:
                continue #continua executando for interno se o  <if self.__lexemas.search(char) is None: for false
            print('Programa finalizado.')
            sys.exit()
            break #para a execução de todos os loops quando o <if self.__lexemas.search(char) is None:> for true

'''
for l in lista:
    if ';' in l:
        txt = re.findall('.*?[;]', l)
        for t in txt:
            self.__listaCodigo.append(t.__str__().lstrip())
    else:
        self.__listaCodigo.append(l)

regex = re.compile('[\{]|'
                   '([a-zA-Z]+[\s]+(([a-zA-Z]+[\s]*[\;])|(([a-zA-Z]+[\s]+)*[\=]+[\s]+(([0-9]+([\.][0-9]+)*[\;]*)|'
                   '([a-zA-Z]+[\s]*[\;])|(([a-zA-Z]+|[0-9]+([\.][0-9]+)*)[\s]*([\+]|[\-]|[\*]|[\/])[\s]*([a-zA-Z]+|[0-9]+([\.][0-9]+)*)[\;]*)))))|'
                   '([a-zA-Z]+[\s]+[\(]+[\s](([a-zA-Z]+[\s][\)])|([a-zA-Z]+[\s]([<]|[>]|[>=]|[<=]|[!=]|[==])[\s]([a-zA-Z]+|[0-9]+)[\s][\)]))[\s]([\{]|[a-zA-Z]+[\;]*))|'
                   '([a-zA-Z]+[\;]*)|'
                   '[\}]')
'''