from lexer.token import Token
from lexer.rules import RESERVADAS, SIMBOLOS, OPERADORES_COMPOSTOS, OPERADORES_SIMPLES


class Lexer:

    def __init__(self, codigo):
        self.codigo = codigo
        self.pos = 0
        self.linha = 1
        self.coluna = 1

    def tokenize(self):

        tokens = []

        while self.pos < len(self.codigo):

            atual = self.codigo[self.pos]

            # IGNORAR VAZIO
            if atual in [" ", "\t"]:
                self.avancar()
                continue

            # BREAK
            if atual == "\n":
                self.linha += 1
                self.coluna = 1
                self.pos += 1
                continue

            # COMENTARIOS
            if atual == "/":
                proxima_barra = self.codigo.find("/", self.pos + 1)

                if proxima_barra != -1:
                    while self.pos <= proxima_barra:
                        
                        if self.codigo[self.pos] == "\n":
                            self.linha += 1
                            self.coluna = 1
                            self.pos += 1
                        else:
                            self.avancar()
                    continue

            # STRINGS
            if atual == '"':

                coluna_inicio = self.coluna + 1

                self.avancar()

                inicio = self.pos

                while self.pos < len(self.codigo) and self.codigo[self.pos] != '"':

                    if self.codigo[self.pos] == "\n":
                        raise Exception(f"String não fechada na linha {self.linha}")

                    self.avancar()

                if self.pos >= len(self.codigo):
                    raise Exception(f"String não fechada na linha {self.linha}")

                texto = self.codigo[inicio : self.pos]

                tokens.append(Token("CADEIA", texto, self.linha, coluna_inicio))

                self.avancar()

                continue

            # IDENTIFICADORES (RESERVADAS)
            if atual.isalpha():

                inicio = self.pos
                coluna_inicio = self.coluna

                while self.pos < len(self.codigo) and self.codigo[self.pos].isalnum():
                    self.avancar()

                palavra = self.codigo[inicio : self.pos]
                if len(palavra) > 16:
                    palavra = palavra[:16]

                if palavra.upper() in ["AND", "OR"]:
                    tokens.append(
                        Token("OPLOG", palavra.upper(), self.linha, coluna_inicio)
                    )
                elif palavra.upper() in RESERVADAS:

                    tokens.append(
                        Token(palavra.upper(), palavra, self.linha, coluna_inicio)
                    )
                else:
                    tokens.append(
                        Token("IDENTIFIER", palavra, self.linha, coluna_inicio)
                    )

                continue

            # NUMEROS
            if atual.isdigit():

                inicio = self.pos
                coluna_inicio = self.coluna

                while self.pos < len(self.codigo) and self.codigo[self.pos].isdigit():
                    self.avancar()

                numero = self.codigo[inicio : self.pos]

                valor = int(numero)

                if valor < -32768 or valor > 32767:
                    raise Exception(
                        f"Erro léxico: inteiro fora do limite "
                        f"na linha {self.linha}, coluna {coluna_inicio}"
                    )

                tokens.append(Token("CTE", numero, self.linha, coluna_inicio))

                continue

            # OPERADORES_COMPOSTOS
            if self.pos + 1 < len(self.codigo):

                dois_chars = self.codigo[self.pos : self.pos + 2]

                if dois_chars in OPERADORES_COMPOSTOS:

                    tipo, atributo = OPERADORES_COMPOSTOS[dois_chars]

                    tokens.append(Token(tipo, dois_chars, self.linha, self.coluna))

                    self.avancar()
                    self.avancar()

                    continue

            # OPERADORES_SIMPLES
            if atual in OPERADORES_SIMPLES:

                tipo, atributo = OPERADORES_SIMPLES[atual]

                tokens.append(Token(tipo, atual, self.linha, self.coluna))

                self.avancar()

                continue

            # SIMBOLOS
            if atual in SIMBOLOS:

                tokens.append(Token(SIMBOLOS[atual], atual, self.linha, self.coluna))

                self.avancar()
                continue

            # ERRO LEXER
            raise Exception(
                f"Erro léxico: token inválido '{atual}' "
                f"na linha {self.linha}, coluna {self.coluna}"
            )

        return tokens

    def avancar(self):
        self.pos += 1
        self.coluna += 1
