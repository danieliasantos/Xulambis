class Token(object):
    __lexema = ""
    __tipo = ""

    def __init__(self, lexema, tipo):
        self.__lexema = lexema
        self.__tipo = tipo