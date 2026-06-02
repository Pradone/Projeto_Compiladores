# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#prog.
    def enterProg(self, ctx:gramaticaParser.ProgContext):
        pass

    # Exit a parse tree produced by gramaticaParser#prog.
    def exitProg(self, ctx:gramaticaParser.ProgContext):
        pass


    # Enter a parse tree produced by gramaticaParser#decls.
    def enterDecls(self, ctx:gramaticaParser.DeclsContext):
        pass

    # Exit a parse tree produced by gramaticaParser#decls.
    def exitDecls(self, ctx:gramaticaParser.DeclsContext):
        pass


    # Enter a parse tree produced by gramaticaParser#listDecl.
    def enterListDecl(self, ctx:gramaticaParser.ListDeclContext):
        pass

    # Exit a parse tree produced by gramaticaParser#listDecl.
    def exitListDecl(self, ctx:gramaticaParser.ListDeclContext):
        pass


    # Enter a parse tree produced by gramaticaParser#declTip.
    def enterDeclTip(self, ctx:gramaticaParser.DeclTipContext):
        pass

    # Exit a parse tree produced by gramaticaParser#declTip.
    def exitDeclTip(self, ctx:gramaticaParser.DeclTipContext):
        pass


    # Enter a parse tree produced by gramaticaParser#listId.
    def enterListId(self, ctx:gramaticaParser.ListIdContext):
        pass

    # Exit a parse tree produced by gramaticaParser#listId.
    def exitListId(self, ctx:gramaticaParser.ListIdContext):
        pass


    # Enter a parse tree produced by gramaticaParser#tip.
    def enterTip(self, ctx:gramaticaParser.TipContext):
        pass

    # Exit a parse tree produced by gramaticaParser#tip.
    def exitTip(self, ctx:gramaticaParser.TipContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdComp.
    def enterCmdComp(self, ctx:gramaticaParser.CmdCompContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdComp.
    def exitCmdComp(self, ctx:gramaticaParser.CmdCompContext):
        pass


    # Enter a parse tree produced by gramaticaParser#listCmd.
    def enterListCmd(self, ctx:gramaticaParser.ListCmdContext):
        pass

    # Exit a parse tree produced by gramaticaParser#listCmd.
    def exitListCmd(self, ctx:gramaticaParser.ListCmdContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmd.
    def enterCmd(self, ctx:gramaticaParser.CmdContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmd.
    def exitCmd(self, ctx:gramaticaParser.CmdContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdIf.
    def enterCmdIf(self, ctx:gramaticaParser.CmdIfContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdIf.
    def exitCmdIf(self, ctx:gramaticaParser.CmdIfContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdWhile.
    def enterCmdWhile(self, ctx:gramaticaParser.CmdWhileContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdWhile.
    def exitCmdWhile(self, ctx:gramaticaParser.CmdWhileContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdRead.
    def enterCmdRead(self, ctx:gramaticaParser.CmdReadContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdRead.
    def exitCmdRead(self, ctx:gramaticaParser.CmdReadContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdWrite.
    def enterCmdWrite(self, ctx:gramaticaParser.CmdWriteContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdWrite.
    def exitCmdWrite(self, ctx:gramaticaParser.CmdWriteContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdAtrib.
    def enterCmdAtrib(self, ctx:gramaticaParser.CmdAtribContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdAtrib.
    def exitCmdAtrib(self, ctx:gramaticaParser.CmdAtribContext):
        pass


    # Enter a parse tree produced by gramaticaParser#expr.
    def enterExpr(self, ctx:gramaticaParser.ExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expr.
    def exitExpr(self, ctx:gramaticaParser.ExprContext):
        pass


    # Enter a parse tree produced by gramaticaParser#exprRel.
    def enterExprRel(self, ctx:gramaticaParser.ExprRelContext):
        pass

    # Exit a parse tree produced by gramaticaParser#exprRel.
    def exitExprRel(self, ctx:gramaticaParser.ExprRelContext):
        pass


    # Enter a parse tree produced by gramaticaParser#exprArit.
    def enterExprArit(self, ctx:gramaticaParser.ExprAritContext):
        pass

    # Exit a parse tree produced by gramaticaParser#exprArit.
    def exitExprArit(self, ctx:gramaticaParser.ExprAritContext):
        pass


    # Enter a parse tree produced by gramaticaParser#termo.
    def enterTermo(self, ctx:gramaticaParser.TermoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#termo.
    def exitTermo(self, ctx:gramaticaParser.TermoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#fator.
    def enterFator(self, ctx:gramaticaParser.FatorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#fator.
    def exitFator(self, ctx:gramaticaParser.FatorContext):
        pass



del gramaticaParser