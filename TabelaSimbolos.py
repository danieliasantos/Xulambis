class TabelaSimbolos(object):
    _hash = []

    # palavras reservadas
    _words = ['{', '}', ':', ';', 'int', 'float', 'bool', '+', '-', '*', '/', '<', '>', '(', ')', 'while', 'if', '=']

    def verify_lex(self, line):

        # desmembramento dos tokens
        line_array = line.split()

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
