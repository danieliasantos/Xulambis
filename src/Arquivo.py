class Arquivo(object):
    # Classe de leitura de arquivo de codigo, e criacao de uma lista de strings com o conteudo do arquivo

    __nome = None

    def __init__(self, nome):
        # construtor da classe. inicializa o arquivo a ser testado, e executa funcao de carregamento do arquivo para uma lista
        if nome is not None:
            self.__nome = nome

    def loadToList(self, lista):
        # função de carregamento do arquivo para lista
        with open(self.__nome, "r") as file:
            for line in file:
                lista.append(line)