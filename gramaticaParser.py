# Generated from gramatica.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,164,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,50,8,1,1,2,4,2,53,8,2,11,2,12,
        2,54,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,65,8,4,10,4,12,4,68,9,4,
        1,5,1,5,1,6,1,6,1,6,1,6,1,7,5,7,77,8,7,10,7,12,7,80,9,7,1,8,1,8,
        1,8,1,8,1,8,1,8,3,8,88,8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,96,8,9,1,
        10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,
        12,1,12,3,12,113,8,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,
        14,1,14,1,14,5,14,126,8,14,10,14,12,14,129,9,14,1,15,1,15,1,15,3,
        15,134,8,15,1,16,1,16,1,16,5,16,139,8,16,10,16,12,16,142,9,16,1,
        17,1,17,1,17,5,17,147,8,17,10,17,12,17,150,9,17,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,162,8,18,1,18,0,0,19,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,1,1,0,2,3,164,0,
        38,1,0,0,0,2,49,1,0,0,0,4,52,1,0,0,0,6,56,1,0,0,0,8,61,1,0,0,0,10,
        69,1,0,0,0,12,71,1,0,0,0,14,78,1,0,0,0,16,87,1,0,0,0,18,89,1,0,0,
        0,20,97,1,0,0,0,22,102,1,0,0,0,24,108,1,0,0,0,26,117,1,0,0,0,28,
        122,1,0,0,0,30,130,1,0,0,0,32,135,1,0,0,0,34,143,1,0,0,0,36,161,
        1,0,0,0,38,39,5,1,0,0,39,40,5,30,0,0,40,41,5,21,0,0,41,42,3,2,1,
        0,42,43,3,12,6,0,43,44,5,22,0,0,44,45,5,0,0,1,45,1,1,0,0,0,46,47,
        5,9,0,0,47,50,3,4,2,0,48,50,1,0,0,0,49,46,1,0,0,0,49,48,1,0,0,0,
        50,3,1,0,0,0,51,53,3,6,3,0,52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,
        0,0,54,55,1,0,0,0,55,5,1,0,0,0,56,57,3,8,4,0,57,58,5,23,0,0,58,59,
        3,10,5,0,59,60,5,21,0,0,60,7,1,0,0,0,61,66,5,30,0,0,62,63,5,24,0,
        0,63,65,5,30,0,0,64,62,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,
        1,0,0,0,67,9,1,0,0,0,68,66,1,0,0,0,69,70,7,0,0,0,70,11,1,0,0,0,71,
        72,5,4,0,0,72,73,3,14,7,0,73,74,5,5,0,0,74,13,1,0,0,0,75,77,3,16,
        8,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,15,
        1,0,0,0,80,78,1,0,0,0,81,88,3,18,9,0,82,88,3,20,10,0,83,88,3,22,
        11,0,84,88,3,24,12,0,85,88,3,26,13,0,86,88,3,12,6,0,87,81,1,0,0,
        0,87,82,1,0,0,0,87,83,1,0,0,0,87,84,1,0,0,0,87,85,1,0,0,0,87,86,
        1,0,0,0,88,17,1,0,0,0,89,90,5,13,0,0,90,91,3,28,14,0,91,92,5,14,
        0,0,92,95,3,16,8,0,93,94,5,15,0,0,94,96,3,16,8,0,95,93,1,0,0,0,95,
        96,1,0,0,0,96,19,1,0,0,0,97,98,5,6,0,0,98,99,3,28,14,0,99,100,5,
        7,0,0,100,101,3,16,8,0,101,21,1,0,0,0,102,103,5,8,0,0,103,104,5,
        25,0,0,104,105,3,8,4,0,105,106,5,26,0,0,106,107,5,21,0,0,107,23,
        1,0,0,0,108,109,5,12,0,0,109,112,5,25,0,0,110,113,3,28,14,0,111,
        113,5,29,0,0,112,110,1,0,0,0,112,111,1,0,0,0,113,114,1,0,0,0,114,
        115,5,26,0,0,115,116,5,21,0,0,116,25,1,0,0,0,117,118,5,30,0,0,118,
        119,5,27,0,0,119,120,3,28,14,0,120,121,5,21,0,0,121,27,1,0,0,0,122,
        127,3,30,15,0,123,124,5,19,0,0,124,126,3,30,15,0,125,123,1,0,0,0,
        126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,29,1,0,0,0,129,
        127,1,0,0,0,130,133,3,32,16,0,131,132,5,16,0,0,132,134,3,32,16,0,
        133,131,1,0,0,0,133,134,1,0,0,0,134,31,1,0,0,0,135,140,3,34,17,0,
        136,137,5,17,0,0,137,139,3,34,17,0,138,136,1,0,0,0,139,142,1,0,0,
        0,140,138,1,0,0,0,140,141,1,0,0,0,141,33,1,0,0,0,142,140,1,0,0,0,
        143,148,3,36,18,0,144,145,5,18,0,0,145,147,3,36,18,0,146,144,1,0,
        0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,35,1,0,0,
        0,150,148,1,0,0,0,151,162,5,30,0,0,152,162,5,28,0,0,153,162,5,11,
        0,0,154,162,5,10,0,0,155,156,5,20,0,0,156,162,3,36,18,0,157,158,
        5,25,0,0,158,159,3,28,14,0,159,160,5,26,0,0,160,162,1,0,0,0,161,
        151,1,0,0,0,161,152,1,0,0,0,161,153,1,0,0,0,161,154,1,0,0,0,161,
        155,1,0,0,0,161,157,1,0,0,0,162,37,1,0,0,0,12,49,54,66,78,87,95,
        112,127,133,140,148,161
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'~'", "';'", "'.'", "':'", "','", "'('", "')'", "':='" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "INTEGER", "BOOLEAN", "BEGIN", 
                      "END", "WHILE", "DO", "READ", "VAR", "FALSE", "TRUE", 
                      "WRITE", "IF", "THEN", "ELSE", "OPREL", "OPAD", "OPMULT", 
                      "OPLOG", "OPNEG", "PVIG", "PONTO", "DPONTOS", "VIG", 
                      "ABPAR", "FPAR", "ATRIB", "CTE", "CADEIA", "IDENTIFIER", 
                      "COMENTARIO", "WS" ]

    RULE_prog = 0
    RULE_decls = 1
    RULE_listDecl = 2
    RULE_declTip = 3
    RULE_listId = 4
    RULE_tip = 5
    RULE_cmdComp = 6
    RULE_listCmd = 7
    RULE_cmd = 8
    RULE_cmdIf = 9
    RULE_cmdWhile = 10
    RULE_cmdRead = 11
    RULE_cmdWrite = 12
    RULE_cmdAtrib = 13
    RULE_expr = 14
    RULE_exprRel = 15
    RULE_exprArit = 16
    RULE_termo = 17
    RULE_fator = 18

    ruleNames =  [ "prog", "decls", "listDecl", "declTip", "listId", "tip", 
                   "cmdComp", "listCmd", "cmd", "cmdIf", "cmdWhile", "cmdRead", 
                   "cmdWrite", "cmdAtrib", "expr", "exprRel", "exprArit", 
                   "termo", "fator" ]

    EOF = Token.EOF
    PROGRAM=1
    INTEGER=2
    BOOLEAN=3
    BEGIN=4
    END=5
    WHILE=6
    DO=7
    READ=8
    VAR=9
    FALSE=10
    TRUE=11
    WRITE=12
    IF=13
    THEN=14
    ELSE=15
    OPREL=16
    OPAD=17
    OPMULT=18
    OPLOG=19
    OPNEG=20
    PVIG=21
    PONTO=22
    DPONTOS=23
    VIG=24
    ABPAR=25
    FPAR=26
    ATRIB=27
    CTE=28
    CADEIA=29
    IDENTIFIER=30
    COMENTARIO=31
    WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(gramaticaParser.PROGRAM, 0)

        def IDENTIFIER(self):
            return self.getToken(gramaticaParser.IDENTIFIER, 0)

        def PVIG(self):
            return self.getToken(gramaticaParser.PVIG, 0)

        def decls(self):
            return self.getTypedRuleContext(gramaticaParser.DeclsContext,0)


        def cmdComp(self):
            return self.getTypedRuleContext(gramaticaParser.CmdCompContext,0)


        def PONTO(self):
            return self.getToken(gramaticaParser.PONTO, 0)

        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = gramaticaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(gramaticaParser.PROGRAM)
            self.state = 39
            self.match(gramaticaParser.IDENTIFIER)
            self.state = 40
            self.match(gramaticaParser.PVIG)
            self.state = 41
            self.decls()
            self.state = 42
            self.cmdComp()
            self.state = 43
            self.match(gramaticaParser.PONTO)
            self.state = 44
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(gramaticaParser.VAR, 0)

        def listDecl(self):
            return self.getTypedRuleContext(gramaticaParser.ListDeclContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls" ):
                listener.enterDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls" ):
                listener.exitDecls(self)




    def decls(self):

        localctx = gramaticaParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(gramaticaParser.VAR)
                self.state = 47
                self.listDecl()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declTip(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.DeclTipContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.DeclTipContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_listDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListDecl" ):
                listener.enterListDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListDecl" ):
                listener.exitListDecl(self)




    def listDecl(self):

        localctx = gramaticaParser.ListDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_listDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.declTip()
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==30):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclTipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listId(self):
            return self.getTypedRuleContext(gramaticaParser.ListIdContext,0)


        def DPONTOS(self):
            return self.getToken(gramaticaParser.DPONTOS, 0)

        def tip(self):
            return self.getTypedRuleContext(gramaticaParser.TipContext,0)


        def PVIG(self):
            return self.getToken(gramaticaParser.PVIG, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_declTip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclTip" ):
                listener.enterDeclTip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclTip" ):
                listener.exitDeclTip(self)




    def declTip(self):

        localctx = gramaticaParser.DeclTipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declTip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.listId()
            self.state = 57
            self.match(gramaticaParser.DPONTOS)
            self.state = 58
            self.tip()
            self.state = 59
            self.match(gramaticaParser.PVIG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.IDENTIFIER)
            else:
                return self.getToken(gramaticaParser.IDENTIFIER, i)

        def VIG(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.VIG)
            else:
                return self.getToken(gramaticaParser.VIG, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_listId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListId" ):
                listener.enterListId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListId" ):
                listener.exitListId(self)




    def listId(self):

        localctx = gramaticaParser.ListIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(gramaticaParser.IDENTIFIER)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 62
                self.match(gramaticaParser.VIG)
                self.state = 63
                self.match(gramaticaParser.IDENTIFIER)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(gramaticaParser.INTEGER, 0)

        def BOOLEAN(self):
            return self.getToken(gramaticaParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_tip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTip" ):
                listener.enterTip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTip" ):
                listener.exitTip(self)




    def tip(self):

        localctx = gramaticaParser.TipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tip)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdCompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(gramaticaParser.BEGIN, 0)

        def listCmd(self):
            return self.getTypedRuleContext(gramaticaParser.ListCmdContext,0)


        def END(self):
            return self.getToken(gramaticaParser.END, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_cmdComp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdComp" ):
                listener.enterCmdComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdComp" ):
                listener.exitCmdComp(self)




    def cmdComp(self):

        localctx = gramaticaParser.CmdCompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cmdComp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(gramaticaParser.BEGIN)
            self.state = 72
            self.listCmd()
            self.state = 73
            self.match(gramaticaParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CmdContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CmdContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_listCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListCmd" ):
                listener.enterListCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListCmd" ):
                listener.exitListCmd(self)




    def listCmd(self):

        localctx = gramaticaParser.ListCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_listCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073754448) != 0):
                self.state = 75
                self.cmd()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmdIf(self):
            return self.getTypedRuleContext(gramaticaParser.CmdIfContext,0)


        def cmdWhile(self):
            return self.getTypedRuleContext(gramaticaParser.CmdWhileContext,0)


        def cmdRead(self):
            return self.getTypedRuleContext(gramaticaParser.CmdReadContext,0)


        def cmdWrite(self):
            return self.getTypedRuleContext(gramaticaParser.CmdWriteContext,0)


        def cmdAtrib(self):
            return self.getTypedRuleContext(gramaticaParser.CmdAtribContext,0)


        def cmdComp(self):
            return self.getTypedRuleContext(gramaticaParser.CmdCompContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)




    def cmd(self):

        localctx = gramaticaParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cmd)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.cmdIf()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.cmdWhile()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.cmdRead()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.cmdWrite()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 5)
                self.state = 85
                self.cmdAtrib()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.cmdComp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(gramaticaParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def THEN(self):
            return self.getToken(gramaticaParser.THEN, 0)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CmdContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CmdContext,i)


        def ELSE(self):
            return self.getToken(gramaticaParser.ELSE, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_cmdIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdIf" ):
                listener.enterCmdIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdIf" ):
                listener.exitCmdIf(self)




    def cmdIf(self):

        localctx = gramaticaParser.CmdIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cmdIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(gramaticaParser.IF)
            self.state = 90
            self.expr()
            self.state = 91
            self.match(gramaticaParser.THEN)
            self.state = 92
            self.cmd()
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 93
                self.match(gramaticaParser.ELSE)
                self.state = 94
                self.cmd()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(gramaticaParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def DO(self):
            return self.getToken(gramaticaParser.DO, 0)

        def cmd(self):
            return self.getTypedRuleContext(gramaticaParser.CmdContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_cmdWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdWhile" ):
                listener.enterCmdWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdWhile" ):
                listener.exitCmdWhile(self)




    def cmdWhile(self):

        localctx = gramaticaParser.CmdWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cmdWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(gramaticaParser.WHILE)
            self.state = 98
            self.expr()
            self.state = 99
            self.match(gramaticaParser.DO)
            self.state = 100
            self.cmd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(gramaticaParser.READ, 0)

        def ABPAR(self):
            return self.getToken(gramaticaParser.ABPAR, 0)

        def listId(self):
            return self.getTypedRuleContext(gramaticaParser.ListIdContext,0)


        def FPAR(self):
            return self.getToken(gramaticaParser.FPAR, 0)

        def PVIG(self):
            return self.getToken(gramaticaParser.PVIG, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_cmdRead

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdRead" ):
                listener.enterCmdRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdRead" ):
                listener.exitCmdRead(self)




    def cmdRead(self):

        localctx = gramaticaParser.CmdReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_cmdRead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(gramaticaParser.READ)
            self.state = 103
            self.match(gramaticaParser.ABPAR)
            self.state = 104
            self.listId()
            self.state = 105
            self.match(gramaticaParser.FPAR)
            self.state = 106
            self.match(gramaticaParser.PVIG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdWriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(gramaticaParser.WRITE, 0)

        def ABPAR(self):
            return self.getToken(gramaticaParser.ABPAR, 0)

        def FPAR(self):
            return self.getToken(gramaticaParser.FPAR, 0)

        def PVIG(self):
            return self.getToken(gramaticaParser.PVIG, 0)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def CADEIA(self):
            return self.getToken(gramaticaParser.CADEIA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_cmdWrite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdWrite" ):
                listener.enterCmdWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdWrite" ):
                listener.exitCmdWrite(self)




    def cmdWrite(self):

        localctx = gramaticaParser.CmdWriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cmdWrite)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(gramaticaParser.WRITE)
            self.state = 109
            self.match(gramaticaParser.ABPAR)
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 20, 25, 28, 30]:
                self.state = 110
                self.expr()
                pass
            elif token in [29]:
                self.state = 111
                self.match(gramaticaParser.CADEIA)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 114
            self.match(gramaticaParser.FPAR)
            self.state = 115
            self.match(gramaticaParser.PVIG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdAtribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(gramaticaParser.IDENTIFIER, 0)

        def ATRIB(self):
            return self.getToken(gramaticaParser.ATRIB, 0)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def PVIG(self):
            return self.getToken(gramaticaParser.PVIG, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_cmdAtrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdAtrib" ):
                listener.enterCmdAtrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdAtrib" ):
                listener.exitCmdAtrib(self)




    def cmdAtrib(self):

        localctx = gramaticaParser.CmdAtribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_cmdAtrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(gramaticaParser.IDENTIFIER)
            self.state = 118
            self.match(gramaticaParser.ATRIB)
            self.state = 119
            self.expr()
            self.state = 120
            self.match(gramaticaParser.PVIG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprRel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExprRelContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExprRelContext,i)


        def OPLOG(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.OPLOG)
            else:
                return self.getToken(gramaticaParser.OPLOG, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = gramaticaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.exprRel()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 123
                self.match(gramaticaParser.OPLOG)
                self.state = 124
                self.exprRel()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprRelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprArit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExprAritContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExprAritContext,i)


        def OPREL(self):
            return self.getToken(gramaticaParser.OPREL, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_exprRel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprRel" ):
                listener.enterExprRel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprRel" ):
                listener.exitExprRel(self)




    def exprRel(self):

        localctx = gramaticaParser.ExprRelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exprRel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.exprArit()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 131
                self.match(gramaticaParser.OPREL)
                self.state = 132
                self.exprArit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprAritContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.TermoContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.TermoContext,i)


        def OPAD(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.OPAD)
            else:
                return self.getToken(gramaticaParser.OPAD, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_exprArit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprArit" ):
                listener.enterExprArit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprArit" ):
                listener.exitExprArit(self)




    def exprArit(self):

        localctx = gramaticaParser.ExprAritContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exprArit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.termo()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 136
                self.match(gramaticaParser.OPAD)
                self.state = 137
                self.termo()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.FatorContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.FatorContext,i)


        def OPMULT(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.OPMULT)
            else:
                return self.getToken(gramaticaParser.OPMULT, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = gramaticaParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.fator()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 144
                self.match(gramaticaParser.OPMULT)
                self.state = 145
                self.fator()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(gramaticaParser.IDENTIFIER, 0)

        def CTE(self):
            return self.getToken(gramaticaParser.CTE, 0)

        def TRUE(self):
            return self.getToken(gramaticaParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(gramaticaParser.FALSE, 0)

        def OPNEG(self):
            return self.getToken(gramaticaParser.OPNEG, 0)

        def fator(self):
            return self.getTypedRuleContext(gramaticaParser.FatorContext,0)


        def ABPAR(self):
            return self.getToken(gramaticaParser.ABPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def FPAR(self):
            return self.getToken(gramaticaParser.FPAR, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)




    def fator(self):

        localctx = gramaticaParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_fator)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(gramaticaParser.IDENTIFIER)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(gramaticaParser.CTE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.match(gramaticaParser.TRUE)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.match(gramaticaParser.FALSE)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.match(gramaticaParser.OPNEG)
                self.state = 156
                self.fator()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 6)
                self.state = 157
                self.match(gramaticaParser.ABPAR)
                self.state = 158
                self.expr()
                self.state = 159
                self.match(gramaticaParser.FPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





