# Generated from JavaScriptParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

if __name__ is not None and "." in __name__:
    from .JavaScriptBaseParser import JavaScriptBaseParser
else:
    from JavaScriptBaseParser import JavaScriptBaseParser


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3p")
        buf.write("\u030d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\5\2|\n\2\3\2\3\2\3\3\5\3\u0081\n\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4\u0096\n\4\3\5\3\5\5\5\u009a\n")
        buf.write("\5\3\5\3\5\3\6\6\6\u009f\n\6\r\6\16\6\u00a0\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\7\b\u00aa\n\b\f\b\16\b\u00ad\13\b\3")
        buf.write("\t\3\t\3\t\5\t\u00b2\n\t\3\t\3\t\5\t\u00b6\n\t\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00c5")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\r\u00d8\n\r\3\r\3\r\5\r\u00dc\n\r")
        buf.write("\3\r\3\r\5\r\u00e0\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00ea\n\r\3\r\3\r\5\r\u00ee\n\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\r\u00f9\n\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\5\r\u0106\n\r\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u010c\n\r\3\16\3\16\3\17\3\17\3\17\5\17\u0113\n\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\5\20\u011a\n\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\5\21\u0121\n\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\5\24\u0133\n\24\3\24\3\24\5\24\u0137\n\24\5\24\u0139")
        buf.write("\n\24\3\24\3\24\3\25\6\25\u013e\n\25\r\25\16\25\u013f")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u0146\n\26\3\27\3\27\3\27\5")
        buf.write("\27\u014b\n\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\5\32\u015a\n\32\3\32\5\32\u015d")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\5\36\u016f\n\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \5 \u017c")
        buf.write("\n \3 \3 \7 \u0180\n \f \16 \u0183\13 \3 \3 \3!\3!\3!")
        buf.write("\5!\u018a\n!\3!\3!\5!\u018e\n!\3\"\3\"\3\"\5\"\u0193\n")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\5\"\u01a4\n\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01ac")
        buf.write("\n\"\3#\5#\u01af\n#\3#\3#\3#\5#\u01b4\n#\3#\3#\3#\3#\3")
        buf.write("#\3$\3$\3$\7$\u01be\n$\f$\16$\u01c1\13$\3$\3$\5$\u01c5")
        buf.write("\n$\3$\3$\3$\5$\u01ca\n$\3%\3%\3%\5%\u01cf\n%\3&\3&\3")
        buf.write("&\3\'\5\'\u01d5\n\'\3(\6(\u01d8\n(\r(\16(\u01d9\3)\3)")
        buf.write("\7)\u01de\n)\f)\16)\u01e1\13)\3)\5)\u01e4\n)\3)\7)\u01e7")
        buf.write("\n)\f)\16)\u01ea\13)\3)\3)\3*\3*\6*\u01f0\n*\r*\16*\u01f1")
        buf.write("\3*\7*\u01f5\n*\f*\16*\u01f8\13*\3*\6*\u01fb\n*\r*\16")
        buf.write("*\u01fc\3*\5*\u0200\n*\3*\5*\u0203\n*\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\7,\u020c\n,\f,\16,\u020f\13,\5,\u0211\n,\3,\5,\u0214")
        buf.write("\n,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0233\n-\3.\3")
        buf.write(".\3.\5.\u0238\n.\3/\3/\3/\3/\7/\u023e\n/\f/\16/\u0241")
        buf.write("\13/\3/\3/\5/\u0245\n/\3/\5/\u0248\n/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\7\61\u0252\n\61\f\61\16\61\u0255")
        buf.write("\13\61\3\62\3\62\3\62\5\62\u025a\n\62\3\62\3\62\5\62\u025e")
        buf.write("\n\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0267\n")
        buf.write("\62\3\62\3\62\3\62\3\62\5\62\u026d\n\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u028f\n\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\7\62\u02d4\n\62\f\62\16\62\u02d7\13\62\3\63\3\63")
        buf.write("\3\63\5\63\u02dc\n\63\3\63\5\63\u02df\n\63\3\64\3\64\3")
        buf.write("\64\3\64\3\64\5\64\u02e6\n\64\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\5\66\u02f0\n\66\3\67\3\67\38\38\58\u02f6")
        buf.write("\n8\39\39\39\59\u02fb\n9\3:\3:\3;\3;\3;\3;\3<\3<\3<\3")
        buf.write("<\3=\3=\3=\3=\5=\u030b\n=\3=\2\3b>\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvx\2\f\5\2FF]]aa\4\2\16\16\20\20\3\2")
        buf.write("\31\33\3\2\25\26\3\2\34\36\3\2\37\"\3\2#&\3\2,\66\3\2")
        buf.write(":>\3\2?h\2\u0366\2{\3\2\2\2\4\u0080\3\2\2\2\6\u0095\3")
        buf.write("\2\2\2\b\u0097\3\2\2\2\n\u009e\3\2\2\2\f\u00a2\3\2\2\2")
        buf.write("\16\u00a6\3\2\2\2\20\u00b1\3\2\2\2\22\u00b7\3\2\2\2\24")
        buf.write("\u00b9\3\2\2\2\26\u00bd\3\2\2\2\30\u010b\3\2\2\2\32\u010d")
        buf.write("\3\2\2\2\34\u010f\3\2\2\2\36\u0116\3\2\2\2 \u011d\3\2")
        buf.write("\2\2\"\u0124\3\2\2\2$\u012a\3\2\2\2&\u0130\3\2\2\2(\u013d")
        buf.write("\3\2\2\2*\u0141\3\2\2\2,\u0147\3\2\2\2.\u014c\3\2\2\2")
        buf.write("\60\u0150\3\2\2\2\62\u0155\3\2\2\2\64\u015e\3\2\2\2\66")
        buf.write("\u0164\3\2\2\28\u0167\3\2\2\2:\u016a\3\2\2\2<\u0175\3")
        buf.write("\2\2\2>\u017b\3\2\2\2@\u018d\3\2\2\2B\u01ab\3\2\2\2D\u01ae")
        buf.write("\3\2\2\2F\u01c9\3\2\2\2H\u01cb\3\2\2\2J\u01d0\3\2\2\2")
        buf.write("L\u01d4\3\2\2\2N\u01d7\3\2\2\2P\u01db\3\2\2\2R\u0202\3")
        buf.write("\2\2\2T\u0204\3\2\2\2V\u0207\3\2\2\2X\u0232\3\2\2\2Z\u0237")
        buf.write("\3\2\2\2\\\u0239\3\2\2\2^\u024b\3\2\2\2`\u024e\3\2\2\2")
        buf.write("b\u028e\3\2\2\2d\u02de\3\2\2\2f\u02e5\3\2\2\2h\u02e7\3")
        buf.write("\2\2\2j\u02ef\3\2\2\2l\u02f1\3\2\2\2n\u02f5\3\2\2\2p\u02fa")
        buf.write("\3\2\2\2r\u02fc\3\2\2\2t\u02fe\3\2\2\2v\u0302\3\2\2\2")
        buf.write("x\u030a\3\2\2\2z|\5N(\2{z\3\2\2\2{|\3\2\2\2|}\3\2\2\2")
        buf.write("}~\7\2\2\3~\3\3\2\2\2\177\u0081\7^\2\2\u0080\177\3\2\2")
        buf.write("\2\u0080\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083")
        buf.write("\5\6\4\2\u0083\5\3\2\2\2\u0084\u0096\5\b\5\2\u0085\u0096")
        buf.write("\5\f\7\2\u0086\u0096\5\22\n\2\u0087\u0096\5\24\13\2\u0088")
        buf.write("\u0096\5\26\f\2\u0089\u0096\5\30\r\2\u008a\u0096\5\34")
        buf.write("\17\2\u008b\u0096\5\36\20\2\u008c\u0096\5 \21\2\u008d")
        buf.write("\u0096\5\"\22\2\u008e\u0096\5.\30\2\u008f\u0096\5$\23")
        buf.write("\2\u0090\u0096\5\60\31\2\u0091\u0096\5\62\32\2\u0092\u0096")
        buf.write("\58\35\2\u0093\u0096\5:\36\2\u0094\u0096\5<\37\2\u0095")
        buf.write("\u0084\3\2\2\2\u0095\u0085\3\2\2\2\u0095\u0086\3\2\2\2")
        buf.write("\u0095\u0087\3\2\2\2\u0095\u0088\3\2\2\2\u0095\u0089\3")
        buf.write("\2\2\2\u0095\u008a\3\2\2\2\u0095\u008b\3\2\2\2\u0095\u008c")
        buf.write("\3\2\2\2\u0095\u008d\3\2\2\2\u0095\u008e\3\2\2\2\u0095")
        buf.write("\u008f\3\2\2\2\u0095\u0090\3\2\2\2\u0095\u0091\3\2\2\2")
        buf.write("\u0095\u0092\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3")
        buf.write("\2\2\2\u0096\7\3\2\2\2\u0097\u0099\7\n\2\2\u0098\u009a")
        buf.write("\5\n\6\2\u0099\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009c\7\13\2\2\u009c\t\3\2\2\2\u009d")
        buf.write("\u009f\5\6\4\2\u009e\u009d\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\13\3\2")
        buf.write("\2\2\u00a2\u00a3\5\32\16\2\u00a3\u00a4\5\16\b\2\u00a4")
        buf.write("\u00a5\5x=\2\u00a5\r\3\2\2\2\u00a6\u00ab\5\20\t\2\u00a7")
        buf.write("\u00a8\7\r\2\2\u00a8\u00aa\5\20\t\2\u00a9\u00a7\3\2\2")
        buf.write("\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac")
        buf.write("\3\2\2\2\u00ac\17\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b2")
        buf.write("\7i\2\2\u00af\u00b2\5P)\2\u00b0\u00b2\5V,\2\u00b1\u00ae")
        buf.write("\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b5\3\2\2\2\u00b3\u00b4\7\16\2\2\u00b4\u00b6\5b\62")
        buf.write("\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\21\3")
        buf.write("\2\2\2\u00b7\u00b8\7\f\2\2\u00b8\23\3\2\2\2\u00b9\u00ba")
        buf.write("\6\13\2\2\u00ba\u00bb\5`\61\2\u00bb\u00bc\5x=\2\u00bc")
        buf.write("\25\3\2\2\2\u00bd\u00be\7T\2\2\u00be\u00bf\7\b\2\2\u00bf")
        buf.write("\u00c0\5`\61\2\u00c0\u00c1\7\t\2\2\u00c1\u00c4\5\6\4\2")
        buf.write("\u00c2\u00c3\7D\2\2\u00c3\u00c5\5\6\4\2\u00c4\u00c2\3")
        buf.write("\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\27\3\2\2\2\u00c6\u00c7")
        buf.write("\7@\2\2\u00c7\u00c8\5\6\4\2\u00c8\u00c9\7N\2\2\u00c9\u00ca")
        buf.write("\7\b\2\2\u00ca\u00cb\5`\61\2\u00cb\u00cc\7\t\2\2\u00cc")
        buf.write("\u00cd\5x=\2\u00cd\u010c\3\2\2\2\u00ce\u00cf\7N\2\2\u00cf")
        buf.write("\u00d0\7\b\2\2\u00d0\u00d1\5`\61\2\u00d1\u00d2\7\t\2\2")
        buf.write("\u00d2\u00d3\5\6\4\2\u00d3\u010c\3\2\2\2\u00d4\u00d5\7")
        buf.write("L\2\2\u00d5\u00d7\7\b\2\2\u00d6\u00d8\5`\61\2\u00d7\u00d6")
        buf.write("\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\u00db\7\f\2\2\u00da\u00dc\5`\61\2\u00db\u00da\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00df\7")
        buf.write("\f\2\2\u00de\u00e0\5`\61\2\u00df\u00de\3\2\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\7\t\2\2\u00e2")
        buf.write("\u010c\5\6\4\2\u00e3\u00e4\7L\2\2\u00e4\u00e5\7\b\2\2")
        buf.write("\u00e5\u00e6\5\32\16\2\u00e6\u00e7\5\16\b\2\u00e7\u00e9")
        buf.write("\7\f\2\2\u00e8\u00ea\5`\61\2\u00e9\u00e8\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ed\7\f\2\2")
        buf.write("\u00ec\u00ee\5`\61\2\u00ed\u00ec\3\2\2\2\u00ed\u00ee\3")
        buf.write("\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\7\t\2\2\u00f0\u00f1")
        buf.write("\5\6\4\2\u00f1\u010c\3\2\2\2\u00f2\u00f3\7L\2\2\u00f3")
        buf.write("\u00f4\7\b\2\2\u00f4\u00f8\5b\62\2\u00f5\u00f9\7W\2\2")
        buf.write("\u00f6\u00f7\7i\2\2\u00f7\u00f9\6\r\3\2\u00f8\u00f5\3")
        buf.write("\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb")
        buf.write("\5`\61\2\u00fb\u00fc\7\t\2\2\u00fc\u00fd\5\6\4\2\u00fd")
        buf.write("\u010c\3\2\2\2\u00fe\u00ff\7L\2\2\u00ff\u0100\7\b\2\2")
        buf.write("\u0100\u0101\5\32\16\2\u0101\u0105\5\20\t\2\u0102\u0106")
        buf.write("\7W\2\2\u0103\u0104\7i\2\2\u0104\u0106\6\r\4\2\u0105\u0102")
        buf.write("\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0107\3\2\2\2\u0107")
        buf.write("\u0108\5`\61\2\u0108\u0109\7\t\2\2\u0109\u010a\5\6\4\2")
        buf.write("\u010a\u010c\3\2\2\2\u010b\u00c6\3\2\2\2\u010b\u00ce\3")
        buf.write("\2\2\2\u010b\u00d4\3\2\2\2\u010b\u00e3\3\2\2\2\u010b\u00f2")
        buf.write("\3\2\2\2\u010b\u00fe\3\2\2\2\u010c\31\3\2\2\2\u010d\u010e")
        buf.write("\t\2\2\2\u010e\33\3\2\2\2\u010f\u0112\7K\2\2\u0110\u0111")
        buf.write("\6\17\5\2\u0111\u0113\7i\2\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\5x=\2\u0115")
        buf.write("\35\3\2\2\2\u0116\u0119\7?\2\2\u0117\u0118\6\20\6\2\u0118")
        buf.write("\u011a\7i\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2")
        buf.write("\u011a\u011b\3\2\2\2\u011b\u011c\5x=\2\u011c\37\3\2\2")
        buf.write("\2\u011d\u0120\7I\2\2\u011e\u011f\6\21\7\2\u011f\u0121")
        buf.write("\5`\61\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write("\u0122\3\2\2\2\u0122\u0123\5x=\2\u0123!\3\2\2\2\u0124")
        buf.write("\u0125\7R\2\2\u0125\u0126\7\b\2\2\u0126\u0127\5`\61\2")
        buf.write("\u0127\u0128\7\t\2\2\u0128\u0129\5\6\4\2\u0129#\3\2\2")
        buf.write("\2\u012a\u012b\7M\2\2\u012b\u012c\7\b\2\2\u012c\u012d")
        buf.write("\5`\61\2\u012d\u012e\7\t\2\2\u012e\u012f\5&\24\2\u012f")
        buf.write("%\3\2\2\2\u0130\u0132\7\n\2\2\u0131\u0133\5(\25\2\u0132")
        buf.write("\u0131\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0138\3\2\2\2")
        buf.write("\u0134\u0136\5,\27\2\u0135\u0137\5(\25\2\u0136\u0135\3")
        buf.write("\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139\3\2\2\2\u0138\u0134")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013b\7\13\2\2\u013b\'\3\2\2\2\u013c\u013e\5*\26\2\u013d")
        buf.write("\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u013d\3\2\2\2")
        buf.write("\u013f\u0140\3\2\2\2\u0140)\3\2\2\2\u0141\u0142\7C\2\2")
        buf.write("\u0142\u0143\5`\61\2\u0143\u0145\7\20\2\2\u0144\u0146")
        buf.write("\5\n\6\2\u0145\u0144\3\2\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write("+\3\2\2\2\u0147\u0148\7S\2\2\u0148\u014a\7\20\2\2\u0149")
        buf.write("\u014b\5\n\6\2\u014a\u0149\3\2\2\2\u014a\u014b\3\2\2\2")
        buf.write("\u014b-\3\2\2\2\u014c\u014d\7i\2\2\u014d\u014e\7\20\2")
        buf.write("\2\u014e\u014f\5\6\4\2\u014f/\3\2\2\2\u0150\u0151\7U\2")
        buf.write("\2\u0151\u0152\6\31\b\2\u0152\u0153\5`\61\2\u0153\u0154")
        buf.write("\5x=\2\u0154\61\3\2\2\2\u0155\u0156\7X\2\2\u0156\u015c")
        buf.write("\5\b\5\2\u0157\u0159\5\64\33\2\u0158\u015a\5\66\34\2\u0159")
        buf.write("\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015d\3\2\2\2")
        buf.write("\u015b\u015d\5\66\34\2\u015c\u0157\3\2\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015d\63\3\2\2\2\u015e\u015f\7G\2\2\u015f\u0160")
        buf.write("\7\b\2\2\u0160\u0161\7i\2\2\u0161\u0162\7\t\2\2\u0162")
        buf.write("\u0163\5\b\5\2\u0163\65\3\2\2\2\u0164\u0165\7H\2\2\u0165")
        buf.write("\u0166\5\b\5\2\u0166\67\3\2\2\2\u0167\u0168\7O\2\2\u0168")
        buf.write("\u0169\5x=\2\u01699\3\2\2\2\u016a\u016b\7P\2\2\u016b\u016c")
        buf.write("\7i\2\2\u016c\u016e\7\b\2\2\u016d\u016f\5F$\2\u016e\u016d")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170")
        buf.write("\u0171\7\t\2\2\u0171\u0172\7\n\2\2\u0172\u0173\5L\'\2")
        buf.write("\u0173\u0174\7\13\2\2\u0174;\3\2\2\2\u0175\u0176\7Y\2")
        buf.write("\2\u0176\u0177\7i\2\2\u0177\u0178\5> \2\u0178=\3\2\2\2")
        buf.write("\u0179\u017a\7[\2\2\u017a\u017c\5b\62\2\u017b\u0179\3")
        buf.write("\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u0181")
        buf.write("\7\n\2\2\u017e\u0180\5@!\2\u017f\u017e\3\2\2\2\u0180\u0183")
        buf.write("\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\u0184\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\7\13\2")
        buf.write("\2\u0185?\3\2\2\2\u0186\u018a\7g\2\2\u0187\u0188\6!\t")
        buf.write("\2\u0188\u018a\7i\2\2\u0189\u0186\3\2\2\2\u0189\u0187")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u018e\5B\"\2\u018c\u018e\5\22\n\2\u018d\u0189\3\2\2\2")
        buf.write("\u018d\u018c\3\2\2\2\u018eA\3\2\2\2\u018f\u0190\5Z.\2")
        buf.write("\u0190\u0192\7\b\2\2\u0191\u0193\5F$\2\u0192\u0191\3\2")
        buf.write("\2\2\u0192\u0193\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0195")
        buf.write("\7\t\2\2\u0195\u0196\7\n\2\2\u0196\u0197\5L\'\2\u0197")
        buf.write("\u0198\7\13\2\2\u0198\u01ac\3\2\2\2\u0199\u019a\5t;\2")
        buf.write("\u019a\u019b\7\b\2\2\u019b\u019c\7\t\2\2\u019c\u019d\7")
        buf.write("\n\2\2\u019d\u019e\5L\'\2\u019e\u019f\7\13\2\2\u019f\u01ac")
        buf.write("\3\2\2\2\u01a0\u01a1\5v<\2\u01a1\u01a3\7\b\2\2\u01a2\u01a4")
        buf.write("\5F$\2\u01a3\u01a2\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5")
        buf.write("\3\2\2\2\u01a5\u01a6\7\t\2\2\u01a6\u01a7\7\n\2\2\u01a7")
        buf.write("\u01a8\5L\'\2\u01a8\u01a9\7\13\2\2\u01a9\u01ac\3\2\2\2")
        buf.write("\u01aa\u01ac\5D#\2\u01ab\u018f\3\2\2\2\u01ab\u0199\3\2")
        buf.write("\2\2\u01ab\u01a0\3\2\2\2\u01ab\u01aa\3\2\2\2\u01acC\3")
        buf.write("\2\2\2\u01ad\u01af\7\31\2\2\u01ae\u01ad\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\7i\2\2")
        buf.write("\u01b1\u01b3\7\b\2\2\u01b2\u01b4\5F$\2\u01b3\u01b2\3\2")
        buf.write("\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6")
        buf.write("\7\t\2\2\u01b6\u01b7\7\n\2\2\u01b7\u01b8\5L\'\2\u01b8")
        buf.write("\u01b9\7\13\2\2\u01b9E\3\2\2\2\u01ba\u01bf\5H%\2\u01bb")
        buf.write("\u01bc\7\r\2\2\u01bc\u01be\5H%\2\u01bd\u01bb\3\2\2\2\u01be")
        buf.write("\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2")
        buf.write("\u01c0\u01c4\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c3\7")
        buf.write("\r\2\2\u01c3\u01c5\5J&\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5")
        buf.write("\3\2\2\2\u01c5\u01ca\3\2\2\2\u01c6\u01ca\5J&\2\u01c7\u01ca")
        buf.write("\5P)\2\u01c8\u01ca\5V,\2\u01c9\u01ba\3\2\2\2\u01c9\u01c6")
        buf.write("\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("G\3\2\2\2\u01cb\u01ce\7i\2\2\u01cc\u01cd\7\16\2\2\u01cd")
        buf.write("\u01cf\5b\62\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2")
        buf.write("\u01cfI\3\2\2\2\u01d0\u01d1\7\21\2\2\u01d1\u01d2\7i\2")
        buf.write("\2\u01d2K\3\2\2\2\u01d3\u01d5\5N(\2\u01d4\u01d3\3\2\2")
        buf.write("\2\u01d4\u01d5\3\2\2\2\u01d5M\3\2\2\2\u01d6\u01d8\5\4")
        buf.write("\3\2\u01d7\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01d7")
        buf.write("\3\2\2\2\u01d9\u01da\3\2\2\2\u01daO\3\2\2\2\u01db\u01df")
        buf.write("\7\6\2\2\u01dc\u01de\7\r\2\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write("\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2")
        buf.write("\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e4\5")
        buf.write("R*\2\u01e3\u01e2\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e8")
        buf.write("\3\2\2\2\u01e5\u01e7\7\r\2\2\u01e6\u01e5\3\2\2\2\u01e7")
        buf.write("\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2")
        buf.write("\u01e9\u01eb\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ec\7")
        buf.write("\7\2\2\u01ecQ\3\2\2\2\u01ed\u01f6\5b\62\2\u01ee\u01f0")
        buf.write("\7\r\2\2\u01ef\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1")
        buf.write("\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\3\2\2\2")
        buf.write("\u01f3\u01f5\5b\62\2\u01f4\u01ef\3\2\2\2\u01f5\u01f8\3")
        buf.write("\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01ff")
        buf.write("\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01fb\7\r\2\2\u01fa")
        buf.write("\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fa\3\2\2\2")
        buf.write("\u01fc\u01fd\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0200\5")
        buf.write("T+\2\u01ff\u01fa\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0203")
        buf.write("\3\2\2\2\u0201\u0203\5T+\2\u0202\u01ed\3\2\2\2\u0202\u0201")
        buf.write("\3\2\2\2\u0203S\3\2\2\2\u0204\u0205\7\21\2\2\u0205\u0206")
        buf.write("\7i\2\2\u0206U\3\2\2\2\u0207\u0210\7\n\2\2\u0208\u020d")
        buf.write("\5X-\2\u0209\u020a\7\r\2\2\u020a\u020c\5X-\2\u020b\u0209")
        buf.write("\3\2\2\2\u020c\u020f\3\2\2\2\u020d\u020b\3\2\2\2\u020d")
        buf.write("\u020e\3\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d\3\2\2\2")
        buf.write("\u0210\u0208\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0213\3")
        buf.write("\2\2\2\u0212\u0214\7\r\2\2\u0213\u0212\3\2\2\2\u0213\u0214")
        buf.write("\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0216\7\13\2\2\u0216")
        buf.write("W\3\2\2\2\u0217\u0218\5Z.\2\u0218\u0219\t\3\2\2\u0219")
        buf.write("\u021a\5b\62\2\u021a\u0233\3\2\2\2\u021b\u021c\7\6\2\2")
        buf.write("\u021c\u021d\5b\62\2\u021d\u021e\7\7\2\2\u021e\u021f\7")
        buf.write("\20\2\2\u021f\u0220\5b\62\2\u0220\u0233\3\2\2\2\u0221")
        buf.write("\u0222\5t;\2\u0222\u0223\7\b\2\2\u0223\u0224\7\t\2\2\u0224")
        buf.write("\u0225\7\n\2\2\u0225\u0226\5L\'\2\u0226\u0227\7\13\2\2")
        buf.write("\u0227\u0233\3\2\2\2\u0228\u0229\5v<\2\u0229\u022a\7\b")
        buf.write("\2\2\u022a\u022b\7i\2\2\u022b\u022c\7\t\2\2\u022c\u022d")
        buf.write("\7\n\2\2\u022d\u022e\5L\'\2\u022e\u022f\7\13\2\2\u022f")
        buf.write("\u0233\3\2\2\2\u0230\u0233\5D#\2\u0231\u0233\7i\2\2\u0232")
        buf.write("\u0217\3\2\2\2\u0232\u021b\3\2\2\2\u0232\u0221\3\2\2\2")
        buf.write("\u0232\u0228\3\2\2\2\u0232\u0230\3\2\2\2\u0232\u0231\3")
        buf.write("\2\2\2\u0233Y\3\2\2\2\u0234\u0238\5n8\2\u0235\u0238\7")
        buf.write("j\2\2\u0236\u0238\5l\67\2\u0237\u0234\3\2\2\2\u0237\u0235")
        buf.write("\3\2\2\2\u0237\u0236\3\2\2\2\u0238[\3\2\2\2\u0239\u0247")
        buf.write("\7\b\2\2\u023a\u023f\5b\62\2\u023b\u023c\7\r\2\2\u023c")
        buf.write("\u023e\5b\62\2\u023d\u023b\3\2\2\2\u023e\u0241\3\2\2\2")
        buf.write("\u023f\u023d\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0244\3")
        buf.write("\2\2\2\u0241\u023f\3\2\2\2\u0242\u0243\7\r\2\2\u0243\u0245")
        buf.write("\5^\60\2\u0244\u0242\3\2\2\2\u0244\u0245\3\2\2\2\u0245")
        buf.write("\u0248\3\2\2\2\u0246\u0248\5^\60\2\u0247\u023a\3\2\2\2")
        buf.write("\u0247\u0246\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u0249\3")
        buf.write("\2\2\2\u0249\u024a\7\t\2\2\u024a]\3\2\2\2\u024b\u024c")
        buf.write("\7\21\2\2\u024c\u024d\7i\2\2\u024d_\3\2\2\2\u024e\u0253")
        buf.write("\5b\62\2\u024f\u0250\7\r\2\2\u0250\u0252\5b\62\2\u0251")
        buf.write("\u024f\3\2\2\2\u0252\u0255\3\2\2\2\u0253\u0251\3\2\2\2")
        buf.write("\u0253\u0254\3\2\2\2\u0254a\3\2\2\2\u0255\u0253\3\2\2")
        buf.write("\2\u0256\u0257\b\62\1\2\u0257\u0259\7P\2\2\u0258\u025a")
        buf.write("\7i\2\2\u0259\u0258\3\2\2\2\u0259\u025a\3\2\2\2\u025a")
        buf.write("\u025b\3\2\2\2\u025b\u025d\7\b\2\2\u025c\u025e\5F$\2\u025d")
        buf.write("\u025c\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u025f\3\2\2\2")
        buf.write("\u025f\u0260\7\t\2\2\u0260\u0261\7\n\2\2\u0261\u0262\5")
        buf.write("L\'\2\u0262\u0263\7\13\2\2\u0263\u028f\3\2\2\2\u0264\u0266")
        buf.write("\7Y\2\2\u0265\u0267\7i\2\2\u0266\u0265\3\2\2\2\u0266\u0267")
        buf.write("\3\2\2\2\u0267\u0268\3\2\2\2\u0268\u028f\5> \2\u0269\u026a")
        buf.write("\7E\2\2\u026a\u026c\5b\62\2\u026b\u026d\5\\/\2\u026c\u026b")
        buf.write("\3\2\2\2\u026c\u026d\3\2\2\2\u026d\u028f\3\2\2\2\u026e")
        buf.write("\u026f\7V\2\2\u026f\u028f\5b\62#\u0270\u0271\7J\2\2\u0271")
        buf.write("\u028f\5b\62\"\u0272\u0273\7B\2\2\u0273\u028f\5b\62!\u0274")
        buf.write("\u0275\7\23\2\2\u0275\u028f\5b\62 \u0276\u0277\7\24\2")
        buf.write("\2\u0277\u028f\5b\62\37\u0278\u0279\7\25\2\2\u0279\u028f")
        buf.write("\5b\62\36\u027a\u027b\7\26\2\2\u027b\u028f\5b\62\35\u027c")
        buf.write("\u027d\7\27\2\2\u027d\u028f\5b\62\34\u027e\u027f\7\30")
        buf.write("\2\2\u027f\u028f\5b\62\33\u0280\u028f\7Q\2\2\u0281\u028f")
        buf.write("\7i\2\2\u0282\u028f\7\\\2\2\u0283\u028f\5j\66\2\u0284")
        buf.write("\u028f\5P)\2\u0285\u028f\5V,\2\u0286\u0287\7\b\2\2\u0287")
        buf.write("\u0288\5`\61\2\u0288\u0289\7\t\2\2\u0289\u028f\3\2\2\2")
        buf.write("\u028a\u028b\5d\63\2\u028b\u028c\7\67\2\2\u028c\u028d")
        buf.write("\5f\64\2\u028d\u028f\3\2\2\2\u028e\u0256\3\2\2\2\u028e")
        buf.write("\u0264\3\2\2\2\u028e\u0269\3\2\2\2\u028e\u026e\3\2\2\2")
        buf.write("\u028e\u0270\3\2\2\2\u028e\u0272\3\2\2\2\u028e\u0274\3")
        buf.write("\2\2\2\u028e\u0276\3\2\2\2\u028e\u0278\3\2\2\2\u028e\u027a")
        buf.write("\3\2\2\2\u028e\u027c\3\2\2\2\u028e\u027e\3\2\2\2\u028e")
        buf.write("\u0280\3\2\2\2\u028e\u0281\3\2\2\2\u028e\u0282\3\2\2\2")
        buf.write("\u028e\u0283\3\2\2\2\u028e\u0284\3\2\2\2\u028e\u0285\3")
        buf.write("\2\2\2\u028e\u0286\3\2\2\2\u028e\u028a\3\2\2\2\u028f\u02d5")
        buf.write("\3\2\2\2\u0290\u0291\f\32\2\2\u0291\u0292\t\4\2\2\u0292")
        buf.write("\u02d4\5b\62\33\u0293\u0294\f\31\2\2\u0294\u0295\t\5\2")
        buf.write("\2\u0295\u02d4\5b\62\32\u0296\u0297\f\30\2\2\u0297\u0298")
        buf.write("\t\6\2\2\u0298\u02d4\5b\62\31\u0299\u029a\f\27\2\2\u029a")
        buf.write("\u029b\t\7\2\2\u029b\u02d4\5b\62\30\u029c\u029d\f\26\2")
        buf.write("\2\u029d\u029e\7A\2\2\u029e\u02d4\5b\62\27\u029f\u02a0")
        buf.write("\f\25\2\2\u02a0\u02a1\7W\2\2\u02a1\u02d4\5b\62\26\u02a2")
        buf.write("\u02a3\f\24\2\2\u02a3\u02a4\t\b\2\2\u02a4\u02d4\5b\62")
        buf.write("\25\u02a5\u02a6\f\23\2\2\u02a6\u02a7\7\'\2\2\u02a7\u02d4")
        buf.write("\5b\62\24\u02a8\u02a9\f\22\2\2\u02a9\u02aa\7(\2\2\u02aa")
        buf.write("\u02d4\5b\62\23\u02ab\u02ac\f\21\2\2\u02ac\u02ad\7)\2")
        buf.write("\2\u02ad\u02d4\5b\62\22\u02ae\u02af\f\20\2\2\u02af\u02b0")
        buf.write("\7*\2\2\u02b0\u02d4\5b\62\21\u02b1\u02b2\f\17\2\2\u02b2")
        buf.write("\u02b3\7+\2\2\u02b3\u02d4\5b\62\20\u02b4\u02b5\f\16\2")
        buf.write("\2\u02b5\u02b6\7\17\2\2\u02b6\u02b7\5b\62\2\u02b7\u02b8")
        buf.write("\7\20\2\2\u02b8\u02b9\5b\62\17\u02b9\u02d4\3\2\2\2\u02ba")
        buf.write("\u02bb\f\r\2\2\u02bb\u02bc\7\16\2\2\u02bc\u02d4\5b\62")
        buf.write("\16\u02bd\u02be\f\f\2\2\u02be\u02bf\5h\65\2\u02bf\u02c0")
        buf.write("\5b\62\r\u02c0\u02d4\3\2\2\2\u02c1\u02c2\f)\2\2\u02c2")
        buf.write("\u02c3\7\6\2\2\u02c3\u02c4\5`\61\2\u02c4\u02c5\7\7\2\2")
        buf.write("\u02c5\u02d4\3\2\2\2\u02c6\u02c7\f(\2\2\u02c7\u02c8\7")
        buf.write("\22\2\2\u02c8\u02d4\5n8\2\u02c9\u02ca\f\'\2\2\u02ca\u02d4")
        buf.write("\5\\/\2\u02cb\u02cc\f%\2\2\u02cc\u02cd\6\62\35\2\u02cd")
        buf.write("\u02d4\7\23\2\2\u02ce\u02cf\f$\2\2\u02cf\u02d0\6\62\37")
        buf.write("\2\u02d0\u02d4\7\24\2\2\u02d1\u02d2\f\13\2\2\u02d2\u02d4")
        buf.write("\7k\2\2\u02d3\u0290\3\2\2\2\u02d3\u0293\3\2\2\2\u02d3")
        buf.write("\u0296\3\2\2\2\u02d3\u0299\3\2\2\2\u02d3\u029c\3\2\2\2")
        buf.write("\u02d3\u029f\3\2\2\2\u02d3\u02a2\3\2\2\2\u02d3\u02a5\3")
        buf.write("\2\2\2\u02d3\u02a8\3\2\2\2\u02d3\u02ab\3\2\2\2\u02d3\u02ae")
        buf.write("\3\2\2\2\u02d3\u02b1\3\2\2\2\u02d3\u02b4\3\2\2\2\u02d3")
        buf.write("\u02ba\3\2\2\2\u02d3\u02bd\3\2\2\2\u02d3\u02c1\3\2\2\2")
        buf.write("\u02d3\u02c6\3\2\2\2\u02d3\u02c9\3\2\2\2\u02d3\u02cb\3")
        buf.write("\2\2\2\u02d3\u02ce\3\2\2\2\u02d3\u02d1\3\2\2\2\u02d4\u02d7")
        buf.write("\3\2\2\2\u02d5\u02d3\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6")
        buf.write("c\3\2\2\2\u02d7\u02d5\3\2\2\2\u02d8\u02df\7i\2\2\u02d9")
        buf.write("\u02db\7\b\2\2\u02da\u02dc\5F$\2\u02db\u02da\3\2\2\2\u02db")
        buf.write("\u02dc\3\2\2\2\u02dc\u02dd\3\2\2\2\u02dd\u02df\7\t\2\2")
        buf.write("\u02de\u02d8\3\2\2\2\u02de\u02d9\3\2\2\2\u02dfe\3\2\2")
        buf.write("\2\u02e0\u02e6\5b\62\2\u02e1\u02e2\7\n\2\2\u02e2\u02e3")
        buf.write("\5L\'\2\u02e3\u02e4\7\13\2\2\u02e4\u02e6\3\2\2\2\u02e5")
        buf.write("\u02e0\3\2\2\2\u02e5\u02e1\3\2\2\2\u02e6g\3\2\2\2\u02e7")
        buf.write("\u02e8\t\t\2\2\u02e8i\3\2\2\2\u02e9\u02f0\78\2\2\u02ea")
        buf.write("\u02f0\79\2\2\u02eb\u02f0\7j\2\2\u02ec\u02f0\7k\2\2\u02ed")
        buf.write("\u02f0\7\5\2\2\u02ee\u02f0\5l\67\2\u02ef\u02e9\3\2\2\2")
        buf.write("\u02ef\u02ea\3\2\2\2\u02ef\u02eb\3\2\2\2\u02ef\u02ec\3")
        buf.write("\2\2\2\u02ef\u02ed\3\2\2\2\u02ef\u02ee\3\2\2\2\u02f0k")
        buf.write("\3\2\2\2\u02f1\u02f2\t\n\2\2\u02f2m\3\2\2\2\u02f3\u02f6")
        buf.write("\7i\2\2\u02f4\u02f6\5p9\2\u02f5\u02f3\3\2\2\2\u02f5\u02f4")
        buf.write("\3\2\2\2\u02f6o\3\2\2\2\u02f7\u02fb\5r:\2\u02f8\u02fb")
        buf.write("\78\2\2\u02f9\u02fb\79\2\2\u02fa\u02f7\3\2\2\2\u02fa\u02f8")
        buf.write("\3\2\2\2\u02fa\u02f9\3\2\2\2\u02fbq\3\2\2\2\u02fc\u02fd")
        buf.write("\t\13\2\2\u02fds\3\2\2\2\u02fe\u02ff\7i\2\2\u02ff\u0300")
        buf.write("\6;!\2\u0300\u0301\5Z.\2\u0301u\3\2\2\2\u0302\u0303\7")
        buf.write("i\2\2\u0303\u0304\6<\"\2\u0304\u0305\5Z.\2\u0305w\3\2")
        buf.write("\2\2\u0306\u030b\7\f\2\2\u0307\u030b\7\2\2\3\u0308\u030b")
        buf.write("\6=#\2\u0309\u030b\6=$\2\u030a\u0306\3\2\2\2\u030a\u0307")
        buf.write("\3\2\2\2\u030a\u0308\3\2\2\2\u030a\u0309\3\2\2\2\u030b")
        buf.write("y\3\2\2\2M{\u0080\u0095\u0099\u00a0\u00ab\u00b1\u00b5")
        buf.write("\u00c4\u00d7\u00db\u00df\u00e9\u00ed\u00f8\u0105\u010b")
        buf.write("\u0112\u0119\u0120\u0132\u0136\u0138\u013f\u0145\u014a")
        buf.write("\u0159\u015c\u016e\u017b\u0181\u0189\u018d\u0192\u01a3")
        buf.write("\u01ab\u01ae\u01b3\u01bf\u01c4\u01c9\u01ce\u01d4\u01d9")
        buf.write("\u01df\u01e3\u01e8\u01f1\u01f6\u01fc\u01ff\u0202\u020d")
        buf.write("\u0210\u0213\u0232\u0237\u023f\u0244\u0247\u0253\u0259")
        buf.write("\u025d\u0266\u026c\u028e\u02d3\u02d5\u02db\u02de\u02e5")
        buf.write("\u02ef\u02f5\u02fa\u030a")
        return buf.getvalue()


class JavaScriptParser ( JavaScriptBaseParser ):

    grammarFileName = "JavaScriptParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "','", 
                     "'='", "'?'", "':'", "'...'", "'.'", "'++'", "'--'", 
                     "'+'", "'-'", "'~'", "'!'", "'*'", "'/'", "'%'", "'>>'", 
                     "'<<'", "'>>>'", "'<'", "'>'", "'<='", "'>='", "'=='", 
                     "'!='", "'==='", "'!=='", "'&'", "'^'", "'|'", "'&&'", 
                     "'||'", "'*='", "'/='", "'%='", "'+='", "'-='", "'<<='", 
                     "'>>='", "'>>>='", "'&='", "'^='", "'|='", "'=>'", 
                     "'null'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'break'", "'do'", "'instanceof'", 
                     "'typeof'", "'case'", "'else'", "'new'", "'var'", "'catch'", 
                     "'finally'", "'return'", "'void'", "'continue'", "'for'", 
                     "'switch'", "'while'", "'debugger'", "'function'", 
                     "'this'", "'with'", "'default'", "'if'", "'throw'", 
                     "'delete'", "'in'", "'try'", "'class'", "'enum'", "'extends'", 
                     "'super'", "'const'", "'export'", "'import'", "'implements'", 
                     "'let'", "'private'", "'public'", "'interface'", "'package'", 
                     "'protected'", "'static'", "'yield'" ]

    symbolicNames = [ "<INVALID>", "MultiLineComment", "SingleLineComment", 
                      "RegularExpressionLiteral", "OpenBracket", "CloseBracket", 
                      "OpenParen", "CloseParen", "OpenBrace", "CloseBrace", 
                      "SemiColon", "Comma", "Assign", "QuestionMark", "Colon", 
                      "Ellipsis", "Dot", "PlusPlus", "MinusMinus", "Plus", 
                      "Minus", "BitNot", "Not", "Multiply", "Divide", "Modulus", 
                      "RightShiftArithmetic", "LeftShiftArithmetic", "RightShiftLogical", 
                      "LessThan", "MoreThan", "LessThanEquals", "GreaterThanEquals", 
                      "Equals_", "NotEquals", "IdentityEquals", "IdentityNotEquals", 
                      "BitAnd", "BitXOr", "BitOr", "And", "Or", "MultiplyAssign", 
                      "DivideAssign", "ModulusAssign", "PlusAssign", "MinusAssign", 
                      "LeftShiftArithmeticAssign", "RightShiftArithmeticAssign", 
                      "RightShiftLogicalAssign", "BitAndAssign", "BitXorAssign", 
                      "BitOrAssign", "ARROW", "NullLiteral", "BooleanLiteral", 
                      "DecimalLiteral", "HexIntegerLiteral", "OctalIntegerLiteral", 
                      "OctalIntegerLiteral2", "BinaryIntegerLiteral", "Break", 
                      "Do", "Instanceof", "Typeof", "Case", "Else", "New", 
                      "Var", "Catch", "Finally", "Return", "Void", "Continue", 
                      "For", "Switch", "While", "Debugger", "Function", 
                      "This", "With", "Default", "If", "Throw", "Delete", 
                      "In", "Try", "Class", "Enum", "Extends", "Super", 
                      "Const", "Export", "Import", "Implements", "Let", 
                      "Private", "Public", "Interface", "Package", "Protected", 
                      "Static", "Yield", "Identifier", "StringLiteral", 
                      "TemplateStringLiteral", "WhiteSpaces", "LineTerminator", 
                      "HtmlComment", "CDataComment", "UnexpectedCharacter" ]

    RULE_program = 0
    RULE_sourceElement = 1
    RULE_statement = 2
    RULE_block = 3
    RULE_statementList = 4
    RULE_variableStatement = 5
    RULE_variableDeclarationList = 6
    RULE_variableDeclaration = 7
    RULE_emptyStatement = 8
    RULE_expressionStatement = 9
    RULE_ifStatement = 10
    RULE_iterationStatement = 11
    RULE_varModifier = 12
    RULE_continueStatement = 13
    RULE_breakStatement = 14
    RULE_returnStatement = 15
    RULE_withStatement = 16
    RULE_switchStatement = 17
    RULE_caseBlock = 18
    RULE_caseClauses = 19
    RULE_caseClause = 20
    RULE_defaultClause = 21
    RULE_labelledStatement = 22
    RULE_throwStatement = 23
    RULE_tryStatement = 24
    RULE_catchProduction = 25
    RULE_finallyProduction = 26
    RULE_debuggerStatement = 27
    RULE_functionDeclaration = 28
    RULE_classDeclaration = 29
    RULE_classTail = 30
    RULE_classElement = 31
    RULE_methodDefinition = 32
    RULE_generatorMethod = 33
    RULE_formalParameterList = 34
    RULE_formalParameterArg = 35
    RULE_lastFormalParameterArg = 36
    RULE_functionBody = 37
    RULE_sourceElements = 38
    RULE_arrayLiteral = 39
    RULE_elementList = 40
    RULE_lastElement = 41
    RULE_objectLiteral = 42
    RULE_propertyAssignment = 43
    RULE_propertyName = 44
    RULE_arguments = 45
    RULE_lastArgument = 46
    RULE_expressionSequence = 47
    RULE_singleExpression = 48
    RULE_arrowFunctionParameters = 49
    RULE_arrowFunctionBody = 50
    RULE_assignmentOperator = 51
    RULE_literal = 52
    RULE_numericLiteral = 53
    RULE_identifierName = 54
    RULE_reservedWord = 55
    RULE_keyword = 56
    RULE_getter = 57
    RULE_setter = 58
    RULE_eos = 59

    ruleNames =  [ "program", "sourceElement", "statement", "block", "statementList", 
                   "variableStatement", "variableDeclarationList", "variableDeclaration", 
                   "emptyStatement", "expressionStatement", "ifStatement", 
                   "iterationStatement", "varModifier", "continueStatement", 
                   "breakStatement", "returnStatement", "withStatement", 
                   "switchStatement", "caseBlock", "caseClauses", "caseClause", 
                   "defaultClause", "labelledStatement", "throwStatement", 
                   "tryStatement", "catchProduction", "finallyProduction", 
                   "debuggerStatement", "functionDeclaration", "classDeclaration", 
                   "classTail", "classElement", "methodDefinition", "generatorMethod", 
                   "formalParameterList", "formalParameterArg", "lastFormalParameterArg", 
                   "functionBody", "sourceElements", "arrayLiteral", "elementList", 
                   "lastElement", "objectLiteral", "propertyAssignment", 
                   "propertyName", "arguments", "lastArgument", "expressionSequence", 
                   "singleExpression", "arrowFunctionParameters", "arrowFunctionBody", 
                   "assignmentOperator", "literal", "numericLiteral", "identifierName", 
                   "reservedWord", "keyword", "getter", "setter", "eos" ]

    EOF = Token.EOF
    MultiLineComment=1
    SingleLineComment=2
    RegularExpressionLiteral=3
    OpenBracket=4
    CloseBracket=5
    OpenParen=6
    CloseParen=7
    OpenBrace=8
    CloseBrace=9
    SemiColon=10
    Comma=11
    Assign=12
    QuestionMark=13
    Colon=14
    Ellipsis=15
    Dot=16
    PlusPlus=17
    MinusMinus=18
    Plus=19
    Minus=20
    BitNot=21
    Not=22
    Multiply=23
    Divide=24
    Modulus=25
    RightShiftArithmetic=26
    LeftShiftArithmetic=27
    RightShiftLogical=28
    LessThan=29
    MoreThan=30
    LessThanEquals=31
    GreaterThanEquals=32
    Equals_=33
    NotEquals=34
    IdentityEquals=35
    IdentityNotEquals=36
    BitAnd=37
    BitXOr=38
    BitOr=39
    And=40
    Or=41
    MultiplyAssign=42
    DivideAssign=43
    ModulusAssign=44
    PlusAssign=45
    MinusAssign=46
    LeftShiftArithmeticAssign=47
    RightShiftArithmeticAssign=48
    RightShiftLogicalAssign=49
    BitAndAssign=50
    BitXorAssign=51
    BitOrAssign=52
    ARROW=53
    NullLiteral=54
    BooleanLiteral=55
    DecimalLiteral=56
    HexIntegerLiteral=57
    OctalIntegerLiteral=58
    OctalIntegerLiteral2=59
    BinaryIntegerLiteral=60
    Break=61
    Do=62
    Instanceof=63
    Typeof=64
    Case=65
    Else=66
    New=67
    Var=68
    Catch=69
    Finally=70
    Return=71
    Void=72
    Continue=73
    For=74
    Switch=75
    While=76
    Debugger=77
    Function=78
    This=79
    With=80
    Default=81
    If=82
    Throw=83
    Delete=84
    In=85
    Try=86
    Class=87
    Enum=88
    Extends=89
    Super=90
    Const=91
    Export=92
    Import=93
    Implements=94
    Let=95
    Private=96
    Public=97
    Interface=98
    Package=99
    Protected=100
    Static=101
    Yield=102
    Identifier=103
    StringLiteral=104
    TemplateStringLiteral=105
    WhiteSpaces=106
    LineTerminator=107
    HtmlComment=108
    CDataComment=109
    UnexpectedCharacter=110

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(JavaScriptParser.EOF, 0)

        def sourceElements(self):
            return self.getTypedRuleContext(JavaScriptParser.SourceElementsContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = JavaScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 120
                self.sourceElements()


            self.state = 123
            self.match(JavaScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SourceElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)


        def Export(self):
            return self.getToken(JavaScriptParser.Export, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_sourceElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceElement" ):
                listener.enterSourceElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceElement" ):
                listener.exitSourceElement(self)




    def sourceElement(self):

        localctx = JavaScriptParser.SourceElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sourceElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 125
                self.match(JavaScriptParser.Export)


            self.state = 128
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(JavaScriptParser.BlockContext,0)


        def variableStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.VariableStatementContext,0)


        def emptyStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.EmptyStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.IfStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.IterationStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.ContinueStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.BreakStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.ReturnStatementContext,0)


        def withStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.WithStatementContext,0)


        def labelledStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.LabelledStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.SwitchStatementContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.ThrowStatementContext,0)


        def tryStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.TryStatementContext,0)


        def debuggerStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.DebuggerStatementContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionDeclarationContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(JavaScriptParser.ClassDeclarationContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = JavaScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.variableStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.emptyStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.expressionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 134
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 135
                self.iterationStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 136
                self.continueStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 137
                self.breakStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 138
                self.returnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 139
                self.withStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 140
                self.labelledStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 141
                self.switchStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 142
                self.throwStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 143
                self.tryStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 144
                self.debuggerStatement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 145
                self.functionDeclaration()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 146
                self.classDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenBrace(self):
            return self.getToken(JavaScriptParser.OpenBrace, 0)

        def CloseBrace(self):
            return self.getToken(JavaScriptParser.CloseBrace, 0)

        def statementList(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = JavaScriptParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(JavaScriptParser.OpenBrace)
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 150
                self.statementList()


            self.state = 153
            self.match(JavaScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = JavaScriptParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statementList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 155
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 158 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varModifier(self):
            return self.getTypedRuleContext(JavaScriptParser.VarModifierContext,0)


        def variableDeclarationList(self):
            return self.getTypedRuleContext(JavaScriptParser.VariableDeclarationListContext,0)


        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_variableStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableStatement" ):
                listener.enterVariableStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableStatement" ):
                listener.exitVariableStatement(self)




    def variableStatement(self):

        localctx = JavaScriptParser.VariableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.varModifier()
            self.state = 161
            self.variableDeclarationList()
            self.state = 162
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.VariableDeclarationContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(JavaScriptParser.Comma)
            else:
                return self.getToken(JavaScriptParser.Comma, i)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_variableDeclarationList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarationList" ):
                listener.enterVariableDeclarationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarationList" ):
                listener.exitVariableDeclarationList(self)




    def variableDeclarationList(self):

        localctx = JavaScriptParser.VariableDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableDeclarationList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.variableDeclaration()
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 165
                    self.match(JavaScriptParser.Comma)
                    self.state = 166
                    self.variableDeclaration() 
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.ArrayLiteralContext,0)


        def objectLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.ObjectLiteralContext,0)


        def Assign(self):
            return self.getToken(JavaScriptParser.Assign, 0)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = JavaScriptParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.Identifier]:
                self.state = 172
                self.match(JavaScriptParser.Identifier)
                pass
            elif token in [JavaScriptParser.OpenBracket]:
                self.state = 173
                self.arrayLiteral()
                pass
            elif token in [JavaScriptParser.OpenBrace]:
                self.state = 174
                self.objectLiteral()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 177
                self.match(JavaScriptParser.Assign)
                self.state = 178
                self.singleExpression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SemiColon(self):
            return self.getToken(JavaScriptParser.SemiColon, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_emptyStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)




    def emptyStatement(self):

        localctx = JavaScriptParser.EmptyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(JavaScriptParser.SemiColon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = JavaScriptParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            if not self.notOpenBraceAndNotFunction():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self.notOpenBraceAndNotFunction()")
            self.state = 184
            self.expressionSequence()
            self.state = 185
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(JavaScriptParser.If, 0)

        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.StatementContext,i)


        def Else(self):
            return self.getToken(JavaScriptParser.Else, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = JavaScriptParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(JavaScriptParser.If)
            self.state = 188
            self.match(JavaScriptParser.OpenParen)
            self.state = 189
            self.expressionSequence()
            self.state = 190
            self.match(JavaScriptParser.CloseParen)
            self.state = 191
            self.statement()
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 192
                self.match(JavaScriptParser.Else)
                self.state = 193
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JavaScriptParser.RULE_iterationStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DoStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Do(self):
            return self.getToken(JavaScriptParser.Do, 0)
        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)

        def While(self):
            return self.getToken(JavaScriptParser.While, 0)
        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)

        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)
        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoStatement" ):
                listener.enterDoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoStatement" ):
                listener.exitDoStatement(self)


    class ForVarStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(JavaScriptParser.For, 0)
        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)
        def varModifier(self):
            return self.getTypedRuleContext(JavaScriptParser.VarModifierContext,0)

        def variableDeclarationList(self):
            return self.getTypedRuleContext(JavaScriptParser.VariableDeclarationListContext,0)

        def SemiColon(self, i:int=None):
            if i is None:
                return self.getTokens(JavaScriptParser.SemiColon)
            else:
                return self.getToken(JavaScriptParser.SemiColon, i)
        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)
        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)

        def expressionSequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForVarStatement" ):
                listener.enterForVarStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForVarStatement" ):
                listener.exitForVarStatement(self)


    class ForVarInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(JavaScriptParser.For, 0)
        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)
        def varModifier(self):
            return self.getTypedRuleContext(JavaScriptParser.VarModifierContext,0)

        def variableDeclaration(self):
            return self.getTypedRuleContext(JavaScriptParser.VariableDeclarationContext,0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)

        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)
        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)

        def In(self):
            return self.getToken(JavaScriptParser.In, 0)
        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForVarInStatement" ):
                listener.enterForVarInStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForVarInStatement" ):
                listener.exitForVarInStatement(self)


    class WhileStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def While(self):
            return self.getToken(JavaScriptParser.While, 0)
        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)

        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)
        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)


    class ForStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(JavaScriptParser.For, 0)
        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)
        def SemiColon(self, i:int=None):
            if i is None:
                return self.getTokens(JavaScriptParser.SemiColon)
            else:
                return self.getToken(JavaScriptParser.SemiColon, i)
        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)
        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)

        def expressionSequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)


    class ForInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(JavaScriptParser.For, 0)
        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)

        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)
        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)

        def In(self):
            return self.getToken(JavaScriptParser.In, 0)
        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInStatement" ):
                listener.enterForInStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInStatement" ):
                listener.exitForInStatement(self)



    def iterationStatement(self):

        localctx = JavaScriptParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = JavaScriptParser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(JavaScriptParser.Do)
                self.state = 197
                self.statement()
                self.state = 198
                self.match(JavaScriptParser.While)
                self.state = 199
                self.match(JavaScriptParser.OpenParen)
                self.state = 200
                self.expressionSequence()
                self.state = 201
                self.match(JavaScriptParser.CloseParen)
                self.state = 202
                self.eos()
                pass

            elif la_ == 2:
                localctx = JavaScriptParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(JavaScriptParser.While)
                self.state = 205
                self.match(JavaScriptParser.OpenParen)
                self.state = 206
                self.expressionSequence()
                self.state = 207
                self.match(JavaScriptParser.CloseParen)
                self.state = 208
                self.statement()
                pass

            elif la_ == 3:
                localctx = JavaScriptParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.match(JavaScriptParser.For)
                self.state = 211
                self.match(JavaScriptParser.OpenParen)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RegularExpressionLiteral) | (1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenParen) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.PlusPlus) | (1 << JavaScriptParser.MinusMinus) | (1 << JavaScriptParser.Plus) | (1 << JavaScriptParser.Minus) | (1 << JavaScriptParser.BitNot) | (1 << JavaScriptParser.Not) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (JavaScriptParser.Typeof - 64)) | (1 << (JavaScriptParser.New - 64)) | (1 << (JavaScriptParser.Void - 64)) | (1 << (JavaScriptParser.Function - 64)) | (1 << (JavaScriptParser.This - 64)) | (1 << (JavaScriptParser.Delete - 64)) | (1 << (JavaScriptParser.Class - 64)) | (1 << (JavaScriptParser.Super - 64)) | (1 << (JavaScriptParser.Identifier - 64)) | (1 << (JavaScriptParser.StringLiteral - 64)) | (1 << (JavaScriptParser.TemplateStringLiteral - 64)))) != 0):
                    self.state = 212
                    self.expressionSequence()


                self.state = 215
                self.match(JavaScriptParser.SemiColon)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RegularExpressionLiteral) | (1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenParen) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.PlusPlus) | (1 << JavaScriptParser.MinusMinus) | (1 << JavaScriptParser.Plus) | (1 << JavaScriptParser.Minus) | (1 << JavaScriptParser.BitNot) | (1 << JavaScriptParser.Not) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (JavaScriptParser.Typeof - 64)) | (1 << (JavaScriptParser.New - 64)) | (1 << (JavaScriptParser.Void - 64)) | (1 << (JavaScriptParser.Function - 64)) | (1 << (JavaScriptParser.This - 64)) | (1 << (JavaScriptParser.Delete - 64)) | (1 << (JavaScriptParser.Class - 64)) | (1 << (JavaScriptParser.Super - 64)) | (1 << (JavaScriptParser.Identifier - 64)) | (1 << (JavaScriptParser.StringLiteral - 64)) | (1 << (JavaScriptParser.TemplateStringLiteral - 64)))) != 0):
                    self.state = 216
                    self.expressionSequence()


                self.state = 219
                self.match(JavaScriptParser.SemiColon)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RegularExpressionLiteral) | (1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenParen) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.PlusPlus) | (1 << JavaScriptParser.MinusMinus) | (1 << JavaScriptParser.Plus) | (1 << JavaScriptParser.Minus) | (1 << JavaScriptParser.BitNot) | (1 << JavaScriptParser.Not) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (JavaScriptParser.Typeof - 64)) | (1 << (JavaScriptParser.New - 64)) | (1 << (JavaScriptParser.Void - 64)) | (1 << (JavaScriptParser.Function - 64)) | (1 << (JavaScriptParser.This - 64)) | (1 << (JavaScriptParser.Delete - 64)) | (1 << (JavaScriptParser.Class - 64)) | (1 << (JavaScriptParser.Super - 64)) | (1 << (JavaScriptParser.Identifier - 64)) | (1 << (JavaScriptParser.StringLiteral - 64)) | (1 << (JavaScriptParser.TemplateStringLiteral - 64)))) != 0):
                    self.state = 220
                    self.expressionSequence()


                self.state = 223
                self.match(JavaScriptParser.CloseParen)
                self.state = 224
                self.statement()
                pass

            elif la_ == 4:
                localctx = JavaScriptParser.ForVarStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.match(JavaScriptParser.For)
                self.state = 226
                self.match(JavaScriptParser.OpenParen)
                self.state = 227
                self.varModifier()
                self.state = 228
                self.variableDeclarationList()
                self.state = 229
                self.match(JavaScriptParser.SemiColon)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RegularExpressionLiteral) | (1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenParen) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.PlusPlus) | (1 << JavaScriptParser.MinusMinus) | (1 << JavaScriptParser.Plus) | (1 << JavaScriptParser.Minus) | (1 << JavaScriptParser.BitNot) | (1 << JavaScriptParser.Not) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (JavaScriptParser.Typeof - 64)) | (1 << (JavaScriptParser.New - 64)) | (1 << (JavaScriptParser.Void - 64)) | (1 << (JavaScriptParser.Function - 64)) | (1 << (JavaScriptParser.This - 64)) | (1 << (JavaScriptParser.Delete - 64)) | (1 << (JavaScriptParser.Class - 64)) | (1 << (JavaScriptParser.Super - 64)) | (1 << (JavaScriptParser.Identifier - 64)) | (1 << (JavaScriptParser.StringLiteral - 64)) | (1 << (JavaScriptParser.TemplateStringLiteral - 64)))) != 0):
                    self.state = 230
                    self.expressionSequence()


                self.state = 233
                self.match(JavaScriptParser.SemiColon)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RegularExpressionLiteral) | (1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenParen) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.PlusPlus) | (1 << JavaScriptParser.MinusMinus) | (1 << JavaScriptParser.Plus) | (1 << JavaScriptParser.Minus) | (1 << JavaScriptParser.BitNot) | (1 << JavaScriptParser.Not) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (JavaScriptParser.Typeof - 64)) | (1 << (JavaScriptParser.New - 64)) | (1 << (JavaScriptParser.Void - 64)) | (1 << (JavaScriptParser.Function - 64)) | (1 << (JavaScriptParser.This - 64)) | (1 << (JavaScriptParser.Delete - 64)) | (1 << (JavaScriptParser.Class - 64)) | (1 << (JavaScriptParser.Super - 64)) | (1 << (JavaScriptParser.Identifier - 64)) | (1 << (JavaScriptParser.StringLiteral - 64)) | (1 << (JavaScriptParser.TemplateStringLiteral - 64)))) != 0):
                    self.state = 234
                    self.expressionSequence()


                self.state = 237
                self.match(JavaScriptParser.CloseParen)
                self.state = 238
                self.statement()
                pass

            elif la_ == 5:
                localctx = JavaScriptParser.ForInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                self.match(JavaScriptParser.For)
                self.state = 241
                self.match(JavaScriptParser.OpenParen)
                self.state = 242
                self.singleExpression(0)
                self.state = 246
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [JavaScriptParser.In]:
                    self.state = 243
                    self.match(JavaScriptParser.In)
                    pass
                elif token in [JavaScriptParser.Identifier]:
                    self.state = 244
                    self.match(JavaScriptParser.Identifier)
                    self.state = 245
                    if not self.p("of"):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.p(\"of\")")
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 248
                self.expressionSequence()
                self.state = 249
                self.match(JavaScriptParser.CloseParen)
                self.state = 250
                self.statement()
                pass

            elif la_ == 6:
                localctx = JavaScriptParser.ForVarInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 252
                self.match(JavaScriptParser.For)
                self.state = 253
                self.match(JavaScriptParser.OpenParen)
                self.state = 254
                self.varModifier()
                self.state = 255
                self.variableDeclaration()
                self.state = 259
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [JavaScriptParser.In]:
                    self.state = 256
                    self.match(JavaScriptParser.In)
                    pass
                elif token in [JavaScriptParser.Identifier]:
                    self.state = 257
                    self.match(JavaScriptParser.Identifier)
                    self.state = 258
                    if not self.p("of"):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.p(\"of\")")
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 261
                self.expressionSequence()
                self.state = 262
                self.match(JavaScriptParser.CloseParen)
                self.state = 263
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarModifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Var(self):
            return self.getToken(JavaScriptParser.Var, 0)

        def Let(self):
            return self.getToken(JavaScriptParser.Let, 0)

        def Const(self):
            return self.getToken(JavaScriptParser.Const, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_varModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarModifier" ):
                listener.enterVarModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarModifier" ):
                listener.exitVarModifier(self)




    def varModifier(self):

        localctx = JavaScriptParser.VarModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_varModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            _la = self._input.LA(1)
            if not(((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (JavaScriptParser.Var - 68)) | (1 << (JavaScriptParser.Const - 68)) | (1 << (JavaScriptParser.Let - 68)))) != 0)):
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


    class ContinueStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(JavaScriptParser.Continue, 0)

        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)




    def continueStatement(self):

        localctx = JavaScriptParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(JavaScriptParser.Continue)
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 270
                if not self.notLineTerminator():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.notLineTerminator()")
                self.state = 271
                self.match(JavaScriptParser.Identifier)


            self.state = 274
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(JavaScriptParser.Break, 0)

        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)




    def breakStatement(self):

        localctx = JavaScriptParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(JavaScriptParser.Break)
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 277
                if not self.notLineTerminator():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.notLineTerminator()")
                self.state = 278
                self.match(JavaScriptParser.Identifier)


            self.state = 281
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(JavaScriptParser.Return, 0)

        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = JavaScriptParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(JavaScriptParser.Return)
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 284
                if not self.notLineTerminator():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.notLineTerminator()")
                self.state = 285
                self.expressionSequence()


            self.state = 288
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def With(self):
            return self.getToken(JavaScriptParser.With, 0)

        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)

        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_withStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithStatement" ):
                listener.enterWithStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithStatement" ):
                listener.exitWithStatement(self)




    def withStatement(self):

        localctx = JavaScriptParser.WithStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_withStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(JavaScriptParser.With)
            self.state = 291
            self.match(JavaScriptParser.OpenParen)
            self.state = 292
            self.expressionSequence()
            self.state = 293
            self.match(JavaScriptParser.CloseParen)
            self.state = 294
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Switch(self):
            return self.getToken(JavaScriptParser.Switch, 0)

        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)

        def caseBlock(self):
            return self.getTypedRuleContext(JavaScriptParser.CaseBlockContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)




    def switchStatement(self):

        localctx = JavaScriptParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_switchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(JavaScriptParser.Switch)
            self.state = 297
            self.match(JavaScriptParser.OpenParen)
            self.state = 298
            self.expressionSequence()
            self.state = 299
            self.match(JavaScriptParser.CloseParen)
            self.state = 300
            self.caseBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenBrace(self):
            return self.getToken(JavaScriptParser.OpenBrace, 0)

        def CloseBrace(self):
            return self.getToken(JavaScriptParser.CloseBrace, 0)

        def caseClauses(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.CaseClausesContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.CaseClausesContext,i)


        def defaultClause(self):
            return self.getTypedRuleContext(JavaScriptParser.DefaultClauseContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_caseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseBlock" ):
                listener.enterCaseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseBlock" ):
                listener.exitCaseBlock(self)




    def caseBlock(self):

        localctx = JavaScriptParser.CaseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_caseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(JavaScriptParser.OpenBrace)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaScriptParser.Case:
                self.state = 303
                self.caseClauses()


            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaScriptParser.Default:
                self.state = 306
                self.defaultClause()
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JavaScriptParser.Case:
                    self.state = 307
                    self.caseClauses()




            self.state = 312
            self.match(JavaScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseClausesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.CaseClauseContext,i)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_caseClauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseClauses" ):
                listener.enterCaseClauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseClauses" ):
                listener.exitCaseClauses(self)




    def caseClauses(self):

        localctx = JavaScriptParser.CaseClausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_caseClauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 314
                self.caseClause()
                self.state = 317 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==JavaScriptParser.Case):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Case(self):
            return self.getToken(JavaScriptParser.Case, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def Colon(self):
            return self.getToken(JavaScriptParser.Colon, 0)

        def statementList(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_caseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseClause" ):
                listener.enterCaseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseClause" ):
                listener.exitCaseClause(self)




    def caseClause(self):

        localctx = JavaScriptParser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_caseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(JavaScriptParser.Case)
            self.state = 320
            self.expressionSequence()
            self.state = 321
            self.match(JavaScriptParser.Colon)
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 322
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Default(self):
            return self.getToken(JavaScriptParser.Default, 0)

        def Colon(self):
            return self.getToken(JavaScriptParser.Colon, 0)

        def statementList(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_defaultClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultClause" ):
                listener.enterDefaultClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultClause" ):
                listener.exitDefaultClause(self)




    def defaultClause(self):

        localctx = JavaScriptParser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_defaultClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(JavaScriptParser.Default)
            self.state = 326
            self.match(JavaScriptParser.Colon)
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 327
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelledStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def Colon(self):
            return self.getToken(JavaScriptParser.Colon, 0)

        def statement(self):
            return self.getTypedRuleContext(JavaScriptParser.StatementContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_labelledStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelledStatement" ):
                listener.enterLabelledStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelledStatement" ):
                listener.exitLabelledStatement(self)




    def labelledStatement(self):

        localctx = JavaScriptParser.LabelledStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_labelledStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(JavaScriptParser.Identifier)
            self.state = 331
            self.match(JavaScriptParser.Colon)
            self.state = 332
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThrowStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Throw(self):
            return self.getToken(JavaScriptParser.Throw, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)


        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_throwStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowStatement" ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowStatement" ):
                listener.exitThrowStatement(self)




    def throwStatement(self):

        localctx = JavaScriptParser.ThrowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_throwStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(JavaScriptParser.Throw)
            self.state = 335
            if not self.notLineTerminator():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self.notLineTerminator()")
            self.state = 336
            self.expressionSequence()
            self.state = 337
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Try(self):
            return self.getToken(JavaScriptParser.Try, 0)

        def block(self):
            return self.getTypedRuleContext(JavaScriptParser.BlockContext,0)


        def catchProduction(self):
            return self.getTypedRuleContext(JavaScriptParser.CatchProductionContext,0)


        def finallyProduction(self):
            return self.getTypedRuleContext(JavaScriptParser.FinallyProductionContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_tryStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryStatement" ):
                listener.enterTryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryStatement" ):
                listener.exitTryStatement(self)




    def tryStatement(self):

        localctx = JavaScriptParser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_tryStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(JavaScriptParser.Try)
            self.state = 340
            self.block()
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.Catch]:
                self.state = 341
                self.catchProduction()
                self.state = 343
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 342
                    self.finallyProduction()


                pass
            elif token in [JavaScriptParser.Finally]:
                self.state = 345
                self.finallyProduction()
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


    class CatchProductionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Catch(self):
            return self.getToken(JavaScriptParser.Catch, 0)

        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)

        def block(self):
            return self.getTypedRuleContext(JavaScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_catchProduction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchProduction" ):
                listener.enterCatchProduction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchProduction" ):
                listener.exitCatchProduction(self)




    def catchProduction(self):

        localctx = JavaScriptParser.CatchProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_catchProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(JavaScriptParser.Catch)
            self.state = 349
            self.match(JavaScriptParser.OpenParen)
            self.state = 350
            self.match(JavaScriptParser.Identifier)
            self.state = 351
            self.match(JavaScriptParser.CloseParen)
            self.state = 352
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinallyProductionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Finally(self):
            return self.getToken(JavaScriptParser.Finally, 0)

        def block(self):
            return self.getTypedRuleContext(JavaScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_finallyProduction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinallyProduction" ):
                listener.enterFinallyProduction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinallyProduction" ):
                listener.exitFinallyProduction(self)




    def finallyProduction(self):

        localctx = JavaScriptParser.FinallyProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_finallyProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(JavaScriptParser.Finally)
            self.state = 355
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DebuggerStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Debugger(self):
            return self.getToken(JavaScriptParser.Debugger, 0)

        def eos(self):
            return self.getTypedRuleContext(JavaScriptParser.EosContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_debuggerStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDebuggerStatement" ):
                listener.enterDebuggerStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDebuggerStatement" ):
                listener.exitDebuggerStatement(self)




    def debuggerStatement(self):

        localctx = JavaScriptParser.DebuggerStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_debuggerStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(JavaScriptParser.Debugger)
            self.state = 358
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Function(self):
            return self.getToken(JavaScriptParser.Function, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)

        def OpenBrace(self):
            return self.getToken(JavaScriptParser.OpenBrace, 0)

        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)


        def CloseBrace(self):
            return self.getToken(JavaScriptParser.CloseBrace, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(JavaScriptParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = JavaScriptParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(JavaScriptParser.Function)
            self.state = 361
            self.match(JavaScriptParser.Identifier)
            self.state = 362
            self.match(JavaScriptParser.OpenParen)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis))) != 0) or _la==JavaScriptParser.Identifier:
                self.state = 363
                self.formalParameterList()


            self.state = 366
            self.match(JavaScriptParser.CloseParen)
            self.state = 367
            self.match(JavaScriptParser.OpenBrace)
            self.state = 368
            self.functionBody()
            self.state = 369
            self.match(JavaScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Class(self):
            return self.getToken(JavaScriptParser.Class, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def classTail(self):
            return self.getTypedRuleContext(JavaScriptParser.ClassTailContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)




    def classDeclaration(self):

        localctx = JavaScriptParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_classDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(JavaScriptParser.Class)
            self.state = 372
            self.match(JavaScriptParser.Identifier)
            self.state = 373
            self.classTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassTailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenBrace(self):
            return self.getToken(JavaScriptParser.OpenBrace, 0)

        def CloseBrace(self):
            return self.getToken(JavaScriptParser.CloseBrace, 0)

        def Extends(self):
            return self.getToken(JavaScriptParser.Extends, 0)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def classElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.ClassElementContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.ClassElementContext,i)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_classTail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassTail" ):
                listener.enterClassTail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassTail" ):
                listener.exitClassTail(self)




    def classTail(self):

        localctx = JavaScriptParser.ClassTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_classTail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaScriptParser.Extends:
                self.state = 375
                self.match(JavaScriptParser.Extends)
                self.state = 376
                self.singleExpression(0)


            self.state = 379
            self.match(JavaScriptParser.OpenBrace)
            self.state = 383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 380
                    self.classElement() 
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 386
            self.match(JavaScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDefinition(self):
            return self.getTypedRuleContext(JavaScriptParser.MethodDefinitionContext,0)


        def Static(self):
            return self.getToken(JavaScriptParser.Static, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def emptyStatement(self):
            return self.getTypedRuleContext(JavaScriptParser.EmptyStatementContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_classElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassElement" ):
                listener.enterClassElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassElement" ):
                listener.exitClassElement(self)




    def classElement(self):

        localctx = JavaScriptParser.ClassElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_classElement)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 388
                    self.match(JavaScriptParser.Static)

                elif la_ == 2:
                    self.state = 389
                    if not n("static"):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "n(\"static\")")
                    self.state = 390
                    self.match(JavaScriptParser.Identifier)


                self.state = 393
                self.methodDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.emptyStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def propertyName(self):
            return self.getTypedRuleContext(JavaScriptParser.PropertyNameContext,0)


        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)

        def OpenBrace(self):
            return self.getToken(JavaScriptParser.OpenBrace, 0)

        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)


        def CloseBrace(self):
            return self.getToken(JavaScriptParser.CloseBrace, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(JavaScriptParser.FormalParameterListContext,0)


        def getter(self):
            return self.getTypedRuleContext(JavaScriptParser.GetterContext,0)


        def setter(self):
            return self.getTypedRuleContext(JavaScriptParser.SetterContext,0)


        def generatorMethod(self):
            return self.getTypedRuleContext(JavaScriptParser.GeneratorMethodContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_methodDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDefinition" ):
                listener.enterMethodDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDefinition" ):
                listener.exitMethodDefinition(self)




    def methodDefinition(self):

        localctx = JavaScriptParser.MethodDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_methodDefinition)
        self._la = 0 # Token type
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.propertyName()
                self.state = 398
                self.match(JavaScriptParser.OpenParen)
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis))) != 0) or _la==JavaScriptParser.Identifier:
                    self.state = 399
                    self.formalParameterList()


                self.state = 402
                self.match(JavaScriptParser.CloseParen)
                self.state = 403
                self.match(JavaScriptParser.OpenBrace)
                self.state = 404
                self.functionBody()
                self.state = 405
                self.match(JavaScriptParser.CloseBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.getter()
                self.state = 408
                self.match(JavaScriptParser.OpenParen)
                self.state = 409
                self.match(JavaScriptParser.CloseParen)
                self.state = 410
                self.match(JavaScriptParser.OpenBrace)
                self.state = 411
                self.functionBody()
                self.state = 412
                self.match(JavaScriptParser.CloseBrace)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.setter()
                self.state = 415
                self.match(JavaScriptParser.OpenParen)
                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis))) != 0) or _la==JavaScriptParser.Identifier:
                    self.state = 416
                    self.formalParameterList()


                self.state = 419
                self.match(JavaScriptParser.CloseParen)
                self.state = 420
                self.match(JavaScriptParser.OpenBrace)
                self.state = 421
                self.functionBody()
                self.state = 422
                self.match(JavaScriptParser.CloseBrace)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 424
                self.generatorMethod()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeneratorMethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)

        def OpenBrace(self):
            return self.getToken(JavaScriptParser.OpenBrace, 0)

        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)


        def CloseBrace(self):
            return self.getToken(JavaScriptParser.CloseBrace, 0)

        def Multiply(self):
            return self.getToken(JavaScriptParser.Multiply, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(JavaScriptParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_generatorMethod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneratorMethod" ):
                listener.enterGeneratorMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneratorMethod" ):
                listener.exitGeneratorMethod(self)




    def generatorMethod(self):

        localctx = JavaScriptParser.GeneratorMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_generatorMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaScriptParser.Multiply:
                self.state = 427
                self.match(JavaScriptParser.Multiply)


            self.state = 430
            self.match(JavaScriptParser.Identifier)
            self.state = 431
            self.match(JavaScriptParser.OpenParen)
            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis))) != 0) or _la==JavaScriptParser.Identifier:
                self.state = 432
                self.formalParameterList()


            self.state = 435
            self.match(JavaScriptParser.CloseParen)
            self.state = 436
            self.match(JavaScriptParser.OpenBrace)
            self.state = 437
            self.functionBody()
            self.state = 438
            self.match(JavaScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formalParameterArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.FormalParameterArgContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.FormalParameterArgContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(JavaScriptParser.Comma)
            else:
                return self.getToken(JavaScriptParser.Comma, i)

        def lastFormalParameterArg(self):
            return self.getTypedRuleContext(JavaScriptParser.LastFormalParameterArgContext,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.ArrayLiteralContext,0)


        def objectLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.ObjectLiteralContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_formalParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterList" ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterList" ):
                listener.exitFormalParameterList(self)




    def formalParameterList(self):

        localctx = JavaScriptParser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.formalParameterArg()
                self.state = 445
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 441
                        self.match(JavaScriptParser.Comma)
                        self.state = 442
                        self.formalParameterArg() 
                    self.state = 447
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

                self.state = 450
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JavaScriptParser.Comma:
                    self.state = 448
                    self.match(JavaScriptParser.Comma)
                    self.state = 449
                    self.lastFormalParameterArg()


                pass
            elif token in [JavaScriptParser.Ellipsis]:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.lastFormalParameterArg()
                pass
            elif token in [JavaScriptParser.OpenBracket]:
                self.enterOuterAlt(localctx, 3)
                self.state = 453
                self.arrayLiteral()
                pass
            elif token in [JavaScriptParser.OpenBrace]:
                self.enterOuterAlt(localctx, 4)
                self.state = 454
                self.objectLiteral()
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


    class FormalParameterArgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def Assign(self):
            return self.getToken(JavaScriptParser.Assign, 0)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_formalParameterArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterArg" ):
                listener.enterFormalParameterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterArg" ):
                listener.exitFormalParameterArg(self)




    def formalParameterArg(self):

        localctx = JavaScriptParser.FormalParameterArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_formalParameterArg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(JavaScriptParser.Identifier)
            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaScriptParser.Assign:
                self.state = 458
                self.match(JavaScriptParser.Assign)
                self.state = 459
                self.singleExpression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LastFormalParameterArgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ellipsis(self):
            return self.getToken(JavaScriptParser.Ellipsis, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_lastFormalParameterArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLastFormalParameterArg" ):
                listener.enterLastFormalParameterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLastFormalParameterArg" ):
                listener.exitLastFormalParameterArg(self)




    def lastFormalParameterArg(self):

        localctx = JavaScriptParser.LastFormalParameterArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_lastFormalParameterArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(JavaScriptParser.Ellipsis)
            self.state = 463
            self.match(JavaScriptParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sourceElements(self):
            return self.getTypedRuleContext(JavaScriptParser.SourceElementsContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_functionBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBody" ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBody" ):
                listener.exitFunctionBody(self)




    def functionBody(self):

        localctx = JavaScriptParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_functionBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 465
                self.sourceElements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SourceElementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sourceElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SourceElementContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SourceElementContext,i)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_sourceElements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceElements" ):
                listener.enterSourceElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceElements" ):
                listener.exitSourceElements(self)




    def sourceElements(self):

        localctx = JavaScriptParser.SourceElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_sourceElements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 468
                    self.sourceElement()

                else:
                    raise NoViableAltException(self)
                self.state = 471 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenBracket(self):
            return self.getToken(JavaScriptParser.OpenBracket, 0)

        def CloseBracket(self):
            return self.getToken(JavaScriptParser.CloseBracket, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(JavaScriptParser.Comma)
            else:
                return self.getToken(JavaScriptParser.Comma, i)

        def elementList(self):
            return self.getTypedRuleContext(JavaScriptParser.ElementListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)




    def arrayLiteral(self):

        localctx = JavaScriptParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(JavaScriptParser.OpenBracket)
            self.state = 477
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 474
                    self.match(JavaScriptParser.Comma) 
                self.state = 479
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RegularExpressionLiteral) | (1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenParen) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis) | (1 << JavaScriptParser.PlusPlus) | (1 << JavaScriptParser.MinusMinus) | (1 << JavaScriptParser.Plus) | (1 << JavaScriptParser.Minus) | (1 << JavaScriptParser.BitNot) | (1 << JavaScriptParser.Not) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (JavaScriptParser.Typeof - 64)) | (1 << (JavaScriptParser.New - 64)) | (1 << (JavaScriptParser.Void - 64)) | (1 << (JavaScriptParser.Function - 64)) | (1 << (JavaScriptParser.This - 64)) | (1 << (JavaScriptParser.Delete - 64)) | (1 << (JavaScriptParser.Class - 64)) | (1 << (JavaScriptParser.Super - 64)) | (1 << (JavaScriptParser.Identifier - 64)) | (1 << (JavaScriptParser.StringLiteral - 64)) | (1 << (JavaScriptParser.TemplateStringLiteral - 64)))) != 0):
                self.state = 480
                self.elementList()


            self.state = 486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JavaScriptParser.Comma:
                self.state = 483
                self.match(JavaScriptParser.Comma)
                self.state = 488
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 489
            self.match(JavaScriptParser.CloseBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def lastElement(self):
            return self.getTypedRuleContext(JavaScriptParser.LastElementContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(JavaScriptParser.Comma)
            else:
                return self.getToken(JavaScriptParser.Comma, i)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_elementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementList" ):
                listener.enterElementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementList" ):
                listener.exitElementList(self)




    def elementList(self):

        localctx = JavaScriptParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_elementList)
        self._la = 0 # Token type
        try:
            self.state = 512
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.RegularExpressionLiteral, JavaScriptParser.OpenBracket, JavaScriptParser.OpenParen, JavaScriptParser.OpenBrace, JavaScriptParser.PlusPlus, JavaScriptParser.MinusMinus, JavaScriptParser.Plus, JavaScriptParser.Minus, JavaScriptParser.BitNot, JavaScriptParser.Not, JavaScriptParser.NullLiteral, JavaScriptParser.BooleanLiteral, JavaScriptParser.DecimalLiteral, JavaScriptParser.HexIntegerLiteral, JavaScriptParser.OctalIntegerLiteral, JavaScriptParser.OctalIntegerLiteral2, JavaScriptParser.BinaryIntegerLiteral, JavaScriptParser.Typeof, JavaScriptParser.New, JavaScriptParser.Void, JavaScriptParser.Function, JavaScriptParser.This, JavaScriptParser.Delete, JavaScriptParser.Class, JavaScriptParser.Super, JavaScriptParser.Identifier, JavaScriptParser.StringLiteral, JavaScriptParser.TemplateStringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.singleExpression(0)
                self.state = 500
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 493 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 492
                            self.match(JavaScriptParser.Comma)
                            self.state = 495 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==JavaScriptParser.Comma):
                                break

                        self.state = 497
                        self.singleExpression(0) 
                    self.state = 502
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

                self.state = 509
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 504 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 503
                        self.match(JavaScriptParser.Comma)
                        self.state = 506 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==JavaScriptParser.Comma):
                            break

                    self.state = 508
                    self.lastElement()


                pass
            elif token in [JavaScriptParser.Ellipsis]:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
                self.lastElement()
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


    class LastElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ellipsis(self):
            return self.getToken(JavaScriptParser.Ellipsis, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_lastElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLastElement" ):
                listener.enterLastElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLastElement" ):
                listener.exitLastElement(self)




    def lastElement(self):

        localctx = JavaScriptParser.LastElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_lastElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(JavaScriptParser.Ellipsis)
            self.state = 515
            self.match(JavaScriptParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenBrace(self):
            return self.getToken(JavaScriptParser.OpenBrace, 0)

        def CloseBrace(self):
            return self.getToken(JavaScriptParser.CloseBrace, 0)

        def propertyAssignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.PropertyAssignmentContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.PropertyAssignmentContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(JavaScriptParser.Comma)
            else:
                return self.getToken(JavaScriptParser.Comma, i)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_objectLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectLiteral" ):
                listener.enterObjectLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectLiteral" ):
                listener.exitObjectLiteral(self)




    def objectLiteral(self):

        localctx = JavaScriptParser.ObjectLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_objectLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(JavaScriptParser.OpenBrace)
            self.state = 526
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.Multiply) | (1 << JavaScriptParser.NullLiteral) | (1 << JavaScriptParser.BooleanLiteral) | (1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral) | (1 << JavaScriptParser.Break) | (1 << JavaScriptParser.Do) | (1 << JavaScriptParser.Instanceof))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (JavaScriptParser.Typeof - 64)) | (1 << (JavaScriptParser.Case - 64)) | (1 << (JavaScriptParser.Else - 64)) | (1 << (JavaScriptParser.New - 64)) | (1 << (JavaScriptParser.Var - 64)) | (1 << (JavaScriptParser.Catch - 64)) | (1 << (JavaScriptParser.Finally - 64)) | (1 << (JavaScriptParser.Return - 64)) | (1 << (JavaScriptParser.Void - 64)) | (1 << (JavaScriptParser.Continue - 64)) | (1 << (JavaScriptParser.For - 64)) | (1 << (JavaScriptParser.Switch - 64)) | (1 << (JavaScriptParser.While - 64)) | (1 << (JavaScriptParser.Debugger - 64)) | (1 << (JavaScriptParser.Function - 64)) | (1 << (JavaScriptParser.This - 64)) | (1 << (JavaScriptParser.With - 64)) | (1 << (JavaScriptParser.Default - 64)) | (1 << (JavaScriptParser.If - 64)) | (1 << (JavaScriptParser.Throw - 64)) | (1 << (JavaScriptParser.Delete - 64)) | (1 << (JavaScriptParser.In - 64)) | (1 << (JavaScriptParser.Try - 64)) | (1 << (JavaScriptParser.Class - 64)) | (1 << (JavaScriptParser.Enum - 64)) | (1 << (JavaScriptParser.Extends - 64)) | (1 << (JavaScriptParser.Super - 64)) | (1 << (JavaScriptParser.Const - 64)) | (1 << (JavaScriptParser.Export - 64)) | (1 << (JavaScriptParser.Import - 64)) | (1 << (JavaScriptParser.Implements - 64)) | (1 << (JavaScriptParser.Let - 64)) | (1 << (JavaScriptParser.Private - 64)) | (1 << (JavaScriptParser.Public - 64)) | (1 << (JavaScriptParser.Interface - 64)) | (1 << (JavaScriptParser.Package - 64)) | (1 << (JavaScriptParser.Protected - 64)) | (1 << (JavaScriptParser.Static - 64)) | (1 << (JavaScriptParser.Yield - 64)) | (1 << (JavaScriptParser.Identifier - 64)) | (1 << (JavaScriptParser.StringLiteral - 64)))) != 0):
                self.state = 518
                self.propertyAssignment()
                self.state = 523
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 519
                        self.match(JavaScriptParser.Comma)
                        self.state = 520
                        self.propertyAssignment() 
                    self.state = 525
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,52,self._ctx)



            self.state = 529
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JavaScriptParser.Comma:
                self.state = 528
                self.match(JavaScriptParser.Comma)


            self.state = 531
            self.match(JavaScriptParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JavaScriptParser.RULE_propertyAssignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PropertyExpressionAssignmentContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def propertyName(self):
            return self.getTypedRuleContext(JavaScriptParser.PropertyNameContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def Colon(self):
            return self.getToken(JavaScriptParser.Colon, 0)
        def Assign(self):
            return self.getToken(JavaScriptParser.Assign, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyExpressionAssignment" ):
                listener.enterPropertyExpressionAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyExpressionAssignment" ):
                listener.exitPropertyExpressionAssignment(self)


    class ComputedPropertyExpressionAssignmentContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OpenBracket(self):
            return self.getToken(JavaScriptParser.OpenBracket, 0)
        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def CloseBracket(self):
            return self.getToken(JavaScriptParser.CloseBracket, 0)
        def Colon(self):
            return self.getToken(JavaScriptParser.Colon, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComputedPropertyExpressionAssignment" ):
                listener.enterComputedPropertyExpressionAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComputedPropertyExpressionAssignment" ):
                listener.exitComputedPropertyExpressionAssignment(self)


    class PropertyShorthandContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyShorthand" ):
                listener.enterPropertyShorthand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyShorthand" ):
                listener.exitPropertyShorthand(self)


    class PropertySetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def setter(self):
            return self.getTypedRuleContext(JavaScriptParser.SetterContext,0)

        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)
        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)
        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)
        def OpenBrace(self):
            return self.getToken(JavaScriptParser.OpenBrace, 0)
        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)

        def CloseBrace(self):
            return self.getToken(JavaScriptParser.CloseBrace, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertySetter" ):
                listener.enterPropertySetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertySetter" ):
                listener.exitPropertySetter(self)


    class PropertyGetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def getter(self):
            return self.getTypedRuleContext(JavaScriptParser.GetterContext,0)

        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)
        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)
        def OpenBrace(self):
            return self.getToken(JavaScriptParser.OpenBrace, 0)
        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)

        def CloseBrace(self):
            return self.getToken(JavaScriptParser.CloseBrace, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyGetter" ):
                listener.enterPropertyGetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyGetter" ):
                listener.exitPropertyGetter(self)


    class MethodPropertyContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def generatorMethod(self):
            return self.getTypedRuleContext(JavaScriptParser.GeneratorMethodContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodProperty" ):
                listener.enterMethodProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodProperty" ):
                listener.exitMethodProperty(self)



    def propertyAssignment(self):

        localctx = JavaScriptParser.PropertyAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_propertyAssignment)
        self._la = 0 # Token type
        try:
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                localctx = JavaScriptParser.PropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.propertyName()
                self.state = 534
                _la = self._input.LA(1)
                if not(_la==JavaScriptParser.Assign or _la==JavaScriptParser.Colon):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 535
                self.singleExpression(0)
                pass

            elif la_ == 2:
                localctx = JavaScriptParser.ComputedPropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 537
                self.match(JavaScriptParser.OpenBracket)
                self.state = 538
                self.singleExpression(0)
                self.state = 539
                self.match(JavaScriptParser.CloseBracket)
                self.state = 540
                self.match(JavaScriptParser.Colon)
                self.state = 541
                self.singleExpression(0)
                pass

            elif la_ == 3:
                localctx = JavaScriptParser.PropertyGetterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 543
                self.getter()
                self.state = 544
                self.match(JavaScriptParser.OpenParen)
                self.state = 545
                self.match(JavaScriptParser.CloseParen)
                self.state = 546
                self.match(JavaScriptParser.OpenBrace)
                self.state = 547
                self.functionBody()
                self.state = 548
                self.match(JavaScriptParser.CloseBrace)
                pass

            elif la_ == 4:
                localctx = JavaScriptParser.PropertySetterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 550
                self.setter()
                self.state = 551
                self.match(JavaScriptParser.OpenParen)
                self.state = 552
                self.match(JavaScriptParser.Identifier)
                self.state = 553
                self.match(JavaScriptParser.CloseParen)
                self.state = 554
                self.match(JavaScriptParser.OpenBrace)
                self.state = 555
                self.functionBody()
                self.state = 556
                self.match(JavaScriptParser.CloseBrace)
                pass

            elif la_ == 5:
                localctx = JavaScriptParser.MethodPropertyContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 558
                self.generatorMethod()
                pass

            elif la_ == 6:
                localctx = JavaScriptParser.PropertyShorthandContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 559
                self.match(JavaScriptParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierName(self):
            return self.getTypedRuleContext(JavaScriptParser.IdentifierNameContext,0)


        def StringLiteral(self):
            return self.getToken(JavaScriptParser.StringLiteral, 0)

        def numericLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.NumericLiteralContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_propertyName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyName" ):
                listener.enterPropertyName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyName" ):
                listener.exitPropertyName(self)




    def propertyName(self):

        localctx = JavaScriptParser.PropertyNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_propertyName)
        try:
            self.state = 565
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.NullLiteral, JavaScriptParser.BooleanLiteral, JavaScriptParser.Break, JavaScriptParser.Do, JavaScriptParser.Instanceof, JavaScriptParser.Typeof, JavaScriptParser.Case, JavaScriptParser.Else, JavaScriptParser.New, JavaScriptParser.Var, JavaScriptParser.Catch, JavaScriptParser.Finally, JavaScriptParser.Return, JavaScriptParser.Void, JavaScriptParser.Continue, JavaScriptParser.For, JavaScriptParser.Switch, JavaScriptParser.While, JavaScriptParser.Debugger, JavaScriptParser.Function, JavaScriptParser.This, JavaScriptParser.With, JavaScriptParser.Default, JavaScriptParser.If, JavaScriptParser.Throw, JavaScriptParser.Delete, JavaScriptParser.In, JavaScriptParser.Try, JavaScriptParser.Class, JavaScriptParser.Enum, JavaScriptParser.Extends, JavaScriptParser.Super, JavaScriptParser.Const, JavaScriptParser.Export, JavaScriptParser.Import, JavaScriptParser.Implements, JavaScriptParser.Let, JavaScriptParser.Private, JavaScriptParser.Public, JavaScriptParser.Interface, JavaScriptParser.Package, JavaScriptParser.Protected, JavaScriptParser.Static, JavaScriptParser.Yield, JavaScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 562
                self.identifierName()
                pass
            elif token in [JavaScriptParser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 563
                self.match(JavaScriptParser.StringLiteral)
                pass
            elif token in [JavaScriptParser.DecimalLiteral, JavaScriptParser.HexIntegerLiteral, JavaScriptParser.OctalIntegerLiteral, JavaScriptParser.OctalIntegerLiteral2, JavaScriptParser.BinaryIntegerLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 564
                self.numericLiteral()
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


    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def lastArgument(self):
            return self.getTypedRuleContext(JavaScriptParser.LastArgumentContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(JavaScriptParser.Comma)
            else:
                return self.getToken(JavaScriptParser.Comma, i)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = JavaScriptParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.match(JavaScriptParser.OpenParen)
            self.state = 581
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.RegularExpressionLiteral, JavaScriptParser.OpenBracket, JavaScriptParser.OpenParen, JavaScriptParser.OpenBrace, JavaScriptParser.PlusPlus, JavaScriptParser.MinusMinus, JavaScriptParser.Plus, JavaScriptParser.Minus, JavaScriptParser.BitNot, JavaScriptParser.Not, JavaScriptParser.NullLiteral, JavaScriptParser.BooleanLiteral, JavaScriptParser.DecimalLiteral, JavaScriptParser.HexIntegerLiteral, JavaScriptParser.OctalIntegerLiteral, JavaScriptParser.OctalIntegerLiteral2, JavaScriptParser.BinaryIntegerLiteral, JavaScriptParser.Typeof, JavaScriptParser.New, JavaScriptParser.Void, JavaScriptParser.Function, JavaScriptParser.This, JavaScriptParser.Delete, JavaScriptParser.Class, JavaScriptParser.Super, JavaScriptParser.Identifier, JavaScriptParser.StringLiteral, JavaScriptParser.TemplateStringLiteral]:
                self.state = 568
                self.singleExpression(0)
                self.state = 573
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 569
                        self.match(JavaScriptParser.Comma)
                        self.state = 570
                        self.singleExpression(0) 
                    self.state = 575
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

                self.state = 578
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JavaScriptParser.Comma:
                    self.state = 576
                    self.match(JavaScriptParser.Comma)
                    self.state = 577
                    self.lastArgument()


                pass
            elif token in [JavaScriptParser.Ellipsis]:
                self.state = 580
                self.lastArgument()
                pass
            elif token in [JavaScriptParser.CloseParen]:
                pass
            else:
                pass
            self.state = 583
            self.match(JavaScriptParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LastArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ellipsis(self):
            return self.getToken(JavaScriptParser.Ellipsis, 0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_lastArgument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLastArgument" ):
                listener.enterLastArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLastArgument" ):
                listener.exitLastArgument(self)




    def lastArgument(self):

        localctx = JavaScriptParser.LastArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_lastArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.match(JavaScriptParser.Ellipsis)
            self.state = 586
            self.match(JavaScriptParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionSequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(JavaScriptParser.Comma)
            else:
                return self.getToken(JavaScriptParser.Comma, i)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_expressionSequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionSequence" ):
                listener.enterExpressionSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionSequence" ):
                listener.exitExpressionSequence(self)




    def expressionSequence(self):

        localctx = JavaScriptParser.ExpressionSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expressionSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.singleExpression(0)
            self.state = 593
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 589
                    self.match(JavaScriptParser.Comma)
                    self.state = 590
                    self.singleExpression(0) 
                self.state = 595
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JavaScriptParser.RULE_singleExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TemplateStringExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def TemplateStringLiteral(self):
            return self.getToken(JavaScriptParser.TemplateStringLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateStringExpression" ):
                listener.enterTemplateStringExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateStringExpression" ):
                listener.exitTemplateStringExpression(self)


    class TernaryExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def QuestionMark(self):
            return self.getToken(JavaScriptParser.QuestionMark, 0)
        def Colon(self):
            return self.getToken(JavaScriptParser.Colon, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernaryExpression" ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernaryExpression" ):
                listener.exitTernaryExpression(self)


    class LogicalAndExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def And(self):
            return self.getToken(JavaScriptParser.And, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)


    class PreIncrementExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PlusPlus(self):
            return self.getToken(JavaScriptParser.PlusPlus, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreIncrementExpression" ):
                listener.enterPreIncrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreIncrementExpression" ):
                listener.exitPreIncrementExpression(self)


    class ObjectLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def objectLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.ObjectLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectLiteralExpression" ):
                listener.enterObjectLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectLiteralExpression" ):
                listener.exitObjectLiteralExpression(self)


    class InExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def In(self):
            return self.getToken(JavaScriptParser.In, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInExpression" ):
                listener.enterInExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInExpression" ):
                listener.exitInExpression(self)


    class LogicalOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def Or(self):
            return self.getToken(JavaScriptParser.Or, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)


    class NotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Not(self):
            return self.getToken(JavaScriptParser.Not, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)


    class PreDecreaseExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MinusMinus(self):
            return self.getToken(JavaScriptParser.MinusMinus, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreDecreaseExpression" ):
                listener.enterPreDecreaseExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreDecreaseExpression" ):
                listener.exitPreDecreaseExpression(self)


    class ArgumentsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def arguments(self):
            return self.getTypedRuleContext(JavaScriptParser.ArgumentsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentsExpression" ):
                listener.enterArgumentsExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentsExpression" ):
                listener.exitArgumentsExpression(self)


    class ThisExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def This(self):
            return self.getToken(JavaScriptParser.This, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThisExpression" ):
                listener.enterThisExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThisExpression" ):
                listener.exitThisExpression(self)


    class FunctionExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Function(self):
            return self.getToken(JavaScriptParser.Function, 0)
        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)
        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)
        def OpenBrace(self):
            return self.getToken(JavaScriptParser.OpenBrace, 0)
        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)

        def CloseBrace(self):
            return self.getToken(JavaScriptParser.CloseBrace, 0)
        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)
        def formalParameterList(self):
            return self.getTypedRuleContext(JavaScriptParser.FormalParameterListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpression" ):
                listener.enterFunctionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpression" ):
                listener.exitFunctionExpression(self)


    class UnaryMinusExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Minus(self):
            return self.getToken(JavaScriptParser.Minus, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpression" ):
                listener.enterUnaryMinusExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpression" ):
                listener.exitUnaryMinusExpression(self)


    class AssignmentExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def Assign(self):
            return self.getToken(JavaScriptParser.Assign, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpression" ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpression" ):
                listener.exitAssignmentExpression(self)


    class PostDecreaseExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def MinusMinus(self):
            return self.getToken(JavaScriptParser.MinusMinus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostDecreaseExpression" ):
                listener.enterPostDecreaseExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostDecreaseExpression" ):
                listener.exitPostDecreaseExpression(self)


    class TypeofExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Typeof(self):
            return self.getToken(JavaScriptParser.Typeof, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeofExpression" ):
                listener.enterTypeofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeofExpression" ):
                listener.exitTypeofExpression(self)


    class InstanceofExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def Instanceof(self):
            return self.getToken(JavaScriptParser.Instanceof, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceofExpression" ):
                listener.enterInstanceofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceofExpression" ):
                listener.exitInstanceofExpression(self)


    class UnaryPlusExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Plus(self):
            return self.getToken(JavaScriptParser.Plus, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryPlusExpression" ):
                listener.enterUnaryPlusExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryPlusExpression" ):
                listener.exitUnaryPlusExpression(self)


    class DeleteExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Delete(self):
            return self.getToken(JavaScriptParser.Delete, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteExpression" ):
                listener.enterDeleteExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteExpression" ):
                listener.exitDeleteExpression(self)


    class ArrowFunctionExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrowFunctionParameters(self):
            return self.getTypedRuleContext(JavaScriptParser.ArrowFunctionParametersContext,0)

        def ARROW(self):
            return self.getToken(JavaScriptParser.ARROW, 0)
        def arrowFunctionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.ArrowFunctionBodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrowFunctionExpression" ):
                listener.enterArrowFunctionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrowFunctionExpression" ):
                listener.exitArrowFunctionExpression(self)


    class EqualityExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def Equals_(self):
            return self.getToken(JavaScriptParser.Equals_, 0)
        def NotEquals(self):
            return self.getToken(JavaScriptParser.NotEquals, 0)
        def IdentityEquals(self):
            return self.getToken(JavaScriptParser.IdentityEquals, 0)
        def IdentityNotEquals(self):
            return self.getToken(JavaScriptParser.IdentityNotEquals, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)


    class BitXOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def BitXOr(self):
            return self.getToken(JavaScriptParser.BitXOr, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitXOrExpression" ):
                listener.enterBitXOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitXOrExpression" ):
                listener.exitBitXOrExpression(self)


    class SuperExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Super(self):
            return self.getToken(JavaScriptParser.Super, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperExpression" ):
                listener.enterSuperExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperExpression" ):
                listener.exitSuperExpression(self)


    class MultiplicativeExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def Multiply(self):
            return self.getToken(JavaScriptParser.Multiply, 0)
        def Divide(self):
            return self.getToken(JavaScriptParser.Divide, 0)
        def Modulus(self):
            return self.getToken(JavaScriptParser.Modulus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)


    class BitShiftExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def LeftShiftArithmetic(self):
            return self.getToken(JavaScriptParser.LeftShiftArithmetic, 0)
        def RightShiftArithmetic(self):
            return self.getToken(JavaScriptParser.RightShiftArithmetic, 0)
        def RightShiftLogical(self):
            return self.getToken(JavaScriptParser.RightShiftLogical, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitShiftExpression" ):
                listener.enterBitShiftExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitShiftExpression" ):
                listener.exitBitShiftExpression(self)


    class ParenthesizedExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)

        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedExpression" ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedExpression" ):
                listener.exitParenthesizedExpression(self)


    class AdditiveExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def Plus(self):
            return self.getToken(JavaScriptParser.Plus, 0)
        def Minus(self):
            return self.getToken(JavaScriptParser.Minus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)


    class RelationalExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def LessThan(self):
            return self.getToken(JavaScriptParser.LessThan, 0)
        def MoreThan(self):
            return self.getToken(JavaScriptParser.MoreThan, 0)
        def LessThanEquals(self):
            return self.getToken(JavaScriptParser.LessThanEquals, 0)
        def GreaterThanEquals(self):
            return self.getToken(JavaScriptParser.GreaterThanEquals, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)


    class PostIncrementExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def PlusPlus(self):
            return self.getToken(JavaScriptParser.PlusPlus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostIncrementExpression" ):
                listener.enterPostIncrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostIncrementExpression" ):
                listener.exitPostIncrementExpression(self)


    class BitNotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BitNot(self):
            return self.getToken(JavaScriptParser.BitNot, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitNotExpression" ):
                listener.enterBitNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitNotExpression" ):
                listener.exitBitNotExpression(self)


    class NewExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def New(self):
            return self.getToken(JavaScriptParser.New, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def arguments(self):
            return self.getTypedRuleContext(JavaScriptParser.ArgumentsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewExpression" ):
                listener.enterNewExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewExpression" ):
                listener.exitNewExpression(self)


    class LiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(JavaScriptParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpression" ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpression" ):
                listener.exitLiteralExpression(self)


    class ArrayLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrayLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.ArrayLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteralExpression" ):
                listener.enterArrayLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteralExpression" ):
                listener.exitArrayLiteralExpression(self)


    class MemberDotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def Dot(self):
            return self.getToken(JavaScriptParser.Dot, 0)
        def identifierName(self):
            return self.getTypedRuleContext(JavaScriptParser.IdentifierNameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberDotExpression" ):
                listener.enterMemberDotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberDotExpression" ):
                listener.exitMemberDotExpression(self)


    class ClassExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Class(self):
            return self.getToken(JavaScriptParser.Class, 0)
        def classTail(self):
            return self.getTypedRuleContext(JavaScriptParser.ClassTailContext,0)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassExpression" ):
                listener.enterClassExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassExpression" ):
                listener.exitClassExpression(self)


    class MemberIndexExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)

        def OpenBracket(self):
            return self.getToken(JavaScriptParser.OpenBracket, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(JavaScriptParser.ExpressionSequenceContext,0)

        def CloseBracket(self):
            return self.getToken(JavaScriptParser.CloseBracket, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberIndexExpression" ):
                listener.enterMemberIndexExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberIndexExpression" ):
                listener.exitMemberIndexExpression(self)


    class IdentifierExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierExpression" ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierExpression" ):
                listener.exitIdentifierExpression(self)


    class BitAndExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def BitAnd(self):
            return self.getToken(JavaScriptParser.BitAnd, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitAndExpression" ):
                listener.enterBitAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitAndExpression" ):
                listener.exitBitAndExpression(self)


    class BitOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def BitOr(self):
            return self.getToken(JavaScriptParser.BitOr, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitOrExpression" ):
                listener.enterBitOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitOrExpression" ):
                listener.exitBitOrExpression(self)


    class AssignmentOperatorExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,i)

        def assignmentOperator(self):
            return self.getTypedRuleContext(JavaScriptParser.AssignmentOperatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperatorExpression" ):
                listener.enterAssignmentOperatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperatorExpression" ):
                listener.exitAssignmentOperatorExpression(self)


    class VoidExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JavaScriptParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Void(self):
            return self.getToken(JavaScriptParser.Void, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidExpression" ):
                listener.enterVoidExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidExpression" ):
                listener.exitVoidExpression(self)



    def singleExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = JavaScriptParser.SingleExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_singleExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                localctx = JavaScriptParser.FunctionExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 597
                self.match(JavaScriptParser.Function)
                self.state = 599
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JavaScriptParser.Identifier:
                    self.state = 598
                    self.match(JavaScriptParser.Identifier)


                self.state = 601
                self.match(JavaScriptParser.OpenParen)
                self.state = 603
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis))) != 0) or _la==JavaScriptParser.Identifier:
                    self.state = 602
                    self.formalParameterList()


                self.state = 605
                self.match(JavaScriptParser.CloseParen)
                self.state = 606
                self.match(JavaScriptParser.OpenBrace)
                self.state = 607
                self.functionBody()
                self.state = 608
                self.match(JavaScriptParser.CloseBrace)
                pass

            elif la_ == 2:
                localctx = JavaScriptParser.ClassExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 610
                self.match(JavaScriptParser.Class)
                self.state = 612
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JavaScriptParser.Identifier:
                    self.state = 611
                    self.match(JavaScriptParser.Identifier)


                self.state = 614
                self.classTail()
                pass

            elif la_ == 3:
                localctx = JavaScriptParser.NewExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 615
                self.match(JavaScriptParser.New)
                self.state = 616
                self.singleExpression(0)
                self.state = 618
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 617
                    self.arguments()


                pass

            elif la_ == 4:
                localctx = JavaScriptParser.DeleteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 620
                self.match(JavaScriptParser.Delete)
                self.state = 621
                self.singleExpression(33)
                pass

            elif la_ == 5:
                localctx = JavaScriptParser.VoidExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 622
                self.match(JavaScriptParser.Void)
                self.state = 623
                self.singleExpression(32)
                pass

            elif la_ == 6:
                localctx = JavaScriptParser.TypeofExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 624
                self.match(JavaScriptParser.Typeof)
                self.state = 625
                self.singleExpression(31)
                pass

            elif la_ == 7:
                localctx = JavaScriptParser.PreIncrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 626
                self.match(JavaScriptParser.PlusPlus)
                self.state = 627
                self.singleExpression(30)
                pass

            elif la_ == 8:
                localctx = JavaScriptParser.PreDecreaseExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 628
                self.match(JavaScriptParser.MinusMinus)
                self.state = 629
                self.singleExpression(29)
                pass

            elif la_ == 9:
                localctx = JavaScriptParser.UnaryPlusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 630
                self.match(JavaScriptParser.Plus)
                self.state = 631
                self.singleExpression(28)
                pass

            elif la_ == 10:
                localctx = JavaScriptParser.UnaryMinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 632
                self.match(JavaScriptParser.Minus)
                self.state = 633
                self.singleExpression(27)
                pass

            elif la_ == 11:
                localctx = JavaScriptParser.BitNotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 634
                self.match(JavaScriptParser.BitNot)
                self.state = 635
                self.singleExpression(26)
                pass

            elif la_ == 12:
                localctx = JavaScriptParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 636
                self.match(JavaScriptParser.Not)
                self.state = 637
                self.singleExpression(25)
                pass

            elif la_ == 13:
                localctx = JavaScriptParser.ThisExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 638
                self.match(JavaScriptParser.This)
                pass

            elif la_ == 14:
                localctx = JavaScriptParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 639
                self.match(JavaScriptParser.Identifier)
                pass

            elif la_ == 15:
                localctx = JavaScriptParser.SuperExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 640
                self.match(JavaScriptParser.Super)
                pass

            elif la_ == 16:
                localctx = JavaScriptParser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 641
                self.literal()
                pass

            elif la_ == 17:
                localctx = JavaScriptParser.ArrayLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 642
                self.arrayLiteral()
                pass

            elif la_ == 18:
                localctx = JavaScriptParser.ObjectLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 643
                self.objectLiteral()
                pass

            elif la_ == 19:
                localctx = JavaScriptParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 644
                self.match(JavaScriptParser.OpenParen)
                self.state = 645
                self.expressionSequence()
                self.state = 646
                self.match(JavaScriptParser.CloseParen)
                pass

            elif la_ == 20:
                localctx = JavaScriptParser.ArrowFunctionExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 648
                self.arrowFunctionParameters()
                self.state = 649
                self.match(JavaScriptParser.ARROW)
                self.state = 650
                self.arrowFunctionBody()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 723
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 721
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                    if la_ == 1:
                        localctx = JavaScriptParser.MultiplicativeExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 654
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 655
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.Multiply) | (1 << JavaScriptParser.Divide) | (1 << JavaScriptParser.Modulus))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 656
                        self.singleExpression(25)
                        pass

                    elif la_ == 2:
                        localctx = JavaScriptParser.AdditiveExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 657
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 658
                        _la = self._input.LA(1)
                        if not(_la==JavaScriptParser.Plus or _la==JavaScriptParser.Minus):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 659
                        self.singleExpression(24)
                        pass

                    elif la_ == 3:
                        localctx = JavaScriptParser.BitShiftExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 660
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 661
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.RightShiftArithmetic) | (1 << JavaScriptParser.LeftShiftArithmetic) | (1 << JavaScriptParser.RightShiftLogical))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 662
                        self.singleExpression(23)
                        pass

                    elif la_ == 4:
                        localctx = JavaScriptParser.RelationalExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 663
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 664
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.LessThan) | (1 << JavaScriptParser.MoreThan) | (1 << JavaScriptParser.LessThanEquals) | (1 << JavaScriptParser.GreaterThanEquals))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 665
                        self.singleExpression(22)
                        pass

                    elif la_ == 5:
                        localctx = JavaScriptParser.InstanceofExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 666
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 667
                        self.match(JavaScriptParser.Instanceof)
                        self.state = 668
                        self.singleExpression(21)
                        pass

                    elif la_ == 6:
                        localctx = JavaScriptParser.InExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 669
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 670
                        self.match(JavaScriptParser.In)
                        self.state = 671
                        self.singleExpression(20)
                        pass

                    elif la_ == 7:
                        localctx = JavaScriptParser.EqualityExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 672
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 673
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.Equals_) | (1 << JavaScriptParser.NotEquals) | (1 << JavaScriptParser.IdentityEquals) | (1 << JavaScriptParser.IdentityNotEquals))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 674
                        self.singleExpression(19)
                        pass

                    elif la_ == 8:
                        localctx = JavaScriptParser.BitAndExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 675
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 676
                        self.match(JavaScriptParser.BitAnd)
                        self.state = 677
                        self.singleExpression(18)
                        pass

                    elif la_ == 9:
                        localctx = JavaScriptParser.BitXOrExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 678
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 679
                        self.match(JavaScriptParser.BitXOr)
                        self.state = 680
                        self.singleExpression(17)
                        pass

                    elif la_ == 10:
                        localctx = JavaScriptParser.BitOrExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 681
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 682
                        self.match(JavaScriptParser.BitOr)
                        self.state = 683
                        self.singleExpression(16)
                        pass

                    elif la_ == 11:
                        localctx = JavaScriptParser.LogicalAndExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 684
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 685
                        self.match(JavaScriptParser.And)
                        self.state = 686
                        self.singleExpression(15)
                        pass

                    elif la_ == 12:
                        localctx = JavaScriptParser.LogicalOrExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 687
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 688
                        self.match(JavaScriptParser.Or)
                        self.state = 689
                        self.singleExpression(14)
                        pass

                    elif la_ == 13:
                        localctx = JavaScriptParser.TernaryExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 690
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 691
                        self.match(JavaScriptParser.QuestionMark)
                        self.state = 692
                        self.singleExpression(0)
                        self.state = 693
                        self.match(JavaScriptParser.Colon)
                        self.state = 694
                        self.singleExpression(13)
                        pass

                    elif la_ == 14:
                        localctx = JavaScriptParser.AssignmentExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 696
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 697
                        self.match(JavaScriptParser.Assign)
                        self.state = 698
                        self.singleExpression(12)
                        pass

                    elif la_ == 15:
                        localctx = JavaScriptParser.AssignmentOperatorExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 699
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 700
                        self.assignmentOperator()
                        self.state = 701
                        self.singleExpression(11)
                        pass

                    elif la_ == 16:
                        localctx = JavaScriptParser.MemberIndexExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 703
                        if not self.precpred(self._ctx, 39):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 39)")
                        self.state = 704
                        self.match(JavaScriptParser.OpenBracket)
                        self.state = 705
                        self.expressionSequence()
                        self.state = 706
                        self.match(JavaScriptParser.CloseBracket)
                        pass

                    elif la_ == 17:
                        localctx = JavaScriptParser.MemberDotExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 708
                        if not self.precpred(self._ctx, 38):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 38)")
                        self.state = 709
                        self.match(JavaScriptParser.Dot)
                        self.state = 710
                        self.identifierName()
                        pass

                    elif la_ == 18:
                        localctx = JavaScriptParser.ArgumentsExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 711
                        if not self.precpred(self._ctx, 37):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 37)")
                        self.state = 712
                        self.arguments()
                        pass

                    elif la_ == 19:
                        localctx = JavaScriptParser.PostIncrementExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 713
                        if not self.precpred(self._ctx, 35):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 35)")
                        self.state = 714
                        if not self.notLineTerminator():
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.notLineTerminator()")
                        self.state = 715
                        self.match(JavaScriptParser.PlusPlus)
                        pass

                    elif la_ == 20:
                        localctx = JavaScriptParser.PostDecreaseExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 716
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 717
                        if not self.notLineTerminator():
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.notLineTerminator()")
                        self.state = 718
                        self.match(JavaScriptParser.MinusMinus)
                        pass

                    elif la_ == 21:
                        localctx = JavaScriptParser.TemplateStringExpressionContext(self, JavaScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 719
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 720
                        self.match(JavaScriptParser.TemplateStringLiteral)
                        pass

             
                self.state = 725
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArrowFunctionParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def OpenParen(self):
            return self.getToken(JavaScriptParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(JavaScriptParser.CloseParen, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(JavaScriptParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_arrowFunctionParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrowFunctionParameters" ):
                listener.enterArrowFunctionParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrowFunctionParameters" ):
                listener.exitArrowFunctionParameters(self)




    def arrowFunctionParameters(self):

        localctx = JavaScriptParser.ArrowFunctionParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_arrowFunctionParameters)
        self._la = 0 # Token type
        try:
            self.state = 732
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 726
                self.match(JavaScriptParser.Identifier)
                pass
            elif token in [JavaScriptParser.OpenParen]:
                self.enterOuterAlt(localctx, 2)
                self.state = 727
                self.match(JavaScriptParser.OpenParen)
                self.state = 729
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.OpenBracket) | (1 << JavaScriptParser.OpenBrace) | (1 << JavaScriptParser.Ellipsis))) != 0) or _la==JavaScriptParser.Identifier:
                    self.state = 728
                    self.formalParameterList()


                self.state = 731
                self.match(JavaScriptParser.CloseParen)
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


    class ArrowFunctionBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self):
            return self.getTypedRuleContext(JavaScriptParser.SingleExpressionContext,0)


        def OpenBrace(self):
            return self.getToken(JavaScriptParser.OpenBrace, 0)

        def functionBody(self):
            return self.getTypedRuleContext(JavaScriptParser.FunctionBodyContext,0)


        def CloseBrace(self):
            return self.getToken(JavaScriptParser.CloseBrace, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_arrowFunctionBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrowFunctionBody" ):
                listener.enterArrowFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrowFunctionBody" ):
                listener.exitArrowFunctionBody(self)




    def arrowFunctionBody(self):

        localctx = JavaScriptParser.ArrowFunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arrowFunctionBody)
        try:
            self.state = 739
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 734
                self.singleExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 735
                self.match(JavaScriptParser.OpenBrace)
                self.state = 736
                self.functionBody()
                self.state = 737
                self.match(JavaScriptParser.CloseBrace)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MultiplyAssign(self):
            return self.getToken(JavaScriptParser.MultiplyAssign, 0)

        def DivideAssign(self):
            return self.getToken(JavaScriptParser.DivideAssign, 0)

        def ModulusAssign(self):
            return self.getToken(JavaScriptParser.ModulusAssign, 0)

        def PlusAssign(self):
            return self.getToken(JavaScriptParser.PlusAssign, 0)

        def MinusAssign(self):
            return self.getToken(JavaScriptParser.MinusAssign, 0)

        def LeftShiftArithmeticAssign(self):
            return self.getToken(JavaScriptParser.LeftShiftArithmeticAssign, 0)

        def RightShiftArithmeticAssign(self):
            return self.getToken(JavaScriptParser.RightShiftArithmeticAssign, 0)

        def RightShiftLogicalAssign(self):
            return self.getToken(JavaScriptParser.RightShiftLogicalAssign, 0)

        def BitAndAssign(self):
            return self.getToken(JavaScriptParser.BitAndAssign, 0)

        def BitXorAssign(self):
            return self.getToken(JavaScriptParser.BitXorAssign, 0)

        def BitOrAssign(self):
            return self.getToken(JavaScriptParser.BitOrAssign, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)




    def assignmentOperator(self):

        localctx = JavaScriptParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.MultiplyAssign) | (1 << JavaScriptParser.DivideAssign) | (1 << JavaScriptParser.ModulusAssign) | (1 << JavaScriptParser.PlusAssign) | (1 << JavaScriptParser.MinusAssign) | (1 << JavaScriptParser.LeftShiftArithmeticAssign) | (1 << JavaScriptParser.RightShiftArithmeticAssign) | (1 << JavaScriptParser.RightShiftLogicalAssign) | (1 << JavaScriptParser.BitAndAssign) | (1 << JavaScriptParser.BitXorAssign) | (1 << JavaScriptParser.BitOrAssign))) != 0)):
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


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NullLiteral(self):
            return self.getToken(JavaScriptParser.NullLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(JavaScriptParser.BooleanLiteral, 0)

        def StringLiteral(self):
            return self.getToken(JavaScriptParser.StringLiteral, 0)

        def TemplateStringLiteral(self):
            return self.getToken(JavaScriptParser.TemplateStringLiteral, 0)

        def RegularExpressionLiteral(self):
            return self.getToken(JavaScriptParser.RegularExpressionLiteral, 0)

        def numericLiteral(self):
            return self.getTypedRuleContext(JavaScriptParser.NumericLiteralContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = JavaScriptParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_literal)
        try:
            self.state = 749
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.NullLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 743
                self.match(JavaScriptParser.NullLiteral)
                pass
            elif token in [JavaScriptParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 744
                self.match(JavaScriptParser.BooleanLiteral)
                pass
            elif token in [JavaScriptParser.StringLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 745
                self.match(JavaScriptParser.StringLiteral)
                pass
            elif token in [JavaScriptParser.TemplateStringLiteral]:
                self.enterOuterAlt(localctx, 4)
                self.state = 746
                self.match(JavaScriptParser.TemplateStringLiteral)
                pass
            elif token in [JavaScriptParser.RegularExpressionLiteral]:
                self.enterOuterAlt(localctx, 5)
                self.state = 747
                self.match(JavaScriptParser.RegularExpressionLiteral)
                pass
            elif token in [JavaScriptParser.DecimalLiteral, JavaScriptParser.HexIntegerLiteral, JavaScriptParser.OctalIntegerLiteral, JavaScriptParser.OctalIntegerLiteral2, JavaScriptParser.BinaryIntegerLiteral]:
                self.enterOuterAlt(localctx, 6)
                self.state = 748
                self.numericLiteral()
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


    class NumericLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DecimalLiteral(self):
            return self.getToken(JavaScriptParser.DecimalLiteral, 0)

        def HexIntegerLiteral(self):
            return self.getToken(JavaScriptParser.HexIntegerLiteral, 0)

        def OctalIntegerLiteral(self):
            return self.getToken(JavaScriptParser.OctalIntegerLiteral, 0)

        def OctalIntegerLiteral2(self):
            return self.getToken(JavaScriptParser.OctalIntegerLiteral2, 0)

        def BinaryIntegerLiteral(self):
            return self.getToken(JavaScriptParser.BinaryIntegerLiteral, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_numericLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericLiteral" ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericLiteral" ):
                listener.exitNumericLiteral(self)




    def numericLiteral(self):

        localctx = JavaScriptParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_numericLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 751
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JavaScriptParser.DecimalLiteral) | (1 << JavaScriptParser.HexIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral) | (1 << JavaScriptParser.OctalIntegerLiteral2) | (1 << JavaScriptParser.BinaryIntegerLiteral))) != 0)):
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


    class IdentifierNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def reservedWord(self):
            return self.getTypedRuleContext(JavaScriptParser.ReservedWordContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_identifierName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierName" ):
                listener.enterIdentifierName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierName" ):
                listener.exitIdentifierName(self)




    def identifierName(self):

        localctx = JavaScriptParser.IdentifierNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_identifierName)
        try:
            self.state = 755
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 753
                self.match(JavaScriptParser.Identifier)
                pass
            elif token in [JavaScriptParser.NullLiteral, JavaScriptParser.BooleanLiteral, JavaScriptParser.Break, JavaScriptParser.Do, JavaScriptParser.Instanceof, JavaScriptParser.Typeof, JavaScriptParser.Case, JavaScriptParser.Else, JavaScriptParser.New, JavaScriptParser.Var, JavaScriptParser.Catch, JavaScriptParser.Finally, JavaScriptParser.Return, JavaScriptParser.Void, JavaScriptParser.Continue, JavaScriptParser.For, JavaScriptParser.Switch, JavaScriptParser.While, JavaScriptParser.Debugger, JavaScriptParser.Function, JavaScriptParser.This, JavaScriptParser.With, JavaScriptParser.Default, JavaScriptParser.If, JavaScriptParser.Throw, JavaScriptParser.Delete, JavaScriptParser.In, JavaScriptParser.Try, JavaScriptParser.Class, JavaScriptParser.Enum, JavaScriptParser.Extends, JavaScriptParser.Super, JavaScriptParser.Const, JavaScriptParser.Export, JavaScriptParser.Import, JavaScriptParser.Implements, JavaScriptParser.Let, JavaScriptParser.Private, JavaScriptParser.Public, JavaScriptParser.Interface, JavaScriptParser.Package, JavaScriptParser.Protected, JavaScriptParser.Static, JavaScriptParser.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 754
                self.reservedWord()
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


    class ReservedWordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(JavaScriptParser.KeywordContext,0)


        def NullLiteral(self):
            return self.getToken(JavaScriptParser.NullLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(JavaScriptParser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_reservedWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReservedWord" ):
                listener.enterReservedWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReservedWord" ):
                listener.exitReservedWord(self)




    def reservedWord(self):

        localctx = JavaScriptParser.ReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_reservedWord)
        try:
            self.state = 760
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JavaScriptParser.Break, JavaScriptParser.Do, JavaScriptParser.Instanceof, JavaScriptParser.Typeof, JavaScriptParser.Case, JavaScriptParser.Else, JavaScriptParser.New, JavaScriptParser.Var, JavaScriptParser.Catch, JavaScriptParser.Finally, JavaScriptParser.Return, JavaScriptParser.Void, JavaScriptParser.Continue, JavaScriptParser.For, JavaScriptParser.Switch, JavaScriptParser.While, JavaScriptParser.Debugger, JavaScriptParser.Function, JavaScriptParser.This, JavaScriptParser.With, JavaScriptParser.Default, JavaScriptParser.If, JavaScriptParser.Throw, JavaScriptParser.Delete, JavaScriptParser.In, JavaScriptParser.Try, JavaScriptParser.Class, JavaScriptParser.Enum, JavaScriptParser.Extends, JavaScriptParser.Super, JavaScriptParser.Const, JavaScriptParser.Export, JavaScriptParser.Import, JavaScriptParser.Implements, JavaScriptParser.Let, JavaScriptParser.Private, JavaScriptParser.Public, JavaScriptParser.Interface, JavaScriptParser.Package, JavaScriptParser.Protected, JavaScriptParser.Static, JavaScriptParser.Yield]:
                self.enterOuterAlt(localctx, 1)
                self.state = 757
                self.keyword()
                pass
            elif token in [JavaScriptParser.NullLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 758
                self.match(JavaScriptParser.NullLiteral)
                pass
            elif token in [JavaScriptParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 759
                self.match(JavaScriptParser.BooleanLiteral)
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


    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(JavaScriptParser.Break, 0)

        def Do(self):
            return self.getToken(JavaScriptParser.Do, 0)

        def Instanceof(self):
            return self.getToken(JavaScriptParser.Instanceof, 0)

        def Typeof(self):
            return self.getToken(JavaScriptParser.Typeof, 0)

        def Case(self):
            return self.getToken(JavaScriptParser.Case, 0)

        def Else(self):
            return self.getToken(JavaScriptParser.Else, 0)

        def New(self):
            return self.getToken(JavaScriptParser.New, 0)

        def Var(self):
            return self.getToken(JavaScriptParser.Var, 0)

        def Catch(self):
            return self.getToken(JavaScriptParser.Catch, 0)

        def Finally(self):
            return self.getToken(JavaScriptParser.Finally, 0)

        def Return(self):
            return self.getToken(JavaScriptParser.Return, 0)

        def Void(self):
            return self.getToken(JavaScriptParser.Void, 0)

        def Continue(self):
            return self.getToken(JavaScriptParser.Continue, 0)

        def For(self):
            return self.getToken(JavaScriptParser.For, 0)

        def Switch(self):
            return self.getToken(JavaScriptParser.Switch, 0)

        def While(self):
            return self.getToken(JavaScriptParser.While, 0)

        def Debugger(self):
            return self.getToken(JavaScriptParser.Debugger, 0)

        def Function(self):
            return self.getToken(JavaScriptParser.Function, 0)

        def This(self):
            return self.getToken(JavaScriptParser.This, 0)

        def With(self):
            return self.getToken(JavaScriptParser.With, 0)

        def Default(self):
            return self.getToken(JavaScriptParser.Default, 0)

        def If(self):
            return self.getToken(JavaScriptParser.If, 0)

        def Throw(self):
            return self.getToken(JavaScriptParser.Throw, 0)

        def Delete(self):
            return self.getToken(JavaScriptParser.Delete, 0)

        def In(self):
            return self.getToken(JavaScriptParser.In, 0)

        def Try(self):
            return self.getToken(JavaScriptParser.Try, 0)

        def Class(self):
            return self.getToken(JavaScriptParser.Class, 0)

        def Enum(self):
            return self.getToken(JavaScriptParser.Enum, 0)

        def Extends(self):
            return self.getToken(JavaScriptParser.Extends, 0)

        def Super(self):
            return self.getToken(JavaScriptParser.Super, 0)

        def Const(self):
            return self.getToken(JavaScriptParser.Const, 0)

        def Export(self):
            return self.getToken(JavaScriptParser.Export, 0)

        def Import(self):
            return self.getToken(JavaScriptParser.Import, 0)

        def Implements(self):
            return self.getToken(JavaScriptParser.Implements, 0)

        def Let(self):
            return self.getToken(JavaScriptParser.Let, 0)

        def Private(self):
            return self.getToken(JavaScriptParser.Private, 0)

        def Public(self):
            return self.getToken(JavaScriptParser.Public, 0)

        def Interface(self):
            return self.getToken(JavaScriptParser.Interface, 0)

        def Package(self):
            return self.getToken(JavaScriptParser.Package, 0)

        def Protected(self):
            return self.getToken(JavaScriptParser.Protected, 0)

        def Static(self):
            return self.getToken(JavaScriptParser.Static, 0)

        def Yield(self):
            return self.getToken(JavaScriptParser.Yield, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword" ):
                listener.enterKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword" ):
                listener.exitKeyword(self)




    def keyword(self):

        localctx = JavaScriptParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 762
            _la = self._input.LA(1)
            if not(((((_la - 61)) & ~0x3f) == 0 and ((1 << (_la - 61)) & ((1 << (JavaScriptParser.Break - 61)) | (1 << (JavaScriptParser.Do - 61)) | (1 << (JavaScriptParser.Instanceof - 61)) | (1 << (JavaScriptParser.Typeof - 61)) | (1 << (JavaScriptParser.Case - 61)) | (1 << (JavaScriptParser.Else - 61)) | (1 << (JavaScriptParser.New - 61)) | (1 << (JavaScriptParser.Var - 61)) | (1 << (JavaScriptParser.Catch - 61)) | (1 << (JavaScriptParser.Finally - 61)) | (1 << (JavaScriptParser.Return - 61)) | (1 << (JavaScriptParser.Void - 61)) | (1 << (JavaScriptParser.Continue - 61)) | (1 << (JavaScriptParser.For - 61)) | (1 << (JavaScriptParser.Switch - 61)) | (1 << (JavaScriptParser.While - 61)) | (1 << (JavaScriptParser.Debugger - 61)) | (1 << (JavaScriptParser.Function - 61)) | (1 << (JavaScriptParser.This - 61)) | (1 << (JavaScriptParser.With - 61)) | (1 << (JavaScriptParser.Default - 61)) | (1 << (JavaScriptParser.If - 61)) | (1 << (JavaScriptParser.Throw - 61)) | (1 << (JavaScriptParser.Delete - 61)) | (1 << (JavaScriptParser.In - 61)) | (1 << (JavaScriptParser.Try - 61)) | (1 << (JavaScriptParser.Class - 61)) | (1 << (JavaScriptParser.Enum - 61)) | (1 << (JavaScriptParser.Extends - 61)) | (1 << (JavaScriptParser.Super - 61)) | (1 << (JavaScriptParser.Const - 61)) | (1 << (JavaScriptParser.Export - 61)) | (1 << (JavaScriptParser.Import - 61)) | (1 << (JavaScriptParser.Implements - 61)) | (1 << (JavaScriptParser.Let - 61)) | (1 << (JavaScriptParser.Private - 61)) | (1 << (JavaScriptParser.Public - 61)) | (1 << (JavaScriptParser.Interface - 61)) | (1 << (JavaScriptParser.Package - 61)) | (1 << (JavaScriptParser.Protected - 61)) | (1 << (JavaScriptParser.Static - 61)) | (1 << (JavaScriptParser.Yield - 61)))) != 0)):
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


    class GetterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def propertyName(self):
            return self.getTypedRuleContext(JavaScriptParser.PropertyNameContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_getter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetter" ):
                listener.enterGetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetter" ):
                listener.exitGetter(self)




    def getter(self):

        localctx = JavaScriptParser.GetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_getter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 764
            self.match(JavaScriptParser.Identifier)
            self.state = 765
            if not self.p("get"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self.p(\"get\")")
            self.state = 766
            self.propertyName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaScriptParser.Identifier, 0)

        def propertyName(self):
            return self.getTypedRuleContext(JavaScriptParser.PropertyNameContext,0)


        def getRuleIndex(self):
            return JavaScriptParser.RULE_setter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetter" ):
                listener.enterSetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetter" ):
                listener.exitSetter(self)




    def setter(self):

        localctx = JavaScriptParser.SetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_setter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 768
            self.match(JavaScriptParser.Identifier)
            self.state = 769
            if not self.p("set"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self.p(\"set\")")
            self.state = 770
            self.propertyName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SemiColon(self):
            return self.getToken(JavaScriptParser.SemiColon, 0)

        def EOF(self):
            return self.getToken(JavaScriptParser.EOF, 0)

        def getRuleIndex(self):
            return JavaScriptParser.RULE_eos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEos" ):
                listener.enterEos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEos" ):
                listener.exitEos(self)




    def eos(self):

        localctx = JavaScriptParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_eos)
        try:
            self.state = 776
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 772
                self.match(JavaScriptParser.SemiColon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 773
                self.match(JavaScriptParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 774
                if not self.lineTerminatorAhead():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.lineTerminatorAhead()")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 775
                if not self.closeBrace():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.closeBrace()")
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expressionStatement_sempred
        self._predicates[11] = self.iterationStatement_sempred
        self._predicates[13] = self.continueStatement_sempred
        self._predicates[14] = self.breakStatement_sempred
        self._predicates[15] = self.returnStatement_sempred
        self._predicates[23] = self.throwStatement_sempred
        self._predicates[31] = self.classElement_sempred
        self._predicates[48] = self.singleExpression_sempred
        self._predicates[57] = self.getter_sempred
        self._predicates[58] = self.setter_sempred
        self._predicates[59] = self.eos_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressionStatement_sempred(self, localctx:ExpressionStatementContext, predIndex:int):
            if predIndex == 0:
                return self.notOpenBraceAndNotFunction()
         

    def iterationStatement_sempred(self, localctx:IterationStatementContext, predIndex:int):
            if predIndex == 1:
                return self.p("of")
         

            if predIndex == 2:
                return self.p("of")
         

    def continueStatement_sempred(self, localctx:ContinueStatementContext, predIndex:int):
            if predIndex == 3:
                return self.notLineTerminator()
         

    def breakStatement_sempred(self, localctx:BreakStatementContext, predIndex:int):
            if predIndex == 4:
                return self.notLineTerminator()
         

    def returnStatement_sempred(self, localctx:ReturnStatementContext, predIndex:int):
            if predIndex == 5:
                return self.notLineTerminator()
         

    def throwStatement_sempred(self, localctx:ThrowStatementContext, predIndex:int):
            if predIndex == 6:
                return self.notLineTerminator()
         

    def classElement_sempred(self, localctx:ClassElementContext, predIndex:int):
            if predIndex == 7:
                return n("static")
         

    def singleExpression_sempred(self, localctx:SingleExpressionContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 39)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 38)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 37)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 35)
         

            if predIndex == 27:
                return self.notLineTerminator()
         

            if predIndex == 28:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 29:
                return self.notLineTerminator()
         

            if predIndex == 30:
                return self.precpred(self._ctx, 9)
         

    def getter_sempred(self, localctx:GetterContext, predIndex:int):
            if predIndex == 31:
                return self.p("get")
         

    def setter_sempred(self, localctx:SetterContext, predIndex:int):
            if predIndex == 32:
                return self.p("set")
         

    def eos_sempred(self, localctx:EosContext, predIndex:int):
            if predIndex == 33:
                return self.lineTerminatorAhead()
         

            if predIndex == 34:
                return self.closeBrace()
