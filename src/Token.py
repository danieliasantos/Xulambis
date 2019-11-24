class Token(object):
    __lexema = ""
    __tipo = ""

    def __init__(self, lexema, tipo):
        self.__lexema = lexema
        self.__tipo = tipo

    def getToken(self):
        return "< " + self.__lexema + " , " + self.__tipo + " >"


    def getTipo(self):
        return self.__tipo

    def getLexema(self):
        return self.__lexema