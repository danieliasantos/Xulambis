#!/usr/bin/python
# -*- coding: utf-8 -*-
import platform
import re
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
        self.__tokens = TabelaSimbolos()
        if len(lista) > 0:
            self.__listaTokens = lista

    def __S(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is '{':
            return True and self.__A(i + 1)
        print('Erro regra S:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: {\n    Encontrado:', tipo)
        return False

    def __A(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is 'int' or tipo is 'double' or tipo is 'float' or tipo is 'bool' or tipo is 'string':
            print(self.__listaTokens[i].getToken())
            return True and self.__C(i + 1)
        if tipo is 'id':
            print(self.__listaTokens[i].getToken())
            return True and self.__E(i + 1)
        if tipo is "if" or tipo is "while":
            print(self.__listaTokens[i].getToken())
            return True and self.__I(i + 1)
        if tipo is '}':
            print(self.__listaTokens[i].getToken())
            return True and self.__B(i + 1)
        print('Erro regra A:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: id, int, double, float, bool, string, if, while ou }\n    Encontrado:', tipo)
        return False

    def __B(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is '}':
            print(self.__listaTokens[i].getToken())
            return True
        print('Erro regra B:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: }\n    Encontrado:', tipo)
        return False

    def __C(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is 'id':
            print(self.__listaTokens[i].getToken())
            return True and self.__E(i + 1)
        print('Erro regra C:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: id\n    Encontrado:', tipo)
        return False

    def __D(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is ';':
            print(self.__listaTokens[i].getToken())
            return True and self.__A(i + 1)
        print('Erro regra D:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: ;\n    Encontrado:', tipo)
        return False

    def __E(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is '=':
            print(self.__listaTokens[i].getToken())
            return True and self.__G(i + 1)
        if tipo is ';':
            print(self.__listaTokens[i].getToken())
            return True and self.__A(i + 1)
        print('Erro regra E:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: = ou ;\n    Encontrado:', tipo)
        return False

    def __F(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is ')':
            print(self.__listaTokens[i].getToken())
            return True and self.__L(i + 1)
        print('Erro regra F:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: )\n    Encontrado:', tipo)
        return False

    def __G(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is 'number' or tipo is 'id' or tipo is 'false' or tipo is 'true':
            print(self.__listaTokens[i].getToken())
            return True and self.__H(i + 1)
        print('Erro regra G:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: number, id, true ou false\n    Encontrado:', tipo)
        return False

    def __H(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is ';':
            print(self.__listaTokens[i].getToken())
            return True and self.__A(i + 1)
        if tipo is '/' or tipo is '-' or tipo is '*' or tipo is '+':
            print(self.__listaTokens[i].getToken())
            return True and self.__G(i + 1)
        print('Erro regra H:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: ;, +, -, * ou /\n    Encontrado:', tipo)
        return False

    def __I(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is '(':
            print(self.__listaTokens[i].getToken())
            return True and self.__J(i + 1)
        print('Erro regra I:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: (\n    Encontrado:', tipo)
        return False

    def __J(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is 'id':
            print(self.__listaTokens[i].getToken())
            return True and self.__M(i + 1)
        if tipo is 'true':
            print(self.__listaTokens[i].getToken())
            return True and self.__F(i + 1)
        print('Erro regra J:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: id ou true\n    Encontrado:', tipo)
        return False

    def __K(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is 'id':
            print(self.__listaTokens[i].getToken())
            return True and self.__F(i + 1)
        print('Erro regra K:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: id\n    Encontrado:', tipo)
        return False

    def __L(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is 'break':
            print(self.__listaTokens[i].getToken())
            return True and self.__D(i + 1)
        if tipo is '{':
            print(self.__listaTokens[i].getToken())
            return True and self.__A(i + 1)
        print('Erro regra L:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: break ou {\n    Encontrado:', tipo)
        return False

    def __M(self, i):
        tipo = self.__listaTokens[i].getTipo()
        if tipo is ')':
            print(self.__listaTokens[i].getToken())
            return True and self.__L(i + 1)
        if tipo is '&&' or tipo is '||' or tipo is '>' or tipo is '>=' or tipo is '<' or tipo is '<=' or tipo is '!=' or tipo is '==' or tipo is '!':
            print(self.__listaTokens[i].getToken())
            return True and self.__K(i + 1)
        print('Erro regra M:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: ), >, <, <=, >=, &&, ||, ==, != ou !\n    Encontrado:', tipo)
        return False

    def analisaTokens(self):
        i = 0 #controle da posicao no vetor __listaTokens
        if self.__S(i) and i == len(self.__listaTokens) - 1:
            print('Analise sintatica finalizada sem erro.')
        else:
            print('Analise sintatica finalizada com erro.')

'''
    def __aceito(self, t):
        if t.getTipo() == "id":
            return (True if self.__lexemas.search(t.getLexema()) is not None else False)
        return(True if self.__tokens.isToken(t) else False)
'''
