#!/usr/bin/python
# -*- coding: utf-8 -*-
import platform
import re
import sys

if platform.sys.platform.__contains__("linux"):
    from src.TabelaSimbolos import TabelaSimbolos
    from src.Token import Token
else:
    from TabelaSimbolos import TabelaSimbolos
    from Token import Token

class AnaliseSemantica(object):

    __listaTokens = []

    def __init__(self, lista):
        self.__tokens = TabelaSimbolos()
        if len(lista) > 0:
            self.__listaTokens = lista