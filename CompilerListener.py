# Generated from Compiler.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CompilerParser import CompilerParser
else:
    from CompilerParser import CompilerParser

# This class defines a complete listener for a parse tree produced by CompilerParser.
class CompilerListener(ParseTreeListener):

    # Enter a parse tree produced by CompilerParser#prog.
    def enterProg(self, ctx:CompilerParser.ProgContext):
        pass

    # Exit a parse tree produced by CompilerParser#prog.
    def exitProg(self, ctx:CompilerParser.ProgContext):
        pass


    # Enter a parse tree produced by CompilerParser#decls.
    def enterDecls(self, ctx:CompilerParser.DeclsContext):
        pass

    # Exit a parse tree produced by CompilerParser#decls.
    def exitDecls(self, ctx:CompilerParser.DeclsContext):
        pass


    # Enter a parse tree produced by CompilerParser#listdecl.
    def enterListdecl(self, ctx:CompilerParser.ListdeclContext):
        pass

    # Exit a parse tree produced by CompilerParser#listdecl.
    def exitListdecl(self, ctx:CompilerParser.ListdeclContext):
        pass


    # Enter a parse tree produced by CompilerParser#decltip.
    def enterDecltip(self, ctx:CompilerParser.DecltipContext):
        pass

    # Exit a parse tree produced by CompilerParser#decltip.
    def exitDecltip(self, ctx:CompilerParser.DecltipContext):
        pass


    # Enter a parse tree produced by CompilerParser#listid.
    def enterListid(self, ctx:CompilerParser.ListidContext):
        pass

    # Exit a parse tree produced by CompilerParser#listid.
    def exitListid(self, ctx:CompilerParser.ListidContext):
        pass


    # Enter a parse tree produced by CompilerParser#tip.
    def enterTip(self, ctx:CompilerParser.TipContext):
        pass

    # Exit a parse tree produced by CompilerParser#tip.
    def exitTip(self, ctx:CompilerParser.TipContext):
        pass


    # Enter a parse tree produced by CompilerParser#cmdcomp.
    def enterCmdcomp(self, ctx:CompilerParser.CmdcompContext):
        pass

    # Exit a parse tree produced by CompilerParser#cmdcomp.
    def exitCmdcomp(self, ctx:CompilerParser.CmdcompContext):
        pass


    # Enter a parse tree produced by CompilerParser#listcmd.
    def enterListcmd(self, ctx:CompilerParser.ListcmdContext):
        pass

    # Exit a parse tree produced by CompilerParser#listcmd.
    def exitListcmd(self, ctx:CompilerParser.ListcmdContext):
        pass


    # Enter a parse tree produced by CompilerParser#cmd.
    def enterCmd(self, ctx:CompilerParser.CmdContext):
        pass

    # Exit a parse tree produced by CompilerParser#cmd.
    def exitCmd(self, ctx:CompilerParser.CmdContext):
        pass


    # Enter a parse tree produced by CompilerParser#cmdif.
    def enterCmdif(self, ctx:CompilerParser.CmdifContext):
        pass

    # Exit a parse tree produced by CompilerParser#cmdif.
    def exitCmdif(self, ctx:CompilerParser.CmdifContext):
        pass


    # Enter a parse tree produced by CompilerParser#elsepart.
    def enterElsepart(self, ctx:CompilerParser.ElsepartContext):
        pass

    # Exit a parse tree produced by CompilerParser#elsepart.
    def exitElsepart(self, ctx:CompilerParser.ElsepartContext):
        pass


    # Enter a parse tree produced by CompilerParser#cmdwhile.
    def enterCmdwhile(self, ctx:CompilerParser.CmdwhileContext):
        pass

    # Exit a parse tree produced by CompilerParser#cmdwhile.
    def exitCmdwhile(self, ctx:CompilerParser.CmdwhileContext):
        pass


    # Enter a parse tree produced by CompilerParser#cmdread.
    def enterCmdread(self, ctx:CompilerParser.CmdreadContext):
        pass

    # Exit a parse tree produced by CompilerParser#cmdread.
    def exitCmdread(self, ctx:CompilerParser.CmdreadContext):
        pass


    # Enter a parse tree produced by CompilerParser#cmdwrite.
    def enterCmdwrite(self, ctx:CompilerParser.CmdwriteContext):
        pass

    # Exit a parse tree produced by CompilerParser#cmdwrite.
    def exitCmdwrite(self, ctx:CompilerParser.CmdwriteContext):
        pass


    # Enter a parse tree produced by CompilerParser#listw.
    def enterListw(self, ctx:CompilerParser.ListwContext):
        pass

    # Exit a parse tree produced by CompilerParser#listw.
    def exitListw(self, ctx:CompilerParser.ListwContext):
        pass


    # Enter a parse tree produced by CompilerParser#elemw.
    def enterElemw(self, ctx:CompilerParser.ElemwContext):
        pass

    # Exit a parse tree produced by CompilerParser#elemw.
    def exitElemw(self, ctx:CompilerParser.ElemwContext):
        pass


    # Enter a parse tree produced by CompilerParser#cmdatrib.
    def enterCmdatrib(self, ctx:CompilerParser.CmdatribContext):
        pass

    # Exit a parse tree produced by CompilerParser#cmdatrib.
    def exitCmdatrib(self, ctx:CompilerParser.CmdatribContext):
        pass


    # Enter a parse tree produced by CompilerParser#expr.
    def enterExpr(self, ctx:CompilerParser.ExprContext):
        pass

    # Exit a parse tree produced by CompilerParser#expr.
    def exitExpr(self, ctx:CompilerParser.ExprContext):
        pass


    # Enter a parse tree produced by CompilerParser#expr1.
    def enterExpr1(self, ctx:CompilerParser.Expr1Context):
        pass

    # Exit a parse tree produced by CompilerParser#expr1.
    def exitExpr1(self, ctx:CompilerParser.Expr1Context):
        pass


    # Enter a parse tree produced by CompilerParser#term.
    def enterTerm(self, ctx:CompilerParser.TermContext):
        pass

    # Exit a parse tree produced by CompilerParser#term.
    def exitTerm(self, ctx:CompilerParser.TermContext):
        pass


    # Enter a parse tree produced by CompilerParser#term1.
    def enterTerm1(self, ctx:CompilerParser.Term1Context):
        pass

    # Exit a parse tree produced by CompilerParser#term1.
    def exitTerm1(self, ctx:CompilerParser.Term1Context):
        pass


    # Enter a parse tree produced by CompilerParser#factor.
    def enterFactor(self, ctx:CompilerParser.FactorContext):
        pass

    # Exit a parse tree produced by CompilerParser#factor.
    def exitFactor(self, ctx:CompilerParser.FactorContext):
        pass


    # Enter a parse tree produced by CompilerParser#factor1.
    def enterFactor1(self, ctx:CompilerParser.Factor1Context):
        pass

    # Exit a parse tree produced by CompilerParser#factor1.
    def exitFactor1(self, ctx:CompilerParser.Factor1Context):
        pass


    # Enter a parse tree produced by CompilerParser#primary.
    def enterPrimary(self, ctx:CompilerParser.PrimaryContext):
        pass

    # Exit a parse tree produced by CompilerParser#primary.
    def exitPrimary(self, ctx:CompilerParser.PrimaryContext):
        pass



del CompilerParser