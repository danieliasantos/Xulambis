#!/usr/bin/python
#-*- coding: utf-8 -*-
import platform

_system = None

if platform.sys.platform.__contains__("linux"):
    _system = False
else:
    _system = True

if _system is True:
    from Arquivo import Arquivo
    from LimpaCodigo import LimpaCodigo
    from AnaliseLexica import AnaliseLexica
    from AnaliseSintatica import AnaliseSintatica
    from AnaliseSemantica import AnaliseSemantica
else:
    from src.Arquivo import Arquivo
    from src.LimpaCodigo import LimpaCodigo
    from src.AnaliseLexica import AnaliseLexica
    from src.AnaliseSintatica import AnaliseSintatica
    from src.AnaliseSemantica import AnaliseSemantica

arquivo = Arquivo("../tests/teste.xul") #cria objeto da classe Arquivo com o arquivo de teste desejado
listaArquivo = [] #lista que vai receber o conteudo do arquivo
arquivo.carregaLista(listaArquivo) #carrega conteudo do arquivo para lista

limpaCodigo = LimpaCodigo(listaArquivo) #cria objeto da classe LimpaCodigo com a lista a ser tratada
listaCodigo = [] #lista que vai recber o conteudo do arquivo tratado
limpaCodigo.limpezaCodigo(listaCodigo) #trata a lista antiga e carrega para uma nova lista

'''
print('Processo de limpeza de codigo: \n')
for idx, line in enumerate(listaCodigo):
    print('%.2d %s' % (idx, line))
'''

print('\nProcesso de analise lexica:')
analiseLexica = AnaliseLexica(listaCodigo)
listaTokens = []
analiseLexica.analisaTokens(listaTokens)
'''
for idx, line in enumerate(listaTokens):
    print(line.getToken(), idx)
    #print('%.2d %s' % (idx, line.getToken()))
'''
print('\nProcesso de analise sintatica:')
analiseSintatica = AnaliseSintatica(listaTokens)
analiseSintatica.analisaTokens()

print('\nProcesso de analise semantica:')
analiseSemantica = AnaliseSemantica(listaTokens)
analiseSintatica.analisaTokens()