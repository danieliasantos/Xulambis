#!/usr/bin/python
#-*- coding: utf-8 -*-
from Arquivo import Arquivo
from LimpaCodigo import LimpaCodigo

lista = []

arquivo = Arquivo("teste.txt")

arquivo.loadToList(lista)

listaCodigo = LimpaCodigo(lista)

listaCodigo.treatCode()

listaCodigo.printCode()