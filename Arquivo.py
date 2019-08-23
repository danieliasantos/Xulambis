class Arquivo(object):

    def imprimir(self):
        with open("teste.txt", "r") as file:
            for line in file:
             self.checkLine(line)


    def checkLine(linha):
        if not linha.__str__().startswith("/n") and not linha.__str__().startswith("//"):
          if linha.__str__().find("//"):
            x = linha.__str__().split("//")
            print(x[0])