import re

class LimpaCodigo(object):

    __listaCodigo = []

    def __init__(self, lista):
        if len(lista) > 0:
            self.__listaCodigo = lista

    # função de checagem da linha do arquivo, que imprime as linhas de código válidas (removendo comentários, quebras de linha e espaços vazios)
    def treatList(self, newList):
        for i in self.__listaCodigo:
            linha = i
            if linha.__str__().__contains__("//"): #verifica se a linha contem comentarios
                linha = linha.__str__().rstrip(linha[int([b.start() for b in re.finditer("//", linha)][0])::])  # remocao de comentarios
            linha = linha.__str__().rstrip('\n') #remocao de quebra de linha a direita
            linha = linha.__str__().rstrip('\t') #remocao de caractere de tabulacao a direita
            linha = linha.__str__().rstrip('\r') #remocao de carriage return a direita
            linha = linha.__str__().rstrip('\f') #remocao de final de pagina a direita
            linha = linha.__str__().rstrip() #remocao de espacos vazios a direita
            linha = linha.__str__().lstrip()  #remocao de espacos vazios a esquerda
            if linha is not "": #despreza linha vazia
                newList.append(linha) #carrega linha na nova lista
        self.__listaCodigo = None