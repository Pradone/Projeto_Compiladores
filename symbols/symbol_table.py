class SymbolTable:

    def __init__(self):
        self.symbols = {}

    def add(self, nome, tipo):
        if nome in self.symbols:
            raise Exception(
                f'Erro semântico: variável "{nome}" já declarada'
            )
        self.symbols[nome] = tipo

    def exists(self, nome):
        return nome in self.symbols