# Generated from ./dpParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .dpParser import dpParser
else:
    from dpParser import dpParser

# This class defines a complete listener for a parse tree produced by dpParser.
class dpParserListener(ParseTreeListener):

    # Enter a parse tree produced by dpParser#program.
    def enterProgram(self, ctx:dpParser.ProgramContext):
        pass

    # Exit a parse tree produced by dpParser#program.
    def exitProgram(self, ctx:dpParser.ProgramContext):
        pass


    # Enter a parse tree produced by dpParser#stat.
    def enterStat(self, ctx:dpParser.StatContext):
        pass

    # Exit a parse tree produced by dpParser#stat.
    def exitStat(self, ctx:dpParser.StatContext):
        pass


    # Enter a parse tree produced by dpParser#dfunc.
    def enterDfunc(self, ctx:dpParser.DfuncContext):
        pass

    # Exit a parse tree produced by dpParser#dfunc.
    def exitDfunc(self, ctx:dpParser.DfuncContext):
        pass


    # Enter a parse tree produced by dpParser#command_with_raw.
    def enterCommand_with_raw(self, ctx:dpParser.Command_with_rawContext):
        pass

    # Exit a parse tree produced by dpParser#command_with_raw.
    def exitCommand_with_raw(self, ctx:dpParser.Command_with_rawContext):
        pass


    # Enter a parse tree produced by dpParser#command.
    def enterCommand(self, ctx:dpParser.CommandContext):
        pass

    # Exit a parse tree produced by dpParser#command.
    def exitCommand(self, ctx:dpParser.CommandContext):
        pass


    # Enter a parse tree produced by dpParser#define_var.
    def enterDefine_var(self, ctx:dpParser.Define_varContext):
        pass

    # Exit a parse tree produced by dpParser#define_var.
    def exitDefine_var(self, ctx:dpParser.Define_varContext):
        pass


    # Enter a parse tree produced by dpParser#call.
    def enterCall(self, ctx:dpParser.CallContext):
        pass

    # Exit a parse tree produced by dpParser#call.
    def exitCall(self, ctx:dpParser.CallContext):
        pass


    # Enter a parse tree produced by dpParser#paramter.
    def enterParamter(self, ctx:dpParser.ParamterContext):
        pass

    # Exit a parse tree produced by dpParser#paramter.
    def exitParamter(self, ctx:dpParser.ParamterContext):
        pass


    # Enter a parse tree produced by dpParser#string.
    def enterString(self, ctx:dpParser.StringContext):
        pass

    # Exit a parse tree produced by dpParser#string.
    def exitString(self, ctx:dpParser.StringContext):
        pass



del dpParser