class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        self.consumir("PROGRAM")
        self.consumir("IDENTIFIER")
        self.consumir("PVIG")

        if self.token_atual() is not None and self.token_atual().tipo == "VAR":
            self.declaracao()

        self.bloco()

        self.consumir("PONTO")

        if self.token_atual() is not None:
            raise Exception("Erro sintático: tokens após fim do programa")

        print("Análise sintática concluída com sucesso")

    def token_atual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consumir(self, tipo_esperado):
        token = self.token_atual()

        if token is None:
            raise Exception("Fim inesperado do arquivo")

        if token.tipo != tipo_esperado:
            raise Exception(
                f"Erro sintático: esperado {tipo_esperado}, encontrado {token.tipo}"
            )

        self.pos += 1

    def declaracao(self):
        self.consumir("VAR")

        while self.token_atual() is not None and self.token_atual().tipo == "IDENTIFIER":
            self.lista_ids()
            self.consumir("DPONTOS")
            self.tipo()
            self.consumir("PVIG")

    def lista_ids(self):
        self.consumir("IDENTIFIER")

        while self.token_atual() is not None and self.token_atual().tipo == "VIG":
            self.consumir("VIG")
            self.consumir("IDENTIFIER")

    def tipo(self):
        token = self.token_atual()

        if token.tipo == "INTEGER":
            self.consumir("INTEGER")
        elif token.tipo == "BOOLEAN":
            self.consumir("BOOLEAN")
        else:
            raise Exception("Erro sintático: tipo inválido")

    def bloco(self):
        self.consumir("BEGIN")

        while self.token_atual() is not None and self.token_atual().tipo != "END":
            self.comando()

        self.consumir("END")

    def comando(self):
        token = self.token_atual()

        if token.tipo == "IDENTIFIER":
            self.atribuicao()
        elif token.tipo == "WRITE":
            self.write()
        elif token.tipo == "READ":
            self.read()
        elif token.tipo == "WHILE":
            self.while_loop()
        elif token.tipo == "IF":
            self.cmd_if()
        elif token.tipo == "BEGIN":
            self.bloco()
        else:
            raise Exception(f"Comando inválido: {token.tipo}")

    def atribuicao(self):
        self.consumir("IDENTIFIER")
        self.consumir("ATRIB")
        self.condicao()
        self.consumir("PVIG")

    def read(self):
        self.consumir("READ")
        self.consumir("ABPAR")
        self.lista_ids()
        self.consumir("FPAR")
        self.consumir("PVIG")

    def write(self):
        self.consumir("WRITE")
        self.consumir("ABPAR")

        token = self.token_atual()

        if token.tipo == "CADEIA":
            self.consumir("CADEIA")
        else:
            self.condicao()

        self.consumir("FPAR")
        self.consumir("PVIG")

    def while_loop(self):
        self.consumir("WHILE")
        self.condicao()
        self.consumir("DO")
        self.comando()

    def cmd_if(self):
        self.consumir("IF")
        self.condicao()
        self.consumir("THEN")
        self.comando()

        if self.token_atual() is not None and self.token_atual().tipo == "ELSE":
            self.consumir("ELSE")
            self.comando()

    def condicao(self):
        self.expr_relacional()

        while self.token_atual() is not None and self.token_atual().tipo == "OPLOG":
            self.consumir("OPLOG")
            self.expr_relacional()

    def expr_relacional(self):
        self.expr()

        if self.token_atual() is not None and self.token_atual().tipo == "OPREL":
            self.consumir("OPREL")
            self.expr()

    def expr(self):
        self.termo()

        while self.token_atual() is not None and self.token_atual().tipo == "OPAD":
            self.consumir("OPAD")
            self.termo()

    def termo(self):
        self.fator()

        while self.token_atual() is not None and self.token_atual().tipo == "OPMULT":
            self.consumir("OPMULT")
            self.fator()

    def fator(self):
        token = self.token_atual()

        if token.tipo == "CTE":
            self.consumir("CTE")
        elif token.tipo == "IDENTIFIER":
            self.consumir("IDENTIFIER")
        elif token.tipo in ["TRUE", "FALSE"]:
            self.consumir(token.tipo)
        elif token.tipo == "OPNEG":
            self.consumir("OPNEG")
            self.fator()
        elif token.tipo == "ABPAR":
            self.consumir("ABPAR")
            self.condicao()
            self.consumir("FPAR")
        else:
            raise Exception(
                "Erro sintático: esperado identificador, constante, booleano, negação ou parênteses"
            )