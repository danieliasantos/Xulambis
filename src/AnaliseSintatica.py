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
    __final = []
    _iterator = 0

    def __init__(self, lista):
        if len(lista) > 0:
            self.__listaTokens = lista

    def analisaTokens(self):
        tokens = TabelaSimbolos()

    def checkRule(self, lista):
        self.s(lista)
           
    def analisys(self):
        self.s(self.__listaTokens)

    def s(self, lista):
        print (lista[self._iterator].getTipo())
        if lista[self._iterator].getTipo() is '{':
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.a(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + " Rule S")
        
    def a(self, lista):
        context = lista[self._iterator].getTipo()
        print (context)
        if context is "id":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.e(self.__listaTokens)

        elif context is 'int' or context is 'double' or context is 'float' or context is'bool' or context is'string':
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.c(self.__listaTokens)

        elif context is '}':
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.b(self.__listaTokens)
        elif context is "while" or context is "if":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.i(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + "Rule A")

    def b(self, lista):
        print (lista[self._iterator].getTipo())
        if lista[self._iterator].getTipo() is "":
            print("LAMBDA REGRA B")
        elif lista[self._iterator].getTipo() is "}":
            self.__final.append(lista[self._iterator])
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + " Rule B")

    def c(self, lista):
        print (lista[self._iterator].getTipo())
        if lista[self._iterator].getTipo() is "id":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.e(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + " Rule C")

    def d(self, lista):
        print (lista[self._iterator].getTipo())
        if lista[self._iterator].getTipo() is ";":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.a(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + "Rule D")
            
    def e(self, lista):
        print (lista[self._iterator].getTipo())
        if lista[self._iterator].getTipo() is "=":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.g(self.__listaTokens)
        elif lista[self._iterator].getTipo() is ";":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.a(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + "Rule E")
    
    def f(self, lista):
        print (lista[self._iterator].getTipo())
        if lista[self._iterator].getTipo() is ")":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.l(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + "Rule F")
 
    def g(self, lista):
        context = lista[self._iterator].getTipo()
        print (lista[self._iterator].getTipo())
        if context is "number" or context is"id" or context is "false" or context is "true":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.h(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + "Rule G")

    def h(self, lista):

        context = lista[self._iterator].getTipo()
        print (lista[self._iterator].getTipo())
        if lista[self._iterator].getTipo() is ";":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.a(self.__listaTokens)
        elif context is "/" or context is "*" or context is "-" or context is "+":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.g(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + "Rule H")
        
    def i(self, lista):
        print (lista[self._iterator].getTipo())
        if lista[self._iterator].getTipo() is "(":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.j(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + "Rule I")

    def j(self, lista):
        print (lista[self._iterator].getTipo())
        if lista[self._iterator].getTipo() is "id":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.m(self.__listaTokens)
        elif lista[self._iterator].getTipo() is "true":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.f(self.__listaTokens)
        elif lista[self._iterator].getTipo() is "false":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.f(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + "Rule j")

    def k(self, lista):
        print (lista[self._iterator].getTipo())
        if lista[self._iterator].getTipo() is "id":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.f(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + "Rule K")

    def l(self, lista):
        print (lista[self._iterator].getTipo())
        if lista[self._iterator].getTipo() is "break":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.d(self.__listaTokens)
        elif lista[self._iterator].getTipo() is "{":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.a(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + "Rule L")

    def m(self, lista):

        context = lista[self._iterator].getTipo()
        print (lista[self._iterator].getTipo())
        if context is "&&" or  context is "||" or context is ">" or context is ">=" or context is"<" or context is "!=" or context is"==" or context is "!" or context is"<=" or context is ">":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.k(self.__listaTokens)
        elif lista[self._iterator].getTipo() is ")":
            self.__final.append(lista[self._iterator])
            self._iterator+=1
            self.l(self.__listaTokens)
        else:
            print("SINTATYC ERROR " + lista[self._iterator].getTipo() + "Rule M")