from semantica.symbol import Symbol


class SymbolTable:
    def __init__(self, escopo_pai=None):
        self.simbolos = {}
        self.escopo_pai = escopo_pai
        self.proximo_deslocamento = 0

    def declarar(self, nome, tipo):
        if nome in self.simbolos:
            raise Exception(f'Erro semântico: variável "{nome}" já declarada neste escopo')

        deslocamento = self.proximo_deslocamento

        if tipo == "INTEGER":
            self.proximo_deslocamento += 2
        elif tipo == "BOOLEAN":
            self.proximo_deslocamento += 1
        elif tipo == "STRING":
            self.proximo_deslocamento += 1

        simbolo = Symbol(nome, tipo, deslocamento)
        self.simbolos[nome] = simbolo

        return simbolo

    def buscar(self, nome):
        if nome in self.simbolos:
            return self.simbolos[nome]

        if self.escopo_pai is not None:
            return self.escopo_pai.buscar(nome)

        return None

    def imprimir(self):
        for simbolo in self.simbolos.values():
            print(simbolo)