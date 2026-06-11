# Generated from antlr/gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#prog.
    def visitProg(self, ctx:gramaticaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#decls.
    def visitDecls(self, ctx:gramaticaParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#listDecl.
    def visitListDecl(self, ctx:gramaticaParser.ListDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#declTip.
    def visitDeclTip(self, ctx:gramaticaParser.DeclTipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#listId.
    def visitListId(self, ctx:gramaticaParser.ListIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#tip.
    def visitTip(self, ctx:gramaticaParser.TipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#cmdComp.
    def visitCmdComp(self, ctx:gramaticaParser.CmdCompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#listCmd.
    def visitListCmd(self, ctx:gramaticaParser.ListCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#cmd.
    def visitCmd(self, ctx:gramaticaParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#cmdIf.
    def visitCmdIf(self, ctx:gramaticaParser.CmdIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#cmdWhile.
    def visitCmdWhile(self, ctx:gramaticaParser.CmdWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#cmdRead.
    def visitCmdRead(self, ctx:gramaticaParser.CmdReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#cmdWrite.
    def visitCmdWrite(self, ctx:gramaticaParser.CmdWriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#cmdAtrib.
    def visitCmdAtrib(self, ctx:gramaticaParser.CmdAtribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#expr.
    def visitExpr(self, ctx:gramaticaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#exprRel.
    def visitExprRel(self, ctx:gramaticaParser.ExprRelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#exprArit.
    def visitExprArit(self, ctx:gramaticaParser.ExprAritContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#termo.
    def visitTermo(self, ctx:gramaticaParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#fator.
    def visitFator(self, ctx:gramaticaParser.FatorContext):
        return self.visitChildren(ctx)



del gramaticaParser