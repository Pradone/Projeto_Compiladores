from antlr.gramaticaVisitor import gramaticaVisitor
from semantica.symbol_table import SymbolTable


class SemanticVisitor(gramaticaVisitor):
    def __init__(self):
        self.tabela_global = SymbolTable()
        self.tabela = self.tabela_global

    def abrir_escopo(self):
        self.tabela = SymbolTable(self.tabela)

    def fechar_escopo(self):
        if self.tabela.escopo_pai is not None:
            self.tabela = self.tabela.escopo_pai

    def visitProg(self, ctx):
        return self.visitChildren(ctx)

    def visitDeclTip(self, ctx):
        tipo = ctx.tip().getText().upper()

        ids = ctx.listId().IDENTIFIER()

        for identificador in ids:
            nome = identificador.getText()

            if len(nome) > 16:
                nome = nome[:16]

            self.tabela.declarar(nome, tipo)

        return None

    def verificar_identificador(self, nome):
        simbolo = self.tabela.buscar(nome)

        if simbolo is None:
            raise Exception(f'Erro semântico: variável "{nome}" não declarada')

        return simbolo

    def visitCmdComp(self, ctx):
        self.abrir_escopo()
        self.visitChildren(ctx)
        self.fechar_escopo()

        return None

    def visitCmdAtrib(self, ctx):
        nome = ctx.IDENTIFIER().getText()
        simbolo = self.verificar_identificador(nome)

        tipo_expr = self.visit(ctx.expr())

        if simbolo.tipo != tipo_expr:
            raise Exception(
                f'Erro semântico: variável "{nome}" é {simbolo.tipo}, '
                f"mas recebeu {tipo_expr}"
            )

        return None

    def visitFator(self, ctx):
        if ctx.CTE() is not None:
            return "INTEGER"

        if ctx.CADEIA() is not None:
            return "STRING"

        if ctx.TRUE() is not None or ctx.FALSE() is not None:
            return "BOOLEAN"

        if ctx.IDENTIFIER() is not None:
            nome = ctx.IDENTIFIER().getText()
            simbolo = self.verificar_identificador(nome)
            return simbolo.tipo

        if ctx.OPNEG() is not None:
            tipo = self.visit(ctx.fator())

            if tipo != "BOOLEAN":
                raise Exception("Erro semântico: operador ~ exige BOOLEAN")

            return "BOOLEAN"

        if ctx.expr() is not None:
            return self.visit(ctx.expr())

        return None

    def visitCmdRead(self, ctx):
        ids = ctx.listId().IDENTIFIER()

        for identificador in ids:
            nome = identificador.getText()
            self.verificar_identificador(nome)

        return None

    def visitExpr(self, ctx):
        tipo = self.visit(ctx.exprRel(0))

        for i in range(1, len(ctx.exprRel())):
            tipo_direita = self.visit(ctx.exprRel(i))

            if tipo != "BOOLEAN" or tipo_direita != "BOOLEAN":
                raise Exception("Erro semântico: operadores AND/OR exigem BOOLEAN")

            tipo = "BOOLEAN"

        return tipo

    def visitExprRel(self, ctx):
        tipo_esquerda = self.visit(ctx.exprArit(0))

        if len(ctx.exprArit()) == 2:
            tipo_direita = self.visit(ctx.exprArit(1))

            if tipo_esquerda != tipo_direita:
                raise Exception(
                    "Erro semântico: operador relacional exige operandos do mesmo tipo"
                )

            return "BOOLEAN"
        return tipo_esquerda

    def visitExprArit(self, ctx):
        tipo = self.visit(ctx.termo(0))

        for i in range(1, len(ctx.termo())):
            tipo_direita = self.visit(ctx.termo(i))

            if tipo != "INTEGER" or tipo_direita != "INTEGER":
                raise Exception("Erro semântico: operadores + e - exigem INTEGER")

            tipo = "INTEGER"

        return tipo

    def visitTermo(self, ctx):
        tipo = self.visit(ctx.fator(0))

        for i in range(1, len(ctx.fator())):
            tipo_direita = self.visit(ctx.fator(i))

            if tipo != "INTEGER" or tipo_direita != "INTEGER":
                raise Exception("Erro semântico: operadores * e / exigem INTEGER")

            tipo = "INTEGER"

        return tipo

    def visitCmdWhile(self, ctx):
        tipo_condicao = self.visit(ctx.expr())

        if tipo_condicao != "BOOLEAN":
            raise Exception("Erro semântico: condição do WHILE deve ser BOOLEAN")

        return self.visit(ctx.cmd())

    def visitCmdIf(self, ctx):
        tipo_condicao = self.visit(ctx.expr())

        if tipo_condicao != "BOOLEAN":
            raise Exception("Erro semântico: condição do IF deve ser BOOLEAN")

        comandos = ctx.cmd()

        for comando in comandos:
            self.visit(comando)

        return None

    def visitCmdWrite(self, ctx):
        if ctx.CADEIA() is not None:
            return None

        return self.visit(ctx.expr())