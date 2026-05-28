from lexer import Lexer

arquivo = open("tests/input_valido.txt", "r", encoding="utf-8")

codigo = arquivo.read()

lexer = Lexer(codigo)

tokens = lexer.tokenize()

for token in tokens:
    print(token)
