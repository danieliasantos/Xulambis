#!/usr/bin/python
# -*- coding: utf-8 -*-
import platform
import sys

if platform.sys.platform.__contains__("win"):
    from TabelaSimbolos import TabelaSimbolos
    from Token import Token
else:
    from src.TabelaSimbolos import TabelaSimbolos
    from src.Token import Token

class AnaliseSintatica(object):

    __listaTokens = []

    def __init__(self, lista):
        if len(lista) > 0:
            self.__listaCodigo = lista

    def analisaTokens(self):
        tokens = TabelaSimbolos()
