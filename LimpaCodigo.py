import re

class LimpaCodigo(object):

    __listaCodigo = []

    def __init__(self, lista):
        if len(lista) > 0:
            self.checkLine(lista)

    def checkLine(self, lista):
        # função de checagem da linha do arquivo, que imprime as linhas de código válidas (removendo comentários, quebras de linha e espaços vazios)
        for linha in lista:
            if linha.__str__().__contains__("//"):
                s = linha.__str__().rstrip(linha[int([b.start() for b in re.finditer("//", linha)][0])::]) #remocao de comentarios
                s = linha.__str__().rstrip() #remocao de espacos vazios a direita
                s = s.lstrip() #remocao de espacos vazios a esquerda
                if s is not "":
                    self.__listaCodigo.append(s)
        return self.__listaCodigo

    def printCode(self):
        # função que enumera as linhas validas e as imprime na tela
        for idx, line in enumerate(self.__listaCodigo):
            print( '%.2d %s' % (idx, line))