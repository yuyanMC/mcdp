# Generated from ./dpParser.g4 by ANTLR 4.13.1
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
        4,1,21,103,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,26,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,36,8,2,10,2,12,2,39,9,2,3,2,41,8,2,1,
        2,1,2,1,2,5,2,46,8,2,10,2,12,2,49,9,2,1,2,1,2,1,3,1,3,1,3,1,3,3,
        3,57,8,3,1,4,1,4,3,4,61,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,74,8,5,1,6,1,6,5,6,78,8,6,10,6,12,6,81,9,6,1,6,1,6,1,
        6,1,6,1,6,5,6,88,8,6,10,6,12,6,91,9,6,3,6,93,8,6,1,6,1,6,1,7,1,7,
        3,7,99,8,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,13,14,
        105,0,18,1,0,0,0,2,25,1,0,0,0,4,27,1,0,0,0,6,56,1,0,0,0,8,60,1,0,
        0,0,10,73,1,0,0,0,12,79,1,0,0,0,14,98,1,0,0,0,16,100,1,0,0,0,18,
        19,3,2,1,0,19,20,5,0,0,1,20,1,1,0,0,0,21,22,3,4,2,0,22,23,3,2,1,
        0,23,26,1,0,0,0,24,26,3,4,2,0,25,21,1,0,0,0,25,24,1,0,0,0,26,3,1,
        0,0,0,27,28,5,15,0,0,28,29,5,20,0,0,29,40,5,8,0,0,30,31,5,16,0,0,
        31,37,5,20,0,0,32,33,5,6,0,0,33,34,5,16,0,0,34,36,5,20,0,0,35,32,
        1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,41,1,0,0,0,
        39,37,1,0,0,0,40,30,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,5,
        9,0,0,43,47,5,10,0,0,44,46,3,6,3,0,45,44,1,0,0,0,46,49,1,0,0,0,47,
        45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,51,5,11,
        0,0,51,5,1,0,0,0,52,57,5,1,0,0,53,54,3,8,4,0,54,55,5,7,0,0,55,57,
        1,0,0,0,56,52,1,0,0,0,56,53,1,0,0,0,57,7,1,0,0,0,58,61,3,10,5,0,
        59,61,3,12,6,0,60,58,1,0,0,0,60,59,1,0,0,0,61,9,1,0,0,0,62,63,5,
        17,0,0,63,64,5,18,0,0,64,65,5,16,0,0,65,74,5,20,0,0,66,67,5,18,0,
        0,67,68,5,17,0,0,68,69,5,16,0,0,69,74,5,20,0,0,70,71,5,17,0,0,71,
        72,5,16,0,0,72,74,5,20,0,0,73,62,1,0,0,0,73,66,1,0,0,0,73,70,1,0,
        0,0,74,11,1,0,0,0,75,76,5,20,0,0,76,78,5,12,0,0,77,75,1,0,0,0,78,
        81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,
        0,82,83,5,20,0,0,83,92,5,8,0,0,84,89,3,14,7,0,85,86,5,6,0,0,86,88,
        3,14,7,0,87,85,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,
        90,93,1,0,0,0,91,89,1,0,0,0,92,84,1,0,0,0,92,93,1,0,0,0,93,94,1,
        0,0,0,94,95,5,9,0,0,95,13,1,0,0,0,96,99,5,20,0,0,97,99,3,16,8,0,
        98,96,1,0,0,0,98,97,1,0,0,0,99,15,1,0,0,0,100,101,7,0,0,0,101,17,
        1,0,0,0,11,25,37,40,47,56,60,73,79,89,92,98
    ]

