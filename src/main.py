#!/usr/bin/python
#-*- coding: utf-8 -*-
import platform

_system = None

if platform.sys.platform.__contains__("win"):
    _system = True
else:
    _system = False

       
if _system is True:
    from Arquivo import Arquivo
    from LimpaCodigo import LimpaCodigo
    from TabelaSimbolos import TabelaSimbolos
else:
    from src.Arquivo import Arquivo
    from src.LimpaCodigo import LimpaCodigo
    from src.TabelaSimbolos import TabelaSimbolos



arquivo = Arquivo("../tests/teste.xul") #cria objeto da classe Arquivo com o arquivo de teste desejado
listaArquivo = [] #lista que vai receber o conteudo do arquivo
arquivo.loadToList(listaArquivo) #carrega conteudo do arquivo para lista
trataLista = LimpaCodigo(listaArquivo) #cria objeto da classe LimpaCodigo com a lista a ser tratada
listaCodigo = [] #lista que vai recber o conteudo do arquivo tratado
trataLista.treatList(listaCodigo) #trata a lista antiga e carrega para uma nova lista

for idx, line in enumerate(listaCodigo):
    print('%.2d %s' % (idx, line))

lexema = TabelaSimbolos()

print (lexema.lexExists("}"))