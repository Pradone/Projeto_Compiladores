from antlr4 import *

from antlr.gramaticaLexer import gramaticaLexer
from antlr.gramaticaParser import gramaticaParser

from semantica.semantic_visitor import SemanticVisitor
from gerador_intermediario.code_generator import CodeGenerator
from gerador_otimizado.optimizer import Optimizer
from gerador_assembly.assembly_generator import AssemblyGenerator


VALIDACAO = True

ARQUIVO_VALIDO = "input/input_valido.txt"
ARQUIVO_INVALIDO = "input/input_invalido.txt"

SAIDA_INTERMEDIARIO_OTIMIZADO = "output/intermediario_otimizado.txt"


def analisar_sintaxe(caminho_arquivo):
    entrada = FileStream(caminho_arquivo, encoding="utf-8")

    lexer = gramaticaLexer(entrada)
    tokens = CommonTokenStream(lexer)

    parser = gramaticaParser(tokens)
    tree = parser.prog()

    return parser, tree


def executar_semantica(tree):
    visitor = SemanticVisitor()
    visitor.visit(tree)

    return visitor


def gerar_codigo_intermediario(tree):
    gerador = CodeGenerator()
    gerador.visit(tree)
    gerador.salvar()

    return gerador.codigo


def otimizar_codigo(codigo_intermediario):
    otimizador = Optimizer(codigo_intermediario)
    codigo_otimizado = otimizador.otimizar()

    with open(SAIDA_INTERMEDIARIO_OTIMIZADO, "w", encoding="utf-8") as arquivo:
        for linha in codigo_otimizado:
            arquivo.write(linha + "\n")

    return codigo_otimizado


def gerar_assembly(codigo_otimizado, tabela_simbolos):
    assembly = AssemblyGenerator(codigo_otimizado, tabela_simbolos)
    assembly.gerar()
    assembly.salvar()


def main():
    caminho_arquivo = ARQUIVO_VALIDO if VALIDACAO else ARQUIVO_INVALIDO

    print(f"Arquivo analisado: {caminho_arquivo}")

    parser, tree = analisar_sintaxe(caminho_arquivo)

    if parser.getNumberOfSyntaxErrors() > 0:
        print("\nPrograma inválido por erro sintático!")
        return

    try:
        visitor = executar_semantica(tree)

        print("\nTabela de símbolos:")
        visitor.tabela_global.imprimir()

        codigo_intermediario = gerar_codigo_intermediario(tree)

        codigo_otimizado = otimizar_codigo(codigo_intermediario)

        gerar_assembly(codigo_otimizado, visitor.tabela_global)

        print("\nCódigo intermediário gerado com sucesso!")
        print("Código intermediário otimizado gerado com sucesso!")
        print("Assembly gerado com sucesso!")
        print("\nPrograma válido!")

    except Exception as erro:
        print("\nPrograma inválido por erro semântico!")
        print(erro)


if __name__ == "__main__":
    main()