class dpParser ( Parser ):

    grammarFileName = "dpParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'and'", "'or'", "'not'", 
                     "'='", "','", "';'", "'('", "')'", "'{'", "'}'", "'.'", 
                     "<INVALID>", "<INVALID>", "'func'", "<INVALID>", "<INVALID>", 
                     "'player'" ]

    symbolicNames = [ "<INVALID>", "RAW", "AND", "OR", "NOT", "EQ", "COMMA", 
                      "SEMI", "LBRAC", "RBRAC", "LCURLY", "RCURLY", "DOT", 
                      "DOUBLESTRING", "SINGLESTRING", "FUNC", "TYPE", "VAR", 
                      "PLAYER", "INT", "ID", "WS" ]

    RULE_program = 0
    RULE_stat = 1
    RULE_dfunc = 2
    RULE_command_with_raw = 3
    RULE_command = 4
    RULE_define_var = 5
    RULE_call = 6
    RULE_paramter = 7
    RULE_string = 8

    ruleNames =  [ "program", "stat", "dfunc", "command_with_raw", "command", 
                   "define_var", "call", "paramter", "string" ]

    EOF = Token.EOF
    RAW=1
    AND=2
    OR=3
    NOT=4
    EQ=5
    COMMA=6
    SEMI=7
    LBRAC=8
    RBRAC=9
    LCURLY=10
    RCURLY=11
    DOT=12
    DOUBLESTRING=13
    SINGLESTRING=14
    FUNC=15
    TYPE=16
    VAR=17
    PLAYER=18
    INT=19
    ID=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self):
            return self.getTypedRuleContext(dpParser.StatContext,0)


        def EOF(self):
            return self.getToken(dpParser.EOF, 0)

        def getRuleIndex(self):
            return dpParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = dpParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.stat()
            self.state = 19
            self.match(dpParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dfunc(self):
            return self.getTypedRuleContext(dpParser.DfuncContext,0)


        def stat(self):
            return self.getTypedRuleContext(dpParser.StatContext,0)


        def getRuleIndex(self):
            return dpParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = dpParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.dfunc()
                self.state = 22
                self.stat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.dfunc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(dpParser.FUNC, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(dpParser.ID)
            else:
                return self.getToken(dpParser.ID, i)

        def LBRAC(self):
            return self.getToken(dpParser.LBRAC, 0)

        def RBRAC(self):
            return self.getToken(dpParser.RBRAC, 0)

        def LCURLY(self):
            return self.getToken(dpParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(dpParser.RCURLY, 0)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(dpParser.TYPE)
            else:
                return self.getToken(dpParser.TYPE, i)

        def command_with_raw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dpParser.Command_with_rawContext)
            else:
                return self.getTypedRuleContext(dpParser.Command_with_rawContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(dpParser.COMMA)
            else:
                return self.getToken(dpParser.COMMA, i)

        def getRuleIndex(self):
            return dpParser.RULE_dfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDfunc" ):
                listener.enterDfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDfunc" ):
                listener.exitDfunc(self)




    def dfunc(self):

        localctx = dpParser.DfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dfunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(dpParser.FUNC)
            self.state = 28
            self.match(dpParser.ID)
            self.state = 29
            self.match(dpParser.LBRAC)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 30
                self.match(dpParser.TYPE)
                self.state = 31
                self.match(dpParser.ID)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 32
                    self.match(dpParser.COMMA)
                    self.state = 33
                    self.match(dpParser.TYPE)
                    self.state = 34
                    self.match(dpParser.ID)
                    self.state = 39
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 42
            self.match(dpParser.RBRAC)
            self.state = 43
            self.match(dpParser.LCURLY)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1441794) != 0):
                self.state = 44
                self.command_with_raw()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(dpParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Command_with_rawContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RAW(self):
            return self.getToken(dpParser.RAW, 0)

        def command(self):
            return self.getTypedRuleContext(dpParser.CommandContext,0)


        def SEMI(self):
            return self.getToken(dpParser.SEMI, 0)

        def getRuleIndex(self):
            return dpParser.RULE_command_with_raw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand_with_raw" ):
                listener.enterCommand_with_raw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand_with_raw" ):
                listener.exitCommand_with_raw(self)




    def command_with_raw(self):

        localctx = dpParser.Command_with_rawContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_command_with_raw)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(dpParser.RAW)
                pass
            elif token in [17, 18, 20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.command()
                self.state = 54
                self.match(dpParser.SEMI)
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


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def define_var(self):
            return self.getTypedRuleContext(dpParser.Define_varContext,0)


        def call(self):
            return self.getTypedRuleContext(dpParser.CallContext,0)


        def getRuleIndex(self):
            return dpParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = dpParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_command)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.define_var()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.call()
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


    class Define_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(dpParser.VAR, 0)

        def PLAYER(self):
            return self.getToken(dpParser.PLAYER, 0)

        def TYPE(self):
            return self.getToken(dpParser.TYPE, 0)

        def ID(self):
            return self.getToken(dpParser.ID, 0)

        def getRuleIndex(self):
            return dpParser.RULE_define_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_var" ):
                listener.enterDefine_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_var" ):
                listener.exitDefine_var(self)




    def define_var(self):

        localctx = dpParser.Define_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_define_var)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(dpParser.VAR)
                self.state = 63
                self.match(dpParser.PLAYER)
                self.state = 64
                self.match(dpParser.TYPE)
                self.state = 65
                self.match(dpParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(dpParser.PLAYER)
                self.state = 67
                self.match(dpParser.VAR)
                self.state = 68
                self.match(dpParser.TYPE)
                self.state = 69
                self.match(dpParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(dpParser.VAR)
                self.state = 71
                self.match(dpParser.TYPE)
                self.state = 72
                self.match(dpParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(dpParser.ID)
            else:
                return self.getToken(dpParser.ID, i)

        def LBRAC(self):
            return self.getToken(dpParser.LBRAC, 0)

        def RBRAC(self):
            return self.getToken(dpParser.RBRAC, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(dpParser.DOT)
            else:
                return self.getToken(dpParser.DOT, i)

        def paramter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dpParser.ParamterContext)
            else:
                return self.getTypedRuleContext(dpParser.ParamterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(dpParser.COMMA)
            else:
                return self.getToken(dpParser.COMMA, i)

        def getRuleIndex(self):
            return dpParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = dpParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 75
                    self.match(dpParser.ID)
                    self.state = 76
                    self.match(dpParser.DOT) 
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 82
            self.match(dpParser.ID)
            self.state = 83
            self.match(dpParser.LBRAC)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073152) != 0):
                self.state = 84
                self.paramter()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 85
                    self.match(dpParser.COMMA)
                    self.state = 86
                    self.paramter()
                    self.state = 91
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 94
            self.match(dpParser.RBRAC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(dpParser.ID, 0)

        def string(self):
            return self.getTypedRuleContext(dpParser.StringContext,0)


        def getRuleIndex(self):
            return dpParser.RULE_paramter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamter" ):
                listener.enterParamter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamter" ):
                listener.exitParamter(self)




    def paramter(self):

        localctx = dpParser.ParamterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramter)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(dpParser.ID)
                pass
            elif token in [13, 14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.string()
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


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLESTRING(self):
            return self.getToken(dpParser.DOUBLESTRING, 0)

        def SINGLESTRING(self):
            return self.getToken(dpParser.SINGLESTRING, 0)

        def getRuleIndex(self):
            return dpParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = dpParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
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





