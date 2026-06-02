from antlr4 import *

from antlr.gramaticaLexer import gramaticaLexer
from antlr.gramaticaParser import gramaticaParser

# Altere para False para testar um programa inválido
validacao = True
#validacao = False

arquivo = "input/input_valido.txt" if validacao else "input/input_invalido.txt"

entrada = FileStream(arquivo, encoding="utf-8")

lexer = gramaticaLexer(entrada)
tokens = CommonTokenStream(lexer)

parser = gramaticaParser(tokens)

parser.prog()

if parser.getNumberOfSyntaxErrors() == 0:
    print(f"\nArquivo analisado: {arquivo}")
    print("Programa válido!")
else:
    print(f"\nArquivo analisado: {arquivo}")
    print("Programa inválido!")
