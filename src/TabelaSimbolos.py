class TabelaSimbolos(object):
    __hashSymbols = {
        "{": "{",
        "}": "}",
        "(": "(",
        ")": ")",
        "[": "[",
        "]": "]",
        "id": str,
        ";": ";",
        "keyword": "keyword",
        "int": "int",
        "float": "float",
        "bool": "bool",
        "str": "str",
        "double": "double",
        "true": "true",
        "false": "false",
        "if": "if",
        "while": "while",
        "break": "break",
        "=": "=",
        "+": "+",
        "<": "<",
        ">": ">",
        ">=": ">=",
        "<=": "<=",
        "!=": "!=",
        "==": "=="
    }

    # palavras reservadas
    _words = []

    def verify_lex(self, line):

        # desmembramento dos tokens
        line_array = line.split() #isso deve ficar na classe de analise lexica

        # salvando os tokens na hash
        for x in line_array:

            if self._words.__contains__(x):
                print(x, ' - true')
                self.tabela._hash.append(x)
            else:
                print(x, ' - false')
                pass

    # visualização dos itens inseridos na hash
    def show_tabela(self):
        print(self.tabela._hash)

    # tabela.show_tabela()
