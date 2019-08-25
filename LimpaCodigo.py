import re

class LimpaCodigo(object):

    __lista = []

    def __init__(self, lista):
        if len(lista) > 0:
            self.__lista = lista

    def checkLine(self):
        # função de checagem da linha do arquivo, que imprime as linhas de código válidas (removendo comentários, quebras de linha e espaços vazios)
        for linha in self.__lista:
            if linha.__str__().startswith("\n"):
                self.__lista.remove(linha)
            elif "//" in linha:
                s = linha.__str__().rstrip(linha[int([b.start() for b in re.finditer("//", linha)][0])::])
                self.__lista.insert(self.__lista.index(linha), s)
                self.__lista.remove(linha)

    def cleanList(self):
        #funcao que remove linhas vazias
        for linha in self.__lista:
            e = 0
            for l in linha:
                if l is not "":
                    e = 1
                    break
            if not e:
                self.__lista.remove(linha)

    def removeSpaces(self):
        #funcao que remove espacos duplicados
        for linha in self.__lista:
            s = linha.__str__().rstrip()
            s = s.lstrip()
            self.__lista.insert(self.__lista.index(linha), s)
            self.__lista.remove(linha)

    def treatCode(self):
        self.checkLine()
        self.cleanList()
        self.removeSpaces()

    def printCode(self):
        # função que enumera as linhas validas e as imprime na tela
        for idx, line in enumerate(self.__lista):
            print( '%.2d %s' % (idx, line))

