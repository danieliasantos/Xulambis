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

class AnaliseSintatica(object):

    #__i = 0
    __listaTokens = []

    def __init__(self, lista):
        self.__tokens = TabelaSimbolos()
        if len(lista) > 0:
            self.__listaTokens = lista

    def __S(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == '{':
            return True and self.__A(i + 1)
        print('Erro regra S:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: {\n    Encontrado:', tipo)
        return False

    def __A(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == 'int' or tipo == 'double' or tipo == 'float' or tipo == 'bool' or tipo == 'string':
            return True and self.__C(i + 1)
        if tipo == 'id':
            return True and self.__E(i + 1)
        if tipo == "if" or tipo == "while":
            return True and self.__I(i + 1)
        if tipo == '}':
            return True and self.__B(i + 1)
        print('Erro regra A:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: id, int, double, float, bool, string, if, while ou }\n    Encontrado:', tipo)
        return False

    def __B(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == '}' and i == len(self.__listaTokens) - 1:
            return True
        elif tipo == '}':
            return True and self.__B(i + 1)
        else:
            print('Erro regra B:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: }\n    Encontrado:', tipo)
            return False

    def __C(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == 'id':
            return True and self.__E(i + 1)
        print('Erro regra C:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: id\n    Encontrado:', tipo)
        return False

    def __D(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == ';':
            return True and self.__A(i + 1)
        print('Erro regra D:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: ;\n    Encontrado:', tipo)
        return False

    def __E(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == '=':
            return True and self.__G(i + 1)
        if tipo == ';':
            return True and self.__A(i + 1)
        print('Erro regra E:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: = ou ;\n    Encontrado:', tipo)
        return False

    def __F(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == ')':
            return True and self.__L(i + 1)
        print('Erro regra F:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: )\n    Encontrado:', tipo)
        return False

    def __G(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == 'number' or tipo == 'id' or tipo == 'false' or tipo == 'true':
            return True and self.__H(i + 1)
        print('Erro regra G:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: number, id, true ou false\n    Encontrado:', tipo)
        return False

    def __H(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == ';':
            return True and self.__A(i + 1)
        if tipo == '/' or tipo == '-' or tipo == '*' or tipo == '+':
            return True and self.__G(i + 1)
        print('Erro regra H:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: ;, +, -, * ou /\n    Encontrado:', tipo)
        return False

    def __I(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == '(':
            return True and self.__J(i + 1)
        print('Erro regra I:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: (\n    Encontrado:', tipo)
        return False

    def __J(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == 'id':
            return True and self.__M(i + 1)
        if tipo == 'true':
            return True and self.__F(i + 1)
        print('Erro regra J:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: id ou true\n    Encontrado:', tipo)
        return False

    def __K(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == 'id' or tipo == 'number':
            return True and self.__F(i + 1)
        print('Erro regra K:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: id\n    Encontrado:', tipo)
        return False

    def __L(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == 'break':
            return True and self.__D(i + 1)
        if tipo == '{':
            return True and self.__A(i + 1)
        print('Erro regra L:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: break ou {\n    Encontrado:', tipo)
        return False

    def __M(self, i):
        tipo = self.__listaTokens[i].getTipo()
        #print(self.__listaTokens[i].getToken())
        if tipo == ')':
            return True and self.__L(i + 1)
        if tipo == "||" or tipo == "==" or tipo == "&&" or tipo == ">" or tipo == ">=" or tipo == "<" or tipo == "<=" or tipo == "!=" or tipo == "!":
            return True and self.__K(i + 1)
        print('Erro regra M:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: ), >, <, <=, >=, &&, ||, ==, != ou !\n    Encontrado:', tipo)
        return False

    def analisaTokens(self):
        i = 0 # controle da posicao no vetor listaTokens
        if self.__S(i):
            print('Analise Sintatica finalizada sem erro.')
        else:
            print('Analise Sintatica finalizada com erro. Programa finalizado')

'''
   def __consome(self, t):
        switch(r){
            case '{':
        }
        if t == self.__listaTokens[self.__i].getTipo():
            self.__i += 1
            return True
        else:
            print('Erro sintatico:\n    Token analisado:', self.__listaTokens[self.__i].getToken(),
                  '\n    Tipo esperado:', t)
            return False

    def __S(self):
        return self.__consome('{') and self.__A() and self.__consome('}')

    def __A(self):
        tipo = self.__listaTokens[i].getTipo()

        if tipo == 'int' or tipo == 'double' or tipo == 'float' or tipo == 'bool' or tipo == 'string':
            return True and self.__C(i + 1)
        if tipo == 'id':
            return True and self.__E(i + 1)
        if tipo == "if" or tipo == "while":
            return True and self.__I(i + 1)
        if tipo == '}':
            return True and self.__B(i + 1)
        print('Erro regra A:\n    Token analisado:', self.__listaTokens[i].getToken(), '\n    Tipo esperado: id, int, double, float, bool, string, if, while ou }\n    Encontrado:', tipo)
        return False
'''