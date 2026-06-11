from antlr.gramaticaVisitor import gramaticaVisitor


class CodeGenerator(gramaticaVisitor):

    def __init__(self):
        self.codigo = []
        self.temp_count = 0
        self.label_count = 0

    def novo_temp(self):
        temp = f"t_{self.temp_count}"
        self.temp_count += 1
        return temp

    def novo_label(self):
        label = f"L_{self.label_count}"
        self.label_count += 1
        return label

    def emitir(self, instrucao):
        self.codigo.append(instrucao)

    def salvar(self, caminho="output/intermediario.txt"):
        with open(caminho, "w", encoding="utf-8") as arquivo:
            for linha in self.codigo:
                arquivo.write(linha + "\n")

    def visitCmdAtrib(self, ctx):
        nome = ctx.IDENTIFIER().getText()
        valor = self.visit(ctx.expr())

        self.emitir(f"{nome} = {valor}")

        return None

    def visitExpr(self, ctx):
        resultado = self.visit(ctx.exprRel(0))

        for i in range(1, len(ctx.exprRel())):
            direita = self.visit(ctx.exprRel(i))
            operador = ctx.OPLOG(i - 1).getText()

            temp = self.novo_temp()
            self.emitir(f"{temp} = {resultado} {operador} {direita}")
            resultado = temp

        return resultado

    def visitExprRel(self, ctx):
        esquerda = self.visit(ctx.exprArit(0))

        if len(ctx.exprArit()) == 2:
            direita = self.visit(ctx.exprArit(1))
            operador = ctx.OPREL().getText()

            temp = self.novo_temp()
            self.emitir(f"{temp} = {esquerda} {operador} {direita}")

            return temp

        return esquerda

    def visitExprArit(self, ctx):
        resultado = self.visit(ctx.termo(0))

        for i in range(1, len(ctx.termo())):
            direita = self.visit(ctx.termo(i))
            operador = ctx.OPAD(i - 1).getText()

            temp = self.novo_temp()
            self.emitir(f"{temp} = {resultado} {operador} {direita}")
            resultado = temp

        return resultado

    def visitTermo(self, ctx):
        resultado = self.visit(ctx.fator(0))

        for i in range(1, len(ctx.fator())):
            direita = self.visit(ctx.fator(i))
            operador = ctx.OPMULT(i - 1).getText()

            temp = self.novo_temp()
            self.emitir(f"{temp} = {resultado} {operador} {direita}")
            resultado = temp

        return resultado

    def visitFator(self, ctx):
        if ctx.CTE() is not None:
            return ctx.CTE().getText()

        if ctx.CADEIA() is not None:
            return ctx.CADEIA().getText()

        if ctx.TRUE() is not None:
            return "TRUE"

        if ctx.FALSE() is not None:
            return "FALSE"

        if ctx.IDENTIFIER() is not None:
            return ctx.IDENTIFIER().getText()

        if ctx.OPNEG() is not None:
            valor = self.visit(ctx.fator())

            temp = self.novo_temp()
            self.emitir(f"{temp} = ~ {valor}")

            return temp

        if ctx.expr() is not None:
            return self.visit(ctx.expr())

        return None

    def visitCmdWhile(self, ctx):
        inicio = self.novo_label()
        fim = self.novo_label()
        self.emitir(f"{inicio}:")

        condicao = self.visit(ctx.expr())

        self.emitir(f"IF_FALSE {condicao} GOTO {fim}")
        self.visit(ctx.cmd())
        self.emitir(f"GOTO {inicio}")
        self.emitir(f"{fim}:")

        return None

    def visitCmdWrite(self, ctx):

        if ctx.CADEIA() is not None:
            self.emitir(f"WRITE {ctx.CADEIA().getText()}")
        else:
            valor = self.visit(ctx.expr())
            self.emitir(f"WRITE {valor}")

        return None
    
    def visitCmdRead(self, ctx):
        ids = ctx.listId().IDENTIFIER()

        for identificador in ids:
            self.emitir(f"READ {identificador.getText()}")

        return None
    
    def visitCmdIf(self, ctx):
        label_else = self.novo_label()
        label_fim = self.novo_label()

        condicao = self.visit(ctx.expr())
        self.emitir(f"IF_FALSE {condicao} GOTO {label_else}")

        comandos = ctx.cmd()
        self.visit(comandos[0])

        if len(comandos) > 1:
            self.emitir(f"GOTO {label_fim}")
            self.emitir(f"{label_else}:")
            self.visit(comandos[1])
            self.emitir(f"{label_fim}:")
        else:
            self.emitir(f"{label_else}:")

        return None