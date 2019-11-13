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
    from AnaliseLexica import AnaliseLexica
else:
    from src.Arquivo import Arquivo
    from src.LimpaCodigo import LimpaCodigo
    from src.AnaliseLexica import AnaliseLexica



arquivo = Arquivo("../tests/teste.xul") #cria objeto da classe Arquivo com o arquivo de teste desejado
listaArquivo = [] #lista que vai receber o conteudo do arquivo
arquivo.carregaLista(listaArquivo) #carrega conteudo do arquivo para lista

limpaCodigo = LimpaCodigo(listaArquivo) #cria objeto da classe LimpaCodigo com a lista a ser tratada
listaCodigo = [] #lista que vai recber o conteudo do arquivo tratado
limpaCodigo.limpezaCodigo(listaCodigo) #trata a lista antiga e carrega para uma nova lista

#for idx, line in enumerate(listaCodigo):
#    print('%.2d %s' % (idx, line))

analiseLexica = AnaliseLexica(listaCodigo)
listaTokens = []
analiseLexica.analisaTokens(listaTokens)

for idx, line in enumerate(listaTokens):
    print('%.2d %s' % (idx, line.getToken()))