from src.Token import Token

class TabelaSimbolos(object):
    __hashSymbols = {
        "int": Token("int", "int"),
        "float": Token("float", "float"),
        "bool": Token("bool", "bool"),
        "double": Token("double", "double"),
        "true",
        "false",
        "if",
        "while",
        "break",
        "{",
        "}",
        "(",
        ")",
        "[",
        "]",
        ";",
        "=",
        "+",
        "<",
        ">",
        ">=",
        "<=",
        "!=": Token(),
        "==": Token("==", "==")
    }
    def lexExists (self, lexema):
        return lexema in self.__hashSymbols

    def getToken(self, lexema):
        return self.__hashSymbols[lexema]