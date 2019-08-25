import re
class Arquivo(object):
    # Classe de leitura de arquivo de codigo, e criacao de uma lista de strings com o conteudo do arquivo

    __nome = None
    __lista = []

    def __init__(self, nome):
        # construtor da classe. inicializa o arquivo a ser testado, e executa funcao de carregamento do arquivo para uma lista
        if nome is not None:
            self.__nome = nome

    def loadFile(self):
        # função de carregamento do arquivo para lista
        with open(self.__nome, "r") as file:
            for line in file:
                self.__lista.append(line)

    def checkLine(self):
        # função de checagem da linha do arquivo, que imprime as linhas de código válidas (removendo comentários, quebras de linha e espaços vazios)
        for linha in self.__lista:
            if linha.__str__().startswith("\n"):
                self.__lista.remove( linha )
            elif "//" in linha:
                s = linha.__str__().rstrip(linha[int([b.start() for b in re.finditer("//", linha)][0])::])
                self.__lista.insert( self.__lista.index( linha ), s )
                self.__lista.remove( linha )

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
            self.__lista.insert( self.__lista.index( linha ), s )
            self.__lista.remove( linha )

    def treatCode(self):
        self.checkLine()
        self.cleanList()
        self.removeSpaces()

    def printCode(self):
        # função que enumera as linhas validas e as imprime na tela
        for idx, line in enumerate(self.__lista):
            print( '%.2d %s' % (idx, line))