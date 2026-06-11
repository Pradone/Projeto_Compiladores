class Symbol:
    def __init__(self, nome, tipo, deslocamento):
        self.nome = nome
        self.tipo = tipo
        self.deslocamento = deslocamento

    def __str__(self):
        return f"{self.nome} | tipo: {self.tipo} | deslocamento: {self.deslocamento}"