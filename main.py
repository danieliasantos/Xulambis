#!/usr/bin/python
#-*- coding: utf-8 -*-
from Arquivo import Arquivo

arquivo = Arquivo("teste.xul")

arquivo.loadFile()

arquivo.treatCode()

arquivo.printCode()
