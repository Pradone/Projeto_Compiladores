class Token:

    def __init__(self, tipo, valor, linha, coluna):
        self.tipo = tipo
        self.valor = valor
        self.linha = linha
        self.coluna = coluna

    def __str__(self):
        return f"{self.tipo}: {self.valor} (Linha {self.linha}, Coluna {self.coluna})"
