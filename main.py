from antlr4 import *

from antlr.gramaticaLexer import gramaticaLexer
from antlr.gramaticaParser import gramaticaParser
from semantica.semantic_visitor import SemanticVisitor

# Altere para False para testar um programa inválido
validacao = True
validacao = False

arquivo = "input/input_valido.txt" if validacao else "input/input_invalido.txt"

entrada = FileStream(arquivo, encoding="utf-8")

lexer = gramaticaLexer(entrada)
tokens = CommonTokenStream(lexer)

parser = gramaticaParser(tokens)

tree = parser.prog()

try:
    visitor = SemanticVisitor()
    visitor.visit(tree)

    print("\nTabela de símbolos:")
    visitor.tabela_global.imprimir()

    print("\nPrograma válido!")

except Exception as erro:
    print("\nPrograma inválido!")
    print(erro)

# if parser.getNumberOfSyntaxErrors() == 0:
#     print(f"\nArquivo analisado: {arquivo}")
# else:
#     print(f"\nArquivo analisado: {arquivo}")
