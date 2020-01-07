# Generated from GoParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

if __name__ is not None and "." in __name__:
    from .GoParserBase import GoParserBase
else:
    from GoParserBase import GoParserBase


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3M")
        buf.write("\u03b5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\3\2\3\2\3\2\3\2\3\2")
        buf.write("\7\2\u00ce\n\2\f\2\16\2\u00d1\13\2\3\2\3\2\3\2\5\2\u00d6")
        buf.write("\n\2\3\2\3\2\7\2\u00da\n\2\f\2\16\2\u00dd\13\2\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u00e8\n\4\f\4\16\4\u00eb")
        buf.write("\13\4\3\4\5\4\u00ee\n\4\3\5\5\5\u00f1\n\5\3\5\3\5\3\6")
        buf.write("\3\6\3\7\3\7\3\7\5\7\u00fa\n\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\7\b\u0102\n\b\f\b\16\b\u0105\13\b\3\b\5\b\u0108\n\b\3")
        buf.write("\t\3\t\5\t\u010c\n\t\3\t\3\t\5\t\u0110\n\t\3\n\3\n\3\n")
        buf.write("\7\n\u0115\n\n\f\n\16\n\u0118\13\n\3\13\3\13\3\13\7\13")
        buf.write("\u011d\n\13\f\13\16\13\u0120\13\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\7\f\u0128\n\f\f\f\16\f\u012b\13\f\3\f\5\f\u012e\n")
        buf.write("\f\3\r\3\r\5\r\u0132\n\r\3\r\3\r\3\16\3\16\3\16\3\16\5")
        buf.write("\16\u013a\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u0141\n\17")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u014b\n")
        buf.write("\21\f\21\16\21\u014e\13\21\3\21\5\21\u0151\n\21\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u0157\n\22\3\22\3\22\5\22\u015b\n\22")
        buf.write("\3\23\3\23\5\23\u015f\n\23\3\23\3\23\3\24\3\24\3\24\6")
        buf.write("\24\u0166\n\24\r\24\16\24\u0167\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u0179\n\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0181")
        buf.write("\n\26\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\5\33\u0191\n\33\3\33\3\33\3\34\3")
        buf.write("\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\5\37\u01a1\n\37\3 \3 \5 \u01a5\n \3!\3!\5!\u01a9\n!\3")
        buf.write("\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3%\5%\u01b7\n%\3%\3")
        buf.write("%\3%\3%\3%\5%\u01be\n%\5%\u01c0\n%\3&\3&\5&\u01c4\n&\3")
        buf.write("\'\3\'\3\'\3\'\5\'\u01ca\n\'\3\'\5\'\u01cd\n\'\3\'\3\'")
        buf.write("\7\'\u01d1\n\'\f\'\16\'\u01d4\13\'\3\'\3\'\3(\3(\3(\5")
        buf.write("(\u01db\n(\3)\3)\3)\5)\u01e0\n)\3*\3*\3*\3*\5*\u01e6\n")
        buf.write("*\3*\3*\3*\7*\u01eb\n*\f*\16*\u01ee\13*\3*\3*\3+\3+\5")
        buf.write("+\u01f4\n+\3+\3+\3+\3+\3+\3+\3,\3,\3,\5,\u01ff\n,\3-\3")
        buf.write("-\3-\5-\u0204\n-\3.\3.\5.\u0208\n.\3.\3.\3.\5.\u020d\n")
        buf.write(".\7.\u020f\n.\f.\16.\u0212\13.\3/\3/\3/\7/\u0217\n/\f")
        buf.write("/\16/\u021a\13/\3/\3/\3\60\3\60\3\60\5\60\u0221\n\60\3")
        buf.write("\61\3\61\3\61\5\61\u0226\n\61\3\61\5\61\u0229\n\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\5\62\u0231\n\62\3\62\3\62\3")
        buf.write("\63\3\63\3\63\3\63\5\63\u0239\n\63\3\63\3\63\3\64\5\64")
        buf.write("\u023e\n\64\3\64\3\64\5\64\u0242\n\64\3\64\3\64\5\64\u0246")
        buf.write("\n\64\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u024e\n\65\3")
        buf.write("\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\5\67\u025c\n\67\38\38\58\u0260\n8\39\39\39\39\3")
        buf.write("9\39\39\39\59\u026a\n9\3:\3:\3:\3:\3:\3;\3;\3<\3<\3=\3")
        buf.write("=\3=\3>\3>\3>\3>\3>\7>\u027d\n>\f>\16>\u0280\13>\3>\3")
        buf.write(">\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\5A\u0293")
        buf.write("\nA\3A\3A\3B\3B\3B\3B\3B\3B\3B\3B\5B\u029f\nB\3C\3C\3")
        buf.write("C\3D\3D\3D\3D\3D\5D\u02a9\nD\3E\3E\5E\u02ad\nE\3F\3F\3")
        buf.write("F\3F\7F\u02b3\nF\fF\16F\u02b6\13F\3F\5F\u02b9\nF\5F\u02bb")
        buf.write("\nF\3F\3F\3G\5G\u02c0\nG\3G\5G\u02c3\nG\3G\3G\3H\3H\3")
        buf.write("H\5H\u02ca\nH\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3")
        buf.write("H\3H\7H\u02db\nH\fH\16H\u02de\13H\3I\3I\3I\5I\u02e3\n")
        buf.write("I\3I\3I\3I\3I\3I\3I\3I\5I\u02ec\nI\7I\u02ee\nI\fI\16I")
        buf.write("\u02f1\13I\3J\3J\3J\5J\u02f6\nJ\3K\3K\3K\3K\5K\u02fc\n")
        buf.write("K\3K\3K\3L\3L\3L\3L\3L\3L\3L\5L\u0307\nL\3M\3M\3M\5M\u030c")
        buf.write("\nM\3N\3N\3N\3N\3N\3N\5N\u0314\nN\3O\3O\3P\3P\5P\u031a")
        buf.write("\nP\3Q\3Q\3Q\3Q\3R\3R\3R\3S\3S\3S\3S\3S\3S\3S\3S\3S\5")
        buf.write("S\u032c\nS\3T\3T\3T\5T\u0331\nT\5T\u0333\nT\3T\3T\3U\3")
        buf.write("U\3U\7U\u033a\nU\fU\16U\u033d\13U\3V\3V\3V\5V\u0342\n")
        buf.write("V\3V\3V\3W\3W\3W\5W\u0349\nW\3X\3X\5X\u034d\nX\3Y\3Y\3")
        buf.write("Y\3Y\3Y\7Y\u0354\nY\fY\16Y\u0357\13Y\3Y\3Y\3Z\3Z\3Z\3")
        buf.write("Z\3Z\5Z\u0360\nZ\3Z\5Z\u0363\nZ\3[\3[\3\\\5\\\u0368\n")
        buf.write("\\\3\\\3\\\3]\3]\3]\3]\3^\3^\3^\3^\3_\3_\5_\u0376\n_\3")
        buf.write("_\3_\5_\u037a\n_\3_\5_\u037d\n_\3_\3_\3_\3_\3_\5_\u0384")
        buf.write("\n_\3_\3_\3`\3`\3`\3`\3`\3a\3a\3a\3a\3a\5a\u0392\na\5")
        buf.write("a\u0394\na\3a\5a\u0397\na\3a\5a\u039a\na\5a\u039c\na\3")
        buf.write("a\3a\3b\3b\3b\3b\3c\3c\3c\3c\3c\5c\u03a9\nc\3c\3c\5c\u03ad")
        buf.write("\nc\3d\3d\3d\3d\5d\u03b3\nd\3d\2\4\u008e\u0090e\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096")
        buf.write("\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8")
        buf.write("\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba")
        buf.write("\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\2\13\4\2\35\35((")
        buf.write("\3\2)*\4\2\65:<@\4\2\66:?@\4\2\65\65<>\3\2/\64\3\2;A\4")
        buf.write("\2BDFG\3\2HI\2\u03ee\2\u00c8\3\2\2\2\4\u00de\3\2\2\2\6")
        buf.write("\u00e1\3\2\2\2\b\u00f0\3\2\2\2\n\u00f4\3\2\2\2\f\u00f9")
        buf.write("\3\2\2\2\16\u00fb\3\2\2\2\20\u0109\3\2\2\2\22\u0111\3")
        buf.write("\2\2\2\24\u0119\3\2\2\2\26\u0121\3\2\2\2\30\u012f\3\2")
        buf.write("\2\2\32\u0135\3\2\2\2\34\u013b\3\2\2\2\36\u0142\3\2\2")
        buf.write("\2 \u0144\3\2\2\2\"\u0152\3\2\2\2$\u015c\3\2\2\2&\u0165")
        buf.write("\3\2\2\2(\u0178\3\2\2\2*\u0180\3\2\2\2,\u0182\3\2\2\2")
        buf.write(".\u0184\3\2\2\2\60\u0188\3\2\2\2\62\u018b\3\2\2\2\64\u0190")
        buf.write("\3\2\2\2\66\u0194\3\2\2\28\u0198\3\2\2\2:\u019a\3\2\2")
        buf.write("\2<\u019e\3\2\2\2>\u01a2\3\2\2\2@\u01a6\3\2\2\2B\u01aa")
        buf.write("\3\2\2\2D\u01ad\3\2\2\2F\u01af\3\2\2\2H\u01b2\3\2\2\2")
        buf.write("J\u01c3\3\2\2\2L\u01c5\3\2\2\2N\u01d7\3\2\2\2P\u01df\3")
        buf.write("\2\2\2R\u01e1\3\2\2\2T\u01f3\3\2\2\2V\u01fb\3\2\2\2X\u0203")
        buf.write("\3\2\2\2Z\u0207\3\2\2\2\\\u0213\3\2\2\2^\u021d\3\2\2\2")
        buf.write("`\u0228\3\2\2\2b\u0230\3\2\2\2d\u0234\3\2\2\2f\u023d\3")
        buf.write("\2\2\2h\u024d\3\2\2\2j\u0252\3\2\2\2l\u025b\3\2\2\2n\u025f")
        buf.write("\3\2\2\2p\u0269\3\2\2\2r\u026b\3\2\2\2t\u0270\3\2\2\2")
        buf.write("v\u0272\3\2\2\2x\u0274\3\2\2\2z\u0277\3\2\2\2|\u0283\3")
        buf.write("\2\2\2~\u0287\3\2\2\2\u0080\u0292\3\2\2\2\u0082\u029e")
        buf.write("\3\2\2\2\u0084\u02a0\3\2\2\2\u0086\u02a8\3\2\2\2\u0088")
        buf.write("\u02ac\3\2\2\2\u008a\u02ae\3\2\2\2\u008c\u02bf\3\2\2\2")
        buf.write("\u008e\u02c9\3\2\2\2\u0090\u02e2\3\2\2\2\u0092\u02f5\3")
        buf.write("\2\2\2\u0094\u02f7\3\2\2\2\u0096\u0306\3\2\2\2\u0098\u030b")
        buf.write("\3\2\2\2\u009a\u0313\3\2\2\2\u009c\u0315\3\2\2\2\u009e")
        buf.write("\u0319\3\2\2\2\u00a0\u031b\3\2\2\2\u00a2\u031f\3\2\2\2")
        buf.write("\u00a4\u032b\3\2\2\2\u00a6\u032d\3\2\2\2\u00a8\u0336\3")
        buf.write("\2\2\2\u00aa\u0341\3\2\2\2\u00ac\u0348\3\2\2\2\u00ae\u034c")
        buf.write("\3\2\2\2\u00b0\u034e\3\2\2\2\u00b2\u035f\3\2\2\2\u00b4")
        buf.write("\u0364\3\2\2\2\u00b6\u0367\3\2\2\2\u00b8\u036b\3\2\2\2")
        buf.write("\u00ba\u036f\3\2\2\2\u00bc\u0373\3\2\2\2\u00be\u0387\3")
        buf.write("\2\2\2\u00c0\u038c\3\2\2\2\u00c2\u039f\3\2\2\2\u00c4\u03ac")
        buf.write("\3\2\2\2\u00c6\u03b2\3\2\2\2\u00c8\u00c9\5\4\3\2\u00c9")
        buf.write("\u00cf\5\u00c6d\2\u00ca\u00cb\5\6\4\2\u00cb\u00cc\5\u00c6")
        buf.write("d\2\u00cc\u00ce\3\2\2\2\u00cd\u00ca\3\2\2\2\u00ce\u00d1")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\u00db\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d6\5\32\16")
        buf.write("\2\u00d3\u00d6\5\34\17\2\u00d4\u00d6\5\f\7\2\u00d5\u00d2")
        buf.write("\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6")
        buf.write("\u00d7\3\2\2\2\u00d7\u00d8\5\u00c6d\2\u00d8\u00da\3\2")
        buf.write("\2\2\u00d9\u00d5\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9")
        buf.write("\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\3\3\2\2\2\u00dd\u00db")
        buf.write("\3\2\2\2\u00de\u00df\7\20\2\2\u00df\u00e0\7\35\2\2\u00e0")
        buf.write("\5\3\2\2\2\u00e1\u00ed\7\31\2\2\u00e2\u00ee\5\b\5\2\u00e3")
        buf.write("\u00e9\7\36\2\2\u00e4\u00e5\5\b\5\2\u00e5\u00e6\5\u00c6")
        buf.write("d\2\u00e6\u00e8\3\2\2\2\u00e7\u00e4\3\2\2\2\u00e8\u00eb")
        buf.write("\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write("\u00ec\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ee\7\37\2")
        buf.write("\2\u00ed\u00e2\3\2\2\2\u00ed\u00e3\3\2\2\2\u00ee\7\3\2")
        buf.write("\2\2\u00ef\u00f1\t\2\2\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\5\n\6\2\u00f3")
        buf.write("\t\3\2\2\2\u00f4\u00f5\5\u00b4[\2\u00f5\13\3\2\2\2\u00f6")
        buf.write("\u00fa\5\16\b\2\u00f7\u00fa\5\26\f\2\u00f8\u00fa\5 \21")
        buf.write("\2\u00f9\u00f6\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8")
        buf.write("\3\2\2\2\u00fa\r\3\2\2\2\u00fb\u0107\7\22\2\2\u00fc\u0108")
        buf.write("\5\20\t\2\u00fd\u0103\7\36\2\2\u00fe\u00ff\5\20\t\2\u00ff")
        buf.write("\u0100\5\u00c6d\2\u0100\u0102\3\2\2\2\u0101\u00fe\3\2")
        buf.write("\2\2\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104")
        buf.write("\3\2\2\2\u0104\u0106\3\2\2\2\u0105\u0103\3\2\2\2\u0106")
        buf.write("\u0108\7\37\2\2\u0107\u00fc\3\2\2\2\u0107\u00fd\3\2\2")
        buf.write("\2\u0108\17\3\2\2\2\u0109\u010f\5\22\n\2\u010a\u010c\5")
        buf.write("l\67\2\u010b\u010a\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u010e\7$\2\2\u010e\u0110\5\24\13\2\u010f")
        buf.write("\u010b\3\2\2\2\u010f\u0110\3\2\2\2\u0110\21\3\2\2\2\u0111")
        buf.write("\u0116\7\35\2\2\u0112\u0113\7%\2\2\u0113\u0115\7\35\2")
        buf.write("\2\u0114\u0112\3\2\2\2\u0115\u0118\3\2\2\2\u0116\u0114")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117\23\3\2\2\2\u0118\u0116")
        buf.write("\3\2\2\2\u0119\u011e\5\u008eH\2\u011a\u011b\7%\2\2\u011b")
        buf.write("\u011d\5\u008eH\2\u011c\u011a\3\2\2\2\u011d\u0120\3\2")
        buf.write("\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\25")
        buf.write("\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u012d\7\26\2\2\u0122")
        buf.write("\u012e\5\30\r\2\u0123\u0129\7\36\2\2\u0124\u0125\5\30")
        buf.write("\r\2\u0125\u0126\5\u00c6d\2\u0126\u0128\3\2\2\2\u0127")
        buf.write("\u0124\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127\3\2\2\2")
        buf.write("\u0129\u012a\3\2\2\2\u012a\u012c\3\2\2\2\u012b\u0129\3")
        buf.write("\2\2\2\u012c\u012e\7\37\2\2\u012d\u0122\3\2\2\2\u012d")
        buf.write("\u0123\3\2\2\2\u012e\27\3\2\2\2\u012f\u0131\7\35\2\2\u0130")
        buf.write("\u0132\7$\2\2\u0131\u0130\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0132\u0133\3\2\2\2\u0133\u0134\5l\67\2\u0134\31\3\2")
        buf.write("\2\2\u0135\u0136\7\5\2\2\u0136\u0137\7\35\2\2\u0137\u0139")
        buf.write("\5\u0086D\2\u0138\u013a\5$\23\2\u0139\u0138\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013a\33\3\2\2\2\u013b\u013c\7\5\2\2\u013c")
        buf.write("\u013d\5\36\20\2\u013d\u013e\7\35\2\2\u013e\u0140\5\u0086")
        buf.write("D\2\u013f\u0141\5$\23\2\u0140\u013f\3\2\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141\35\3\2\2\2\u0142\u0143\5\u008aF\2\u0143")
        buf.write("\37\3\2\2\2\u0144\u0150\7\33\2\2\u0145\u0151\5\"\22\2")
        buf.write("\u0146\u014c\7\36\2\2\u0147\u0148\5\"\22\2\u0148\u0149")
        buf.write("\5\u00c6d\2\u0149\u014b\3\2\2\2\u014a\u0147\3\2\2\2\u014b")
        buf.write("\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2")
        buf.write("\u014d\u014f\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0151\7")
        buf.write("\37\2\2\u0150\u0145\3\2\2\2\u0150\u0146\3\2\2\2\u0151")
        buf.write("!\3\2\2\2\u0152\u015a\5\22\n\2\u0153\u0156\5l\67\2\u0154")
        buf.write("\u0155\7$\2\2\u0155\u0157\5\24\13\2\u0156\u0154\3\2\2")
        buf.write("\2\u0156\u0157\3\2\2\2\u0157\u015b\3\2\2\2\u0158\u0159")
        buf.write("\7$\2\2\u0159\u015b\5\24\13\2\u015a\u0153\3\2\2\2\u015a")
        buf.write("\u0158\3\2\2\2\u015b#\3\2\2\2\u015c\u015e\7 \2\2\u015d")
        buf.write("\u015f\5&\24\2\u015e\u015d\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f\u0160\3\2\2\2\u0160\u0161\7!\2\2\u0161%\3\2\2\2")
        buf.write("\u0162\u0163\5(\25\2\u0163\u0164\5\u00c6d\2\u0164\u0166")
        buf.write("\3\2\2\2\u0165\u0162\3\2\2\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\'\3\2\2\2\u0169")
        buf.write("\u0179\5\f\7\2\u016a\u0179\5:\36\2\u016b\u0179\5*\26\2")
        buf.write("\u016c\u0179\5j\66\2\u016d\u0179\5<\37\2\u016e\u0179\5")
        buf.write("> \2\u016f\u0179\5@!\2\u0170\u0179\5B\"\2\u0171\u0179")
        buf.write("\5D#\2\u0172\u0179\5$\23\2\u0173\u0179\5H%\2\u0174\u0179")
        buf.write("\5J&\2\u0175\u0179\5\\/\2\u0176\u0179\5d\63\2\u0177\u0179")
        buf.write("\5F$\2\u0178\u0169\3\2\2\2\u0178\u016a\3\2\2\2\u0178\u016b")
        buf.write("\3\2\2\2\u0178\u016c\3\2\2\2\u0178\u016d\3\2\2\2\u0178")
        buf.write("\u016e\3\2\2\2\u0178\u016f\3\2\2\2\u0178\u0170\3\2\2\2")
        buf.write("\u0178\u0171\3\2\2\2\u0178\u0172\3\2\2\2\u0178\u0173\3")
        buf.write("\2\2\2\u0178\u0174\3\2\2\2\u0178\u0175\3\2\2\2\u0178\u0176")
        buf.write("\3\2\2\2\u0178\u0177\3\2\2\2\u0179)\3\2\2\2\u017a\u0181")
        buf.write("\5.\30\2\u017b\u0181\5,\27\2\u017c\u0181\5\60\31\2\u017d")
        buf.write("\u0181\5\62\32\2\u017e\u0181\5\66\34\2\u017f\u0181\58")
        buf.write("\35\2\u0180\u017a\3\2\2\2\u0180\u017b\3\2\2\2\u0180\u017c")
        buf.write("\3\2\2\2\u0180\u017d\3\2\2\2\u0180\u017e\3\2\2\2\u0180")
        buf.write("\u017f\3\2\2\2\u0181+\3\2\2\2\u0182\u0183\5\u008eH\2\u0183")
        buf.write("-\3\2\2\2\u0184\u0185\5\u008eH\2\u0185\u0186\7A\2\2\u0186")
        buf.write("\u0187\5\u008eH\2\u0187/\3\2\2\2\u0188\u0189\5\u008eH")
        buf.write("\2\u0189\u018a\t\3\2\2\u018a\61\3\2\2\2\u018b\u018c\5")
        buf.write("\24\13\2\u018c\u018d\5\64\33\2\u018d\u018e\5\24\13\2\u018e")
        buf.write("\63\3\2\2\2\u018f\u0191\t\4\2\2\u0190\u018f\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193\7$\2\2")
        buf.write("\u0193\65\3\2\2\2\u0194\u0195\5\22\n\2\u0195\u0196\7+")
        buf.write("\2\2\u0196\u0197\5\24\13\2\u0197\67\3\2\2\2\u0198\u0199")
        buf.write("\7&\2\2\u01999\3\2\2\2\u019a\u019b\7\35\2\2\u019b\u019c")
        buf.write("\7\'\2\2\u019c\u019d\5(\25\2\u019d;\3\2\2\2\u019e\u01a0")
        buf.write("\7\32\2\2\u019f\u01a1\5\24\13\2\u01a0\u019f\3\2\2\2\u01a0")
        buf.write("\u01a1\3\2\2\2\u01a1=\3\2\2\2\u01a2\u01a4\7\3\2\2\u01a3")
        buf.write("\u01a5\7\35\2\2\u01a4\u01a3\3\2\2\2\u01a4\u01a5\3\2\2")
        buf.write("\2\u01a5?\3\2\2\2\u01a6\u01a8\7\27\2\2\u01a7\u01a9\7\35")
        buf.write("\2\2\u01a8\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9A\3")
        buf.write("\2\2\2\u01aa\u01ab\7\17\2\2\u01ab\u01ac\7\35\2\2\u01ac")
        buf.write("C\3\2\2\2\u01ad\u01ae\7\23\2\2\u01aeE\3\2\2\2\u01af\u01b0")
        buf.write("\7\t\2\2\u01b0\u01b1\5\u008eH\2\u01b1G\3\2\2\2\u01b2\u01b6")
        buf.write("\7\24\2\2\u01b3\u01b4\5*\26\2\u01b4\u01b5\7&\2\2\u01b5")
        buf.write("\u01b7\3\2\2\2\u01b6\u01b3\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b8\3\2\2\2\u01b8\u01b9\5\u008eH\2\u01b9\u01bf")
        buf.write("\5$\23\2\u01ba\u01bd\7\16\2\2\u01bb\u01be\5H%\2\u01bc")
        buf.write("\u01be\5$\23\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2")
        buf.write("\u01be\u01c0\3\2\2\2\u01bf\u01ba\3\2\2\2\u01bf\u01c0\3")
        buf.write("\2\2\2\u01c0I\3\2\2\2\u01c1\u01c4\5L\'\2\u01c2\u01c4\5")
        buf.write("R*\2\u01c3\u01c1\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4K\3")
        buf.write("\2\2\2\u01c5\u01c9\7\21\2\2\u01c6\u01c7\5*\26\2\u01c7")
        buf.write("\u01c8\7&\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c6\3\2\2\2")
        buf.write("\u01c9\u01ca\3\2\2\2\u01ca\u01cc\3\2\2\2\u01cb\u01cd\5")
        buf.write("\u008eH\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd")
        buf.write("\u01ce\3\2\2\2\u01ce\u01d2\7 \2\2\u01cf\u01d1\5N(\2\u01d0")
        buf.write("\u01cf\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2")
        buf.write("\u01d2\u01d3\3\2\2\2\u01d3\u01d5\3\2\2\2\u01d4\u01d2\3")
        buf.write("\2\2\2\u01d5\u01d6\7!\2\2\u01d6M\3\2\2\2\u01d7\u01d8\5")
        buf.write("P)\2\u01d8\u01da\7\'\2\2\u01d9\u01db\5&\24\2\u01da\u01d9")
        buf.write("\3\2\2\2\u01da\u01db\3\2\2\2\u01dbO\3\2\2\2\u01dc\u01dd")
        buf.write("\7\b\2\2\u01dd\u01e0\5\24\13\2\u01de\u01e0\7\4\2\2\u01df")
        buf.write("\u01dc\3\2\2\2\u01df\u01de\3\2\2\2\u01e0Q\3\2\2\2\u01e1")
        buf.write("\u01e5\7\21\2\2\u01e2\u01e3\5*\26\2\u01e3\u01e4\7&\2\2")
        buf.write("\u01e4\u01e6\3\2\2\2\u01e5\u01e2\3\2\2\2\u01e5\u01e6\3")
        buf.write("\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\5T+\2\u01e8\u01ec")
        buf.write("\7 \2\2\u01e9\u01eb\5V,\2\u01ea\u01e9\3\2\2\2\u01eb\u01ee")
        buf.write("\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write("\u01ef\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01f0\7!\2\2")
        buf.write("\u01f0S\3\2\2\2\u01f1\u01f2\7\35\2\2\u01f2\u01f4\7+\2")
        buf.write("\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\u01f6\5\u0090I\2\u01f6\u01f7\7(\2\2\u01f7")
        buf.write("\u01f8\7\36\2\2\u01f8\u01f9\7\26\2\2\u01f9\u01fa\7\37")
        buf.write("\2\2\u01faU\3\2\2\2\u01fb\u01fc\5X-\2\u01fc\u01fe\7\'")
        buf.write("\2\2\u01fd\u01ff\5&\24\2\u01fe\u01fd\3\2\2\2\u01fe\u01ff")
        buf.write("\3\2\2\2\u01ffW\3\2\2\2\u0200\u0201\7\b\2\2\u0201\u0204")
        buf.write("\5Z.\2\u0202\u0204\7\4\2\2\u0203\u0200\3\2\2\2\u0203\u0202")
        buf.write("\3\2\2\2\u0204Y\3\2\2\2\u0205\u0208\5l\67\2\u0206\u0208")
        buf.write("\7\34\2\2\u0207\u0205\3\2\2\2\u0207\u0206\3\2\2\2\u0208")
        buf.write("\u0210\3\2\2\2\u0209\u020c\7%\2\2\u020a\u020d\5l\67\2")
        buf.write("\u020b\u020d\7\34\2\2\u020c\u020a\3\2\2\2\u020c\u020b")
        buf.write("\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u0209\3\2\2\2\u020f")
        buf.write("\u0212\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2")
        buf.write("\u0211[\3\2\2\2\u0212\u0210\3\2\2\2\u0213\u0214\7\7\2")
        buf.write("\2\u0214\u0218\7 \2\2\u0215\u0217\5^\60\2\u0216\u0215")
        buf.write("\3\2\2\2\u0217\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218")
        buf.write("\u0219\3\2\2\2\u0219\u021b\3\2\2\2\u021a\u0218\3\2\2\2")
        buf.write("\u021b\u021c\7!\2\2\u021c]\3\2\2\2\u021d\u021e\5`\61\2")
        buf.write("\u021e\u0220\7\'\2\2\u021f\u0221\5&\24\2\u0220\u021f\3")
        buf.write("\2\2\2\u0220\u0221\3\2\2\2\u0221_\3\2\2\2\u0222\u0225")
        buf.write("\7\b\2\2\u0223\u0226\5.\30\2\u0224\u0226\5b\62\2\u0225")
        buf.write("\u0223\3\2\2\2\u0225\u0224\3\2\2\2\u0226\u0229\3\2\2\2")
        buf.write("\u0227\u0229\7\4\2\2\u0228\u0222\3\2\2\2\u0228\u0227\3")
        buf.write("\2\2\2\u0229a\3\2\2\2\u022a\u022b\5\24\13\2\u022b\u022c")
        buf.write("\7$\2\2\u022c\u0231\3\2\2\2\u022d\u022e\5\22\n\2\u022e")
        buf.write("\u022f\7+\2\2\u022f\u0231\3\2\2\2\u0230\u022a\3\2\2\2")
        buf.write("\u0230\u022d\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0232\3")
        buf.write("\2\2\2\u0232\u0233\5\u008eH\2\u0233c\3\2\2\2\u0234\u0238")
        buf.write("\7\30\2\2\u0235\u0239\5\u008eH\2\u0236\u0239\5f\64\2\u0237")
        buf.write("\u0239\5h\65\2\u0238\u0235\3\2\2\2\u0238\u0236\3\2\2\2")
        buf.write("\u0238\u0237\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u023a\3")
        buf.write("\2\2\2\u023a\u023b\5$\23\2\u023be\3\2\2\2\u023c\u023e")
        buf.write("\5*\26\2\u023d\u023c\3\2\2\2\u023d\u023e\3\2\2\2\u023e")
        buf.write("\u023f\3\2\2\2\u023f\u0241\7&\2\2\u0240\u0242\5\u008e")
        buf.write("H\2\u0241\u0240\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0243")
        buf.write("\3\2\2\2\u0243\u0245\7&\2\2\u0244\u0246\5*\26\2\u0245")
        buf.write("\u0244\3\2\2\2\u0245\u0246\3\2\2\2\u0246g\3\2\2\2\u0247")
        buf.write("\u0248\5\24\13\2\u0248\u0249\7$\2\2\u0249\u024e\3\2\2")
        buf.write("\2\u024a\u024b\5\22\n\2\u024b\u024c\7+\2\2\u024c\u024e")
        buf.write("\3\2\2\2\u024d\u0247\3\2\2\2\u024d\u024a\3\2\2\2\u024d")
        buf.write("\u024e\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u0250\7\25\2")
        buf.write("\2\u0250\u0251\5\u008eH\2\u0251i\3\2\2\2\u0252\u0253\7")
        buf.write("\n\2\2\u0253\u0254\5\u008eH\2\u0254k\3\2\2\2\u0255\u025c")
        buf.write("\5n8\2\u0256\u025c\5p9\2\u0257\u0258\7\36\2\2\u0258\u0259")
        buf.write("\5l\67\2\u0259\u025a\7\37\2\2\u025a\u025c\3\2\2\2\u025b")
        buf.write("\u0255\3\2\2\2\u025b\u0256\3\2\2\2\u025b\u0257\3\2\2\2")
        buf.write("\u025cm\3\2\2\2\u025d\u0260\7\35\2\2\u025e\u0260\5\u00a0")
        buf.write("Q\2\u025f\u025d\3\2\2\2\u025f\u025e\3\2\2\2\u0260o\3\2")
        buf.write("\2\2\u0261\u026a\5r:\2\u0262\u026a\5\u00b0Y\2\u0263\u026a")
        buf.write("\5x=\2\u0264\u026a\5\u0084C\2\u0265\u026a\5z>\2\u0266")
        buf.write("\u026a\5|?\2\u0267\u026a\5~@\2\u0268\u026a\5\u0080A\2")
        buf.write("\u0269\u0261\3\2\2\2\u0269\u0262\3\2\2\2\u0269\u0263\3")
        buf.write("\2\2\2\u0269\u0264\3\2\2\2\u0269\u0265\3\2\2\2\u0269\u0266")
        buf.write("\3\2\2\2\u0269\u0267\3\2\2\2\u0269\u0268\3\2\2\2\u026a")
        buf.write("q\3\2\2\2\u026b\u026c\7\"\2\2\u026c\u026d\5t;\2\u026d")
        buf.write("\u026e\7#\2\2\u026e\u026f\5v<\2\u026fs\3\2\2\2\u0270\u0271")
        buf.write("\5\u008eH\2\u0271u\3\2\2\2\u0272\u0273\5l\67\2\u0273w")
        buf.write("\3\2\2\2\u0274\u0275\7?\2\2\u0275\u0276\5l\67\2\u0276")
        buf.write("y\3\2\2\2\u0277\u0278\7\6\2\2\u0278\u027e\7 \2\2\u0279")
        buf.write("\u027a\5\u0082B\2\u027a\u027b\5\u00c6d\2\u027b\u027d\3")
        buf.write("\2\2\2\u027c\u0279\3\2\2\2\u027d\u0280\3\2\2\2\u027e\u027c")
        buf.write("\3\2\2\2\u027e\u027f\3\2\2\2\u027f\u0281\3\2\2\2\u0280")
        buf.write("\u027e\3\2\2\2\u0281\u0282\7!\2\2\u0282{\3\2\2\2\u0283")
        buf.write("\u0284\7\"\2\2\u0284\u0285\7#\2\2\u0285\u0286\5v<\2\u0286")
        buf.write("}\3\2\2\2\u0287\u0288\7\13\2\2\u0288\u0289\7\"\2\2\u0289")
        buf.write("\u028a\5l\67\2\u028a\u028b\7#\2\2\u028b\u028c\5v<\2\u028c")
        buf.write("\177\3\2\2\2\u028d\u0293\7\r\2\2\u028e\u028f\7\r\2\2\u028f")
        buf.write("\u0293\7A\2\2\u0290\u0291\7A\2\2\u0291\u0293\7\r\2\2\u0292")
        buf.write("\u028d\3\2\2\2\u0292\u028e\3\2\2\2\u0292\u0290\3\2\2\2")
        buf.write("\u0293\u0294\3\2\2\2\u0294\u0295\5v<\2\u0295\u0081\3\2")
        buf.write("\2\2\u0296\u0297\6B\2\2\u0297\u0298\7\35\2\2\u0298\u0299")
        buf.write("\5\u008aF\2\u0299\u029a\5\u0088E\2\u029a\u029f\3\2\2\2")
        buf.write("\u029b\u029f\5n8\2\u029c\u029d\7\35\2\2\u029d\u029f\5")
        buf.write("\u008aF\2\u029e\u0296\3\2\2\2\u029e\u029b\3\2\2\2\u029e")
        buf.write("\u029c\3\2\2\2\u029f\u0083\3\2\2\2\u02a0\u02a1\7\5\2\2")
        buf.write("\u02a1\u02a2\5\u0086D\2\u02a2\u0085\3\2\2\2\u02a3\u02a4")
        buf.write("\6D\3\2\u02a4\u02a5\5\u008aF\2\u02a5\u02a6\5\u0088E\2")
        buf.write("\u02a6\u02a9\3\2\2\2\u02a7\u02a9\5\u008aF\2\u02a8\u02a3")
        buf.write("\3\2\2\2\u02a8\u02a7\3\2\2\2\u02a9\u0087\3\2\2\2\u02aa")
        buf.write("\u02ad\5\u008aF\2\u02ab\u02ad\5l\67\2\u02ac\u02aa\3\2")
        buf.write("\2\2\u02ac\u02ab\3\2\2\2\u02ad\u0089\3\2\2\2\u02ae\u02ba")
        buf.write("\7\36\2\2\u02af\u02b4\5\u008cG\2\u02b0\u02b1\7%\2\2\u02b1")
        buf.write("\u02b3\5\u008cG\2\u02b2\u02b0\3\2\2\2\u02b3\u02b6\3\2")
        buf.write("\2\2\u02b4\u02b2\3\2\2\2\u02b4\u02b5\3\2\2\2\u02b5\u02b8")
        buf.write("\3\2\2\2\u02b6\u02b4\3\2\2\2\u02b7\u02b9\7%\2\2\u02b8")
        buf.write("\u02b7\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9\u02bb\3\2\2\2")
        buf.write("\u02ba\u02af\3\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u02bc\3")
        buf.write("\2\2\2\u02bc\u02bd\7\37\2\2\u02bd\u008b\3\2\2\2\u02be")
        buf.write("\u02c0\5\22\n\2\u02bf\u02be\3\2\2\2\u02bf\u02c0\3\2\2")
        buf.write("\2\u02c0\u02c2\3\2\2\2\u02c1\u02c3\7,\2\2\u02c2\u02c1")
        buf.write("\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3\u02c4\3\2\2\2\u02c4")
        buf.write("\u02c5\5l\67\2\u02c5\u008d\3\2\2\2\u02c6\u02c7\bH\1\2")
        buf.write("\u02c7\u02ca\5\u0090I\2\u02c8\u02ca\5\u0092J\2\u02c9\u02c6")
        buf.write("\3\2\2\2\u02c9\u02c8\3\2\2\2\u02ca\u02dc\3\2\2\2\u02cb")
        buf.write("\u02cc\f\7\2\2\u02cc\u02cd\t\5\2\2\u02cd\u02db\5\u008e")
        buf.write("H\b\u02ce\u02cf\f\6\2\2\u02cf\u02d0\t\6\2\2\u02d0\u02db")
        buf.write("\5\u008eH\7\u02d1\u02d2\f\5\2\2\u02d2\u02d3\t\7\2\2\u02d3")
        buf.write("\u02db\5\u008eH\6\u02d4\u02d5\f\4\2\2\u02d5\u02d6\7.\2")
        buf.write("\2\u02d6\u02db\5\u008eH\5\u02d7\u02d8\f\3\2\2\u02d8\u02d9")
        buf.write("\7-\2\2\u02d9\u02db\5\u008eH\4\u02da\u02cb\3\2\2\2\u02da")
        buf.write("\u02ce\3\2\2\2\u02da\u02d1\3\2\2\2\u02da\u02d4\3\2\2\2")
        buf.write("\u02da\u02d7\3\2\2\2\u02db\u02de\3\2\2\2\u02dc\u02da\3")
        buf.write("\2\2\2\u02dc\u02dd\3\2\2\2\u02dd\u008f\3\2\2\2\u02de\u02dc")
        buf.write("\3\2\2\2\u02df\u02e0\bI\1\2\u02e0\u02e3\5\u0096L\2\u02e1")
        buf.write("\u02e3\5\u0094K\2\u02e2\u02df\3\2\2\2\u02e2\u02e1\3\2")
        buf.write("\2\2\u02e3\u02ef\3\2\2\2\u02e4\u02eb\f\3\2\2\u02e5\u02e6")
        buf.write("\7(\2\2\u02e6\u02ec\7\35\2\2\u02e7\u02ec\5\u00ba^\2\u02e8")
        buf.write("\u02ec\5\u00bc_\2\u02e9\u02ec\5\u00be`\2\u02ea\u02ec\5")
        buf.write("\u00c0a\2\u02eb\u02e5\3\2\2\2\u02eb\u02e7\3\2\2\2\u02eb")
        buf.write("\u02e8\3\2\2\2\u02eb\u02e9\3\2\2\2\u02eb\u02ea\3\2\2\2")
        buf.write("\u02ec\u02ee\3\2\2\2\u02ed\u02e4\3\2\2\2\u02ee\u02f1\3")
        buf.write("\2\2\2\u02ef\u02ed\3\2\2\2\u02ef\u02f0\3\2\2\2\u02f0\u0091")
        buf.write("\3\2\2\2\u02f1\u02ef\3\2\2\2\u02f2\u02f6\5\u0090I\2\u02f3")
        buf.write("\u02f4\t\b\2\2\u02f4\u02f6\5\u008eH\2\u02f5\u02f2\3\2")
        buf.write("\2\2\u02f5\u02f3\3\2\2\2\u02f6\u0093\3\2\2\2\u02f7\u02f8")
        buf.write("\5l\67\2\u02f8\u02f9\7\36\2\2\u02f9\u02fb\5\u008eH\2\u02fa")
        buf.write("\u02fc\7%\2\2\u02fb\u02fa\3\2\2\2\u02fb\u02fc\3\2\2\2")
        buf.write("\u02fc\u02fd\3\2\2\2\u02fd\u02fe\7\37\2\2\u02fe\u0095")
        buf.write("\3\2\2\2\u02ff\u0307\5\u0098M\2\u0300\u0307\5\u009eP\2")
        buf.write("\u0301\u0307\5\u00c2b\2\u0302\u0303\7\36\2\2\u0303\u0304")
        buf.write("\5\u008eH\2\u0304\u0305\7\37\2\2\u0305\u0307\3\2\2\2\u0306")
        buf.write("\u02ff\3\2\2\2\u0306\u0300\3\2\2\2\u0306\u0301\3\2\2\2")
        buf.write("\u0306\u0302\3\2\2\2\u0307\u0097\3\2\2\2\u0308\u030c\5")
        buf.write("\u009aN\2\u0309\u030c\5\u00a2R\2\u030a\u030c\5\u00b8]")
        buf.write("\2\u030b\u0308\3\2\2\2\u030b\u0309\3\2\2\2\u030b\u030a")
        buf.write("\3\2\2\2\u030c\u0099\3\2\2\2\u030d\u0314\7\34\2\2\u030e")
        buf.write("\u0314\5\u009cO\2\u030f\u0314\5\u00b4[\2\u0310\u0314\7")
        buf.write("E\2\2\u0311\u0314\7F\2\2\u0312\u0314\7G\2\2\u0313\u030d")
        buf.write("\3\2\2\2\u0313\u030e\3\2\2\2\u0313\u030f\3\2\2\2\u0313")
        buf.write("\u0310\3\2\2\2\u0313\u0311\3\2\2\2\u0313\u0312\3\2\2\2")
        buf.write("\u0314\u009b\3\2\2\2\u0315\u0316\t\t\2\2\u0316\u009d\3")
        buf.write("\2\2\2\u0317\u031a\7\35\2\2\u0318\u031a\5\u00a0Q\2\u0319")
        buf.write("\u0317\3\2\2\2\u0319\u0318\3\2\2\2\u031a\u009f\3\2\2\2")
        buf.write("\u031b\u031c\7\35\2\2\u031c\u031d\7(\2\2\u031d\u031e\7")
        buf.write("\35\2\2\u031e\u00a1\3\2\2\2\u031f\u0320\5\u00a4S\2\u0320")
        buf.write("\u0321\5\u00a6T\2\u0321\u00a3\3\2\2\2\u0322\u032c\5\u00b0")
        buf.write("Y\2\u0323\u032c\5r:\2\u0324\u0325\7\"\2\2\u0325\u0326")
        buf.write("\7,\2\2\u0326\u0327\7#\2\2\u0327\u032c\5v<\2\u0328\u032c")
        buf.write("\5|?\2\u0329\u032c\5~@\2\u032a\u032c\5n8\2\u032b\u0322")
        buf.write("\3\2\2\2\u032b\u0323\3\2\2\2\u032b\u0324\3\2\2\2\u032b")
        buf.write("\u0328\3\2\2\2\u032b\u0329\3\2\2\2\u032b\u032a\3\2\2\2")
        buf.write("\u032c\u00a5\3\2\2\2\u032d\u0332\7 \2\2\u032e\u0330\5")
        buf.write("\u00a8U\2\u032f\u0331\7%\2\2\u0330\u032f\3\2\2\2\u0330")
        buf.write("\u0331\3\2\2\2\u0331\u0333\3\2\2\2\u0332\u032e\3\2\2\2")
        buf.write("\u0332\u0333\3\2\2\2\u0333\u0334\3\2\2\2\u0334\u0335\7")
        buf.write("!\2\2\u0335\u00a7\3\2\2\2\u0336\u033b\5\u00aaV\2\u0337")
        buf.write("\u0338\7%\2\2\u0338\u033a\5\u00aaV\2\u0339\u0337\3\2\2")
        buf.write("\2\u033a\u033d\3\2\2\2\u033b\u0339\3\2\2\2\u033b\u033c")
        buf.write("\3\2\2\2\u033c\u00a9\3\2\2\2\u033d\u033b\3\2\2\2\u033e")
        buf.write("\u033f\5\u00acW\2\u033f\u0340\7\'\2\2\u0340\u0342\3\2")
        buf.write("\2\2\u0341\u033e\3\2\2\2\u0341\u0342\3\2\2\2\u0342\u0343")
        buf.write("\3\2\2\2\u0343\u0344\5\u00aeX\2\u0344\u00ab\3\2\2\2\u0345")
        buf.write("\u0349\7\35\2\2\u0346\u0349\5\u008eH\2\u0347\u0349\5\u00a6")
        buf.write("T\2\u0348\u0345\3\2\2\2\u0348\u0346\3\2\2\2\u0348\u0347")
        buf.write("\3\2\2\2\u0349\u00ad\3\2\2\2\u034a\u034d\5\u008eH\2\u034b")
        buf.write("\u034d\5\u00a6T\2\u034c\u034a\3\2\2\2\u034c\u034b\3\2")
        buf.write("\2\2\u034d\u00af\3\2\2\2\u034e\u034f\7\f\2\2\u034f\u0355")
        buf.write("\7 \2\2\u0350\u0351\5\u00b2Z\2\u0351\u0352\5\u00c6d\2")
        buf.write("\u0352\u0354\3\2\2\2\u0353\u0350\3\2\2\2\u0354\u0357\3")
        buf.write("\2\2\2\u0355\u0353\3\2\2\2\u0355\u0356\3\2\2\2\u0356\u0358")
        buf.write("\3\2\2\2\u0357\u0355\3\2\2\2\u0358\u0359\7!\2\2\u0359")
        buf.write("\u00b1\3\2\2\2\u035a\u035b\6Z\n\2\u035b\u035c\5\22\n\2")
        buf.write("\u035c\u035d\5l\67\2\u035d\u0360\3\2\2\2\u035e\u0360\5")
        buf.write("\u00b6\\\2\u035f\u035a\3\2\2\2\u035f\u035e\3\2\2\2\u0360")
        buf.write("\u0362\3\2\2\2\u0361\u0363\5\u00b4[\2\u0362\u0361\3\2")
        buf.write("\2\2\u0362\u0363\3\2\2\2\u0363\u00b3\3\2\2\2\u0364\u0365")
        buf.write("\t\n\2\2\u0365\u00b5\3\2\2\2\u0366\u0368\7?\2\2\u0367")
        buf.write("\u0366\3\2\2\2\u0367\u0368\3\2\2\2\u0368\u0369\3\2\2\2")
        buf.write("\u0369\u036a\5n8\2\u036a\u00b7\3\2\2\2\u036b\u036c\7\5")
        buf.write("\2\2\u036c\u036d\5\u0086D\2\u036d\u036e\5$\23\2\u036e")
        buf.write("\u00b9\3\2\2\2\u036f\u0370\7\"\2\2\u0370\u0371\5\u008e")
        buf.write("H\2\u0371\u0372\7#\2\2\u0372\u00bb\3\2\2\2\u0373\u0383")
        buf.write("\7\"\2\2\u0374\u0376\5\u008eH\2\u0375\u0374\3\2\2\2\u0375")
        buf.write("\u0376\3\2\2\2\u0376\u0377\3\2\2\2\u0377\u0379\7\'\2\2")
        buf.write("\u0378\u037a\5\u008eH\2\u0379\u0378\3\2\2\2\u0379\u037a")
        buf.write("\3\2\2\2\u037a\u0384\3\2\2\2\u037b\u037d\5\u008eH\2\u037c")
        buf.write("\u037b\3\2\2\2\u037c\u037d\3\2\2\2\u037d\u037e\3\2\2\2")
        buf.write("\u037e\u037f\7\'\2\2\u037f\u0380\5\u008eH\2\u0380\u0381")
        buf.write("\7\'\2\2\u0381\u0382\5\u008eH\2\u0382\u0384\3\2\2\2\u0383")
        buf.write("\u0375\3\2\2\2\u0383\u037c\3\2\2\2\u0384\u0385\3\2\2\2")
        buf.write("\u0385\u0386\7#\2\2\u0386\u00bd\3\2\2\2\u0387\u0388\7")
        buf.write("(\2\2\u0388\u0389\7\36\2\2\u0389\u038a\5l\67\2\u038a\u038b")
        buf.write("\7\37\2\2\u038b\u00bf\3\2\2\2\u038c\u039b\7\36\2\2\u038d")
        buf.write("\u0394\5\24\13\2\u038e\u0391\5l\67\2\u038f\u0390\7%\2")
        buf.write("\2\u0390\u0392\5\24\13\2\u0391\u038f\3\2\2\2\u0391\u0392")
        buf.write("\3\2\2\2\u0392\u0394\3\2\2\2\u0393\u038d\3\2\2\2\u0393")
        buf.write("\u038e\3\2\2\2\u0394\u0396\3\2\2\2\u0395\u0397\7,\2\2")
        buf.write("\u0396\u0395\3\2\2\2\u0396\u0397\3\2\2\2\u0397\u0399\3")
        buf.write("\2\2\2\u0398\u039a\7%\2\2\u0399\u0398\3\2\2\2\u0399\u039a")
        buf.write("\3\2\2\2\u039a\u039c\3\2\2\2\u039b\u0393\3\2\2\2\u039b")
        buf.write("\u039c\3\2\2\2\u039c\u039d\3\2\2\2\u039d\u039e\7\37\2")
        buf.write("\2\u039e\u00c1\3\2\2\2\u039f\u03a0\5\u00c4c\2\u03a0\u03a1")
        buf.write("\7(\2\2\u03a1\u03a2\7\35\2\2\u03a2\u00c3\3\2\2\2\u03a3")
        buf.write("\u03ad\5n8\2\u03a4\u03a8\7\36\2\2\u03a5\u03a6\7?\2\2\u03a6")
        buf.write("\u03a9\5n8\2\u03a7\u03a9\5\u00c4c\2\u03a8\u03a5\3\2\2")
        buf.write("\2\u03a8\u03a7\3\2\2\2\u03a9\u03aa\3\2\2\2\u03aa\u03ab")
        buf.write("\7\37\2\2\u03ab\u03ad\3\2\2\2\u03ac\u03a3\3\2\2\2\u03ac")
        buf.write("\u03a4\3\2\2\2\u03ad\u00c5\3\2\2\2\u03ae\u03b3\7&\2\2")
        buf.write("\u03af\u03b3\7\2\2\3\u03b0\u03b3\6d\13\2\u03b1\u03b3\6")
        buf.write("d\f\2\u03b2\u03ae\3\2\2\2\u03b2\u03af\3\2\2\2\u03b2\u03b0")
        buf.write("\3\2\2\2\u03b2\u03b1\3\2\2\2\u03b3\u00c7\3\2\2\2k\u00cf")
        buf.write("\u00d5\u00db\u00e9\u00ed\u00f0\u00f9\u0103\u0107\u010b")
        buf.write("\u010f\u0116\u011e\u0129\u012d\u0131\u0139\u0140\u014c")
        buf.write("\u0150\u0156\u015a\u015e\u0167\u0178\u0180\u0190\u01a0")
        buf.write("\u01a4\u01a8\u01b6\u01bd\u01bf\u01c3\u01c9\u01cc\u01d2")
        buf.write("\u01da\u01df\u01e5\u01ec\u01f3\u01fe\u0203\u0207\u020c")
        buf.write("\u0210\u0218\u0220\u0225\u0228\u0230\u0238\u023d\u0241")
        buf.write("\u0245\u024d\u025b\u025f\u0269\u027e\u0292\u029e\u02a8")
        buf.write("\u02ac\u02b4\u02b8\u02ba\u02bf\u02c2\u02c9\u02da\u02dc")
        buf.write("\u02e2\u02eb\u02ef\u02f5\u02fb\u0306\u030b\u0313\u0319")
        buf.write("\u032b\u0330\u0332\u033b\u0341\u0348\u034c\u0355\u035f")
        buf.write("\u0362\u0367\u0375\u0379\u037c\u0383\u0391\u0393\u0396")
        buf.write("\u0399\u039b\u03a8\u03ac\u03b2")
        return buf.getvalue()


class GoParser ( GoParserBase ):

    grammarFileName = "GoParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'break'", "'default'", "'func'", "'interface'", 
                     "'select'", "'case'", "'defer'", "'go'", "'map'", "'struct'", 
                     "'chan'", "'else'", "'goto'", "'package'", "'switch'", 
                     "'const'", "'fallthrough'", "'if'", "'range'", "'type'", 
                     "'continue'", "'for'", "'import'", "'return'", "'var'", 
                     "'nil'", "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "'='", "','", "';'", "':'", "'.'", "'++'", "'--'", 
                     "':='", "'...'", "'||'", "'&&'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'|'", "'/'", "'%'", "'<<'", 
                     "'>>'", "'&^'", "'!'", "'+'", "'-'", "'^'", "'*'", 
                     "'&'", "'<-'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "DEFAULT", "FUNC", "INTERFACE", 
                      "SELECT", "CASE", "DEFER", "GO", "MAP", "STRUCT", 
                      "CHAN", "ELSE", "GOTO", "PACKAGE", "SWITCH", "CONST", 
                      "FALLTHROUGH", "IF", "RANGE", "TYPE", "CONTINUE", 
                      "FOR", "IMPORT", "RETURN", "VAR", "NIL_LIT", "IDENTIFIER", 
                      "L_PAREN", "R_PAREN", "L_CURLY", "R_CURLY", "L_BRACKET", 
                      "R_BRACKET", "ASSIGN", "COMMA", "SEMI", "COLON", "DOT", 
                      "PLUS_PLUS", "MINUS_MINUS", "DECLARE_ASSIGN", "ELLIPSIS", 
                      "LOGICAL_OR", "LOGICAL_AND", "EQUALS", "NOT_EQUALS", 
                      "LESS", "LESS_OR_EQUALS", "GREATER", "GREATER_OR_EQUALS", 
                      "OR", "DIV", "MOD", "LSHIFT", "RSHIFT", "BIT_CLEAR", 
                      "EXCLAMATION", "PLUS", "MINUS", "CARET", "STAR", "AMPERSAND", 
                      "RECEIVE", "DECIMAL_LIT", "OCTAL_LIT", "HEX_LIT", 
                      "FLOAT_LIT", "IMAGINARY_LIT", "RUNE_LIT", "RAW_STRING_LIT", 
                      "INTERPRETED_STRING_LIT", "WS", "COMMENT", "TERMINATOR", 
                      "LINE_COMMENT" ]

    RULE_sourceFile = 0
    RULE_packageClause = 1
    RULE_importDecl = 2
    RULE_importSpec = 3
    RULE_importPath = 4
    RULE_declaration = 5
    RULE_constDecl = 6
    RULE_constSpec = 7
    RULE_identifierList = 8
    RULE_expressionList = 9
    RULE_typeDecl = 10
    RULE_typeSpec = 11
    RULE_functionDecl = 12
    RULE_methodDecl = 13
    RULE_receiver = 14
    RULE_varDecl = 15
    RULE_varSpec = 16
    RULE_block = 17
    RULE_statementList = 18
    RULE_statement = 19
    RULE_simpleStmt = 20
    RULE_expressionStmt = 21
    RULE_sendStmt = 22
    RULE_incDecStmt = 23
    RULE_assignment = 24
    RULE_assign_op = 25
    RULE_shortVarDecl = 26
    RULE_emptyStmt = 27
    RULE_labeledStmt = 28
    RULE_returnStmt = 29
    RULE_breakStmt = 30
    RULE_continueStmt = 31
    RULE_gotoStmt = 32
    RULE_fallthroughStmt = 33
    RULE_deferStmt = 34
    RULE_ifStmt = 35
    RULE_switchStmt = 36
    RULE_exprSwitchStmt = 37
    RULE_exprCaseClause = 38
    RULE_exprSwitchCase = 39
    RULE_typeSwitchStmt = 40
    RULE_typeSwitchGuard = 41
    RULE_typeCaseClause = 42
    RULE_typeSwitchCase = 43
    RULE_typeList = 44
    RULE_selectStmt = 45
    RULE_commClause = 46
    RULE_commCase = 47
    RULE_recvStmt = 48
    RULE_forStmt = 49
    RULE_forClause = 50
    RULE_rangeClause = 51
    RULE_goStmt = 52
    RULE_type_ = 53
    RULE_typeName = 54
    RULE_typeLit = 55
    RULE_arrayType = 56
    RULE_arrayLength = 57
    RULE_elementType = 58
    RULE_pointerType = 59
    RULE_interfaceType = 60
    RULE_sliceType = 61
    RULE_mapType = 62
    RULE_channelType = 63
    RULE_methodSpec = 64
    RULE_functionType = 65
    RULE_signature = 66
    RULE_result = 67
    RULE_parameters = 68
    RULE_parameterDecl = 69
    RULE_expression = 70
    RULE_primaryExpr = 71
    RULE_unaryExpr = 72
    RULE_conversion = 73
    RULE_operand = 74
    RULE_literal = 75
    RULE_basicLit = 76
    RULE_integer = 77
    RULE_operandName = 78
    RULE_qualifiedIdent = 79
    RULE_compositeLit = 80
    RULE_literalType = 81
    RULE_literalValue = 82
    RULE_elementList = 83
    RULE_keyedElement = 84
    RULE_key = 85
    RULE_element = 86
    RULE_structType = 87
    RULE_fieldDecl = 88
    RULE_string_ = 89
    RULE_anonymousField = 90
    RULE_functionLit = 91
    RULE_index = 92
    RULE_slice = 93
    RULE_typeAssertion = 94
    RULE_arguments = 95
    RULE_methodExpr = 96
    RULE_receiverType = 97
    RULE_eos = 98

    ruleNames =  [ "sourceFile", "packageClause", "importDecl", "importSpec", 
                   "importPath", "declaration", "constDecl", "constSpec", 
                   "identifierList", "expressionList", "typeDecl", "typeSpec", 
                   "functionDecl", "methodDecl", "receiver", "varDecl", 
                   "varSpec", "block", "statementList", "statement", "simpleStmt", 
                   "expressionStmt", "sendStmt", "incDecStmt", "assignment", 
                   "assign_op", "shortVarDecl", "emptyStmt", "labeledStmt", 
                   "returnStmt", "breakStmt", "continueStmt", "gotoStmt", 
                   "fallthroughStmt", "deferStmt", "ifStmt", "switchStmt", 
                   "exprSwitchStmt", "exprCaseClause", "exprSwitchCase", 
                   "typeSwitchStmt", "typeSwitchGuard", "typeCaseClause", 
                   "typeSwitchCase", "typeList", "selectStmt", "commClause", 
                   "commCase", "recvStmt", "forStmt", "forClause", "rangeClause", 
                   "goStmt", "type_", "typeName", "typeLit", "arrayType", 
                   "arrayLength", "elementType", "pointerType", "interfaceType", 
                   "sliceType", "mapType", "channelType", "methodSpec", 
                   "functionType", "signature", "result", "parameters", 
                   "parameterDecl", "expression", "primaryExpr", "unaryExpr", 
                   "conversion", "operand", "literal", "basicLit", "integer", 
                   "operandName", "qualifiedIdent", "compositeLit", "literalType", 
                   "literalValue", "elementList", "keyedElement", "key", 
                   "element", "structType", "fieldDecl", "string_", "anonymousField", 
                   "functionLit", "index", "slice", "typeAssertion", "arguments", 
                   "methodExpr", "receiverType", "eos" ]

    EOF = Token.EOF
    BREAK=1
    DEFAULT=2
    FUNC=3
    INTERFACE=4
    SELECT=5
    CASE=6
    DEFER=7
    GO=8
    MAP=9
    STRUCT=10
    CHAN=11
    ELSE=12
    GOTO=13
    PACKAGE=14
    SWITCH=15
    CONST=16
    FALLTHROUGH=17
    IF=18
    RANGE=19
    TYPE=20
    CONTINUE=21
    FOR=22
    IMPORT=23
    RETURN=24
    VAR=25
    NIL_LIT=26
    IDENTIFIER=27
    L_PAREN=28
    R_PAREN=29
    L_CURLY=30
    R_CURLY=31
    L_BRACKET=32
    R_BRACKET=33
    ASSIGN=34
    COMMA=35
    SEMI=36
    COLON=37
    DOT=38
    PLUS_PLUS=39
    MINUS_MINUS=40
    DECLARE_ASSIGN=41
    ELLIPSIS=42
    LOGICAL_OR=43
    LOGICAL_AND=44
    EQUALS=45
    NOT_EQUALS=46
    LESS=47
    LESS_OR_EQUALS=48
    GREATER=49
    GREATER_OR_EQUALS=50
    OR=51
    DIV=52
    MOD=53
    LSHIFT=54
    RSHIFT=55
    BIT_CLEAR=56
    EXCLAMATION=57
    PLUS=58
    MINUS=59
    CARET=60
    STAR=61
    AMPERSAND=62
    RECEIVE=63
    DECIMAL_LIT=64
    OCTAL_LIT=65
    HEX_LIT=66
    FLOAT_LIT=67
    IMAGINARY_LIT=68
    RUNE_LIT=69
    RAW_STRING_LIT=70
    INTERPRETED_STRING_LIT=71
    WS=72
    COMMENT=73
    TERMINATOR=74
    LINE_COMMENT=75

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SourceFileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def packageClause(self):
            return self.getTypedRuleContext(GoParser.PackageClauseContext,0)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def importDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ImportDeclContext)
            else:
                return self.getTypedRuleContext(GoParser.ImportDeclContext,i)


        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(GoParser.FunctionDeclContext,i)


        def methodDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.MethodDeclContext)
            else:
                return self.getTypedRuleContext(GoParser.MethodDeclContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(GoParser.DeclarationContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_sourceFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceFile" ):
                listener.enterSourceFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceFile" ):
                listener.exitSourceFile(self)




    def sourceFile(self):

        localctx = GoParser.SourceFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sourceFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.packageClause()
            self.state = 199
            self.eos()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GoParser.IMPORT:
                self.state = 200
                self.importDecl()
                self.state = 201
                self.eos()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.CONST) | (1 << GoParser.TYPE) | (1 << GoParser.VAR))) != 0):
                self.state = 211
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 208
                    self.functionDecl()
                    pass

                elif la_ == 2:
                    self.state = 209
                    self.methodDecl()
                    pass

                elif la_ == 3:
                    self.state = 210
                    self.declaration()
                    pass


                self.state = 213
                self.eos()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PACKAGE(self):
            return self.getToken(GoParser.PACKAGE, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_packageClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageClause" ):
                listener.enterPackageClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageClause" ):
                listener.exitPackageClause(self)




    def packageClause(self):

        localctx = GoParser.PackageClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_packageClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(GoParser.PACKAGE)
            self.state = 221
            self.match(GoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(GoParser.IMPORT, 0)

        def importSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ImportSpecContext)
            else:
                return self.getTypedRuleContext(GoParser.ImportSpecContext,i)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_importDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportDecl" ):
                listener.enterImportDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportDecl" ):
                listener.exitImportDecl(self)




    def importDecl(self):

        localctx = GoParser.ImportDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(GoParser.IMPORT)
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.IDENTIFIER, GoParser.DOT, GoParser.RAW_STRING_LIT, GoParser.INTERPRETED_STRING_LIT]:
                self.state = 224
                self.importSpec()
                pass
            elif token in [GoParser.L_PAREN]:
                self.state = 225
                self.match(GoParser.L_PAREN)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 27)) & ~0x3f) == 0 and ((1 << (_la - 27)) & ((1 << (GoParser.IDENTIFIER - 27)) | (1 << (GoParser.DOT - 27)) | (1 << (GoParser.RAW_STRING_LIT - 27)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 27)))) != 0):
                    self.state = 226
                    self.importSpec()
                    self.state = 227
                    self.eos()
                    self.state = 233
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 234
                self.match(GoParser.R_PAREN)
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


    class ImportSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def importPath(self):
            return self.getTypedRuleContext(GoParser.ImportPathContext,0)


        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_importSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportSpec" ):
                listener.enterImportSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportSpec" ):
                listener.exitImportSpec(self)




    def importSpec(self):

        localctx = GoParser.ImportSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_importSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GoParser.IDENTIFIER or _la==GoParser.DOT:
                self.state = 237
                _la = self._input.LA(1)
                if not(_la==GoParser.IDENTIFIER or _la==GoParser.DOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 240
            self.importPath()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportPathContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_(self):
            return self.getTypedRuleContext(GoParser.String_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_importPath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportPath" ):
                listener.enterImportPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportPath" ):
                listener.exitImportPath(self)




    def importPath(self):

        localctx = GoParser.ImportPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_importPath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.string_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constDecl(self):
            return self.getTypedRuleContext(GoParser.ConstDeclContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(GoParser.TypeDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(GoParser.VarDeclContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = GoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaration)
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.constDecl()
                pass
            elif token in [GoParser.TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.typeDecl()
                pass
            elif token in [GoParser.VAR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.varDecl()
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


    class ConstDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(GoParser.CONST, 0)

        def constSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ConstSpecContext)
            else:
                return self.getTypedRuleContext(GoParser.ConstSpecContext,i)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_constDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstDecl" ):
                listener.enterConstDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstDecl" ):
                listener.exitConstDecl(self)




    def constDecl(self):

        localctx = GoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(GoParser.CONST)
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.IDENTIFIER]:
                self.state = 250
                self.constSpec()
                pass
            elif token in [GoParser.L_PAREN]:
                self.state = 251
                self.match(GoParser.L_PAREN)
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GoParser.IDENTIFIER:
                    self.state = 252
                    self.constSpec()
                    self.state = 253
                    self.eos()
                    self.state = 259
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 260
                self.match(GoParser.R_PAREN)
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


    class ConstSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_constSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstSpec" ):
                listener.enterConstSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstSpec" ):
                listener.exitConstSpec(self)




    def constSpec(self):

        localctx = GoParser.ConstSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.identifierList()
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.STAR) | (1 << GoParser.RECEIVE))) != 0):
                    self.state = 264
                    self.type_()


                self.state = 267
                self.match(GoParser.ASSIGN)
                self.state = 268
                self.expressionList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.IDENTIFIER)
            else:
                return self.getToken(GoParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_identifierList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierList" ):
                listener.enterIdentifierList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierList" ):
                listener.exitIdentifierList(self)




    def identifierList(self):

        localctx = GoParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifierList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(GoParser.IDENTIFIER)
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 272
                    self.match(GoParser.COMMA)
                    self.state = 273
                    self.match(GoParser.IDENTIFIER) 
                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GoParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = GoParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expressionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.expression(0)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 280
                    self.match(GoParser.COMMA)
                    self.state = 281
                    self.expression(0) 
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(GoParser.TYPE, 0)

        def typeSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.TypeSpecContext)
            else:
                return self.getTypedRuleContext(GoParser.TypeSpecContext,i)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_typeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDecl" ):
                listener.enterTypeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDecl" ):
                listener.exitTypeDecl(self)




    def typeDecl(self):

        localctx = GoParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(GoParser.TYPE)
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.IDENTIFIER]:
                self.state = 288
                self.typeSpec()
                pass
            elif token in [GoParser.L_PAREN]:
                self.state = 289
                self.match(GoParser.L_PAREN)
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GoParser.IDENTIFIER:
                    self.state = 290
                    self.typeSpec()
                    self.state = 291
                    self.eos()
                    self.state = 297
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 298
                self.match(GoParser.R_PAREN)
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


    class TypeSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_typeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpec" ):
                listener.enterTypeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpec" ):
                listener.exitTypeSpec(self)




    def typeSpec(self):

        localctx = GoParser.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(GoParser.IDENTIFIER)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GoParser.ASSIGN:
                self.state = 302
                self.match(GoParser.ASSIGN)


            self.state = 305
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(GoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(GoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(GoParser.BlockContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)




    def functionDecl(self):

        localctx = GoParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(GoParser.FUNC)
            self.state = 308
            self.match(GoParser.IDENTIFIER)

            self.state = 309
            self.signature()
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 310
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(GoParser.FUNC, 0)

        def receiver(self):
            return self.getTypedRuleContext(GoParser.ReceiverContext,0)


        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(GoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(GoParser.BlockContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_methodDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDecl" ):
                listener.enterMethodDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDecl" ):
                listener.exitMethodDecl(self)




    def methodDecl(self):

        localctx = GoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_methodDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(GoParser.FUNC)
            self.state = 314
            self.receiver()
            self.state = 315
            self.match(GoParser.IDENTIFIER)

            self.state = 316
            self.signature()
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 317
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(GoParser.ParametersContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_receiver

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReceiver" ):
                listener.enterReceiver(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReceiver" ):
                listener.exitReceiver(self)




    def receiver(self):

        localctx = GoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.parameters()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GoParser.VAR, 0)

        def varSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.VarSpecContext)
            else:
                return self.getTypedRuleContext(GoParser.VarSpecContext,i)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = GoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(GoParser.VAR)
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.IDENTIFIER]:
                self.state = 323
                self.varSpec()
                pass
            elif token in [GoParser.L_PAREN]:
                self.state = 324
                self.match(GoParser.L_PAREN)
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GoParser.IDENTIFIER:
                    self.state = 325
                    self.varSpec()
                    self.state = 326
                    self.eos()
                    self.state = 332
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 333
                self.match(GoParser.R_PAREN)
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


    class VarSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_varSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarSpec" ):
                listener.enterVarSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarSpec" ):
                listener.exitVarSpec(self)




    def varSpec(self):

        localctx = GoParser.VarSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_varSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.identifierList()
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.FUNC, GoParser.INTERFACE, GoParser.MAP, GoParser.STRUCT, GoParser.CHAN, GoParser.IDENTIFIER, GoParser.L_PAREN, GoParser.L_BRACKET, GoParser.STAR, GoParser.RECEIVE]:
                self.state = 337
                self.type_()
                self.state = 340
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 338
                    self.match(GoParser.ASSIGN)
                    self.state = 339
                    self.expressionList()


                pass
            elif token in [GoParser.ASSIGN]:
                self.state = 342
                self.match(GoParser.ASSIGN)
                self.state = 343
                self.expressionList()
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


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def statementList(self):
            return self.getTypedRuleContext(GoParser.StatementListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = GoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(GoParser.L_CURLY)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.BREAK) | (1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.SELECT) | (1 << GoParser.DEFER) | (1 << GoParser.GO) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.GOTO) | (1 << GoParser.SWITCH) | (1 << GoParser.CONST) | (1 << GoParser.FALLTHROUGH) | (1 << GoParser.IF) | (1 << GoParser.TYPE) | (1 << GoParser.CONTINUE) | (1 << GoParser.FOR) | (1 << GoParser.RETURN) | (1 << GoParser.VAR) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_CURLY) | (1 << GoParser.L_BRACKET) | (1 << GoParser.SEMI) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 347
                self.statementList()


            self.state = 350
            self.match(GoParser.R_CURLY)
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
                return self.getTypedRuleContexts(GoParser.StatementContext)
            else:
                return self.getTypedRuleContext(GoParser.StatementContext,i)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = GoParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 352
                self.statement()
                self.state = 353
                self.eos()
                self.state = 357 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.BREAK) | (1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.SELECT) | (1 << GoParser.DEFER) | (1 << GoParser.GO) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.GOTO) | (1 << GoParser.SWITCH) | (1 << GoParser.CONST) | (1 << GoParser.FALLTHROUGH) | (1 << GoParser.IF) | (1 << GoParser.TYPE) | (1 << GoParser.CONTINUE) | (1 << GoParser.FOR) | (1 << GoParser.RETURN) | (1 << GoParser.VAR) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_CURLY) | (1 << GoParser.L_BRACKET) | (1 << GoParser.SEMI) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0)):
                    break

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

        def declaration(self):
            return self.getTypedRuleContext(GoParser.DeclarationContext,0)


        def labeledStmt(self):
            return self.getTypedRuleContext(GoParser.LabeledStmtContext,0)


        def simpleStmt(self):
            return self.getTypedRuleContext(GoParser.SimpleStmtContext,0)


        def goStmt(self):
            return self.getTypedRuleContext(GoParser.GoStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(GoParser.ReturnStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(GoParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(GoParser.ContinueStmtContext,0)


        def gotoStmt(self):
            return self.getTypedRuleContext(GoParser.GotoStmtContext,0)


        def fallthroughStmt(self):
            return self.getTypedRuleContext(GoParser.FallthroughStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(GoParser.BlockContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(GoParser.IfStmtContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(GoParser.SwitchStmtContext,0)


        def selectStmt(self):
            return self.getTypedRuleContext(GoParser.SelectStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(GoParser.ForStmtContext,0)


        def deferStmt(self):
            return self.getTypedRuleContext(GoParser.DeferStmtContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = GoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statement)
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.labeledStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 361
                self.simpleStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 362
                self.goStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 363
                self.returnStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 364
                self.breakStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 365
                self.continueStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 366
                self.gotoStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 367
                self.fallthroughStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 368
                self.block()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 369
                self.ifStmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 370
                self.switchStmt()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 371
                self.selectStmt()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 372
                self.forStmt()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 373
                self.deferStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sendStmt(self):
            return self.getTypedRuleContext(GoParser.SendStmtContext,0)


        def expressionStmt(self):
            return self.getTypedRuleContext(GoParser.ExpressionStmtContext,0)


        def incDecStmt(self):
            return self.getTypedRuleContext(GoParser.IncDecStmtContext,0)


        def assignment(self):
            return self.getTypedRuleContext(GoParser.AssignmentContext,0)


        def shortVarDecl(self):
            return self.getTypedRuleContext(GoParser.ShortVarDeclContext,0)


        def emptyStmt(self):
            return self.getTypedRuleContext(GoParser.EmptyStmtContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_simpleStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleStmt" ):
                listener.enterSimpleStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleStmt" ):
                listener.exitSimpleStmt(self)




    def simpleStmt(self):

        localctx = GoParser.SimpleStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_simpleStmt)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.sendStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.expressionStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.incDecStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 379
                self.assignment()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 380
                self.shortVarDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 381
                self.emptyStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_expressionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStmt" ):
                listener.enterExpressionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStmt" ):
                listener.exitExpressionStmt(self)




    def expressionStmt(self):

        localctx = GoParser.ExpressionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expressionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SendStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GoParser.ExpressionContext,i)


        def RECEIVE(self):
            return self.getToken(GoParser.RECEIVE, 0)

        def getRuleIndex(self):
            return GoParser.RULE_sendStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSendStmt" ):
                listener.enterSendStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSendStmt" ):
                listener.exitSendStmt(self)




    def sendStmt(self):

        localctx = GoParser.SendStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_sendStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.expression(0)
            self.state = 387
            self.match(GoParser.RECEIVE)
            self.state = 388
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncDecStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def PLUS_PLUS(self):
            return self.getToken(GoParser.PLUS_PLUS, 0)

        def MINUS_MINUS(self):
            return self.getToken(GoParser.MINUS_MINUS, 0)

        def getRuleIndex(self):
            return GoParser.RULE_incDecStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncDecStmt" ):
                listener.enterIncDecStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncDecStmt" ):
                listener.exitIncDecStmt(self)




    def incDecStmt(self):

        localctx = GoParser.IncDecStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_incDecStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.expression(0)
            self.state = 391
            _la = self._input.LA(1)
            if not(_la==GoParser.PLUS_PLUS or _la==GoParser.MINUS_MINUS):
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


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExpressionListContext)
            else:
                return self.getTypedRuleContext(GoParser.ExpressionListContext,i)


        def assign_op(self):
            return self.getTypedRuleContext(GoParser.Assign_opContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = GoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.expressionList()
            self.state = 394
            self.assign_op()
            self.state = 395
            self.expressionList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def PLUS(self):
            return self.getToken(GoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GoParser.MINUS, 0)

        def OR(self):
            return self.getToken(GoParser.OR, 0)

        def CARET(self):
            return self.getToken(GoParser.CARET, 0)

        def STAR(self):
            return self.getToken(GoParser.STAR, 0)

        def DIV(self):
            return self.getToken(GoParser.DIV, 0)

        def MOD(self):
            return self.getToken(GoParser.MOD, 0)

        def LSHIFT(self):
            return self.getToken(GoParser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(GoParser.RSHIFT, 0)

        def AMPERSAND(self):
            return self.getToken(GoParser.AMPERSAND, 0)

        def BIT_CLEAR(self):
            return self.getToken(GoParser.BIT_CLEAR, 0)

        def getRuleIndex(self):
            return GoParser.RULE_assign_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_op" ):
                listener.enterAssign_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_op" ):
                listener.exitAssign_op(self)




    def assign_op(self):

        localctx = GoParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.OR) | (1 << GoParser.DIV) | (1 << GoParser.MOD) | (1 << GoParser.LSHIFT) | (1 << GoParser.RSHIFT) | (1 << GoParser.BIT_CLEAR) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND))) != 0):
                self.state = 397
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.OR) | (1 << GoParser.DIV) | (1 << GoParser.MOD) | (1 << GoParser.LSHIFT) | (1 << GoParser.RSHIFT) | (1 << GoParser.BIT_CLEAR) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 400
            self.match(GoParser.ASSIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortVarDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def DECLARE_ASSIGN(self):
            return self.getToken(GoParser.DECLARE_ASSIGN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_shortVarDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShortVarDecl" ):
                listener.enterShortVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShortVarDecl" ):
                listener.exitShortVarDecl(self)




    def shortVarDecl(self):

        localctx = GoParser.ShortVarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_shortVarDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.identifierList()
            self.state = 403
            self.match(GoParser.DECLARE_ASSIGN)
            self.state = 404
            self.expressionList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(GoParser.SEMI, 0)

        def getRuleIndex(self):
            return GoParser.RULE_emptyStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStmt" ):
                listener.enterEmptyStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStmt" ):
                listener.exitEmptyStmt(self)




    def emptyStmt(self):

        localctx = GoParser.EmptyStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_emptyStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(GoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabeledStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(GoParser.COLON, 0)

        def statement(self):
            return self.getTypedRuleContext(GoParser.StatementContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_labeledStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeledStmt" ):
                listener.enterLabeledStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeledStmt" ):
                listener.exitLabeledStmt(self)




    def labeledStmt(self):

        localctx = GoParser.LabeledStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_labeledStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(GoParser.IDENTIFIER)
            self.state = 409
            self.match(GoParser.COLON)
            self.state = 410
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(GoParser.RETURN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)




    def returnStmt(self):

        localctx = GoParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(GoParser.RETURN)
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 413
                self.expressionList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(GoParser.BREAK, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)




    def breakStmt(self):

        localctx = GoParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(GoParser.BREAK)
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 417
                self.match(GoParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(GoParser.CONTINUE, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_continueStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)




    def continueStmt(self):

        localctx = GoParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(GoParser.CONTINUE)
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 421
                self.match(GoParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOTO(self):
            return self.getToken(GoParser.GOTO, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_gotoStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotoStmt" ):
                listener.enterGotoStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotoStmt" ):
                listener.exitGotoStmt(self)




    def gotoStmt(self):

        localctx = GoParser.GotoStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_gotoStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(GoParser.GOTO)
            self.state = 425
            self.match(GoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FallthroughStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FALLTHROUGH(self):
            return self.getToken(GoParser.FALLTHROUGH, 0)

        def getRuleIndex(self):
            return GoParser.RULE_fallthroughStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFallthroughStmt" ):
                listener.enterFallthroughStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFallthroughStmt" ):
                listener.exitFallthroughStmt(self)




    def fallthroughStmt(self):

        localctx = GoParser.FallthroughStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_fallthroughStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(GoParser.FALLTHROUGH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeferStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFER(self):
            return self.getToken(GoParser.DEFER, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_deferStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeferStmt" ):
                listener.enterDeferStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeferStmt" ):
                listener.exitDeferStmt(self)




    def deferStmt(self):

        localctx = GoParser.DeferStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_deferStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(GoParser.DEFER)
            self.state = 430
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GoParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.BlockContext)
            else:
                return self.getTypedRuleContext(GoParser.BlockContext,i)


        def simpleStmt(self):
            return self.getTypedRuleContext(GoParser.SimpleStmtContext,0)


        def SEMI(self):
            return self.getToken(GoParser.SEMI, 0)

        def ELSE(self):
            return self.getToken(GoParser.ELSE, 0)

        def ifStmt(self):
            return self.getTypedRuleContext(GoParser.IfStmtContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)




    def ifStmt(self):

        localctx = GoParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(GoParser.IF)
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 433
                self.simpleStmt()
                self.state = 434
                self.match(GoParser.SEMI)


            self.state = 438
            self.expression(0)
            self.state = 439
            self.block()
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 440
                self.match(GoParser.ELSE)
                self.state = 443
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [GoParser.IF]:
                    self.state = 441
                    self.ifStmt()
                    pass
                elif token in [GoParser.L_CURLY]:
                    self.state = 442
                    self.block()
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


    class SwitchStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprSwitchStmt(self):
            return self.getTypedRuleContext(GoParser.ExprSwitchStmtContext,0)


        def typeSwitchStmt(self):
            return self.getTypedRuleContext(GoParser.TypeSwitchStmtContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_switchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStmt" ):
                listener.enterSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStmt" ):
                listener.exitSwitchStmt(self)




    def switchStmt(self):

        localctx = GoParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_switchStmt)
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.exprSwitchStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.typeSwitchStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprSwitchStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(GoParser.SWITCH, 0)

        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def simpleStmt(self):
            return self.getTypedRuleContext(GoParser.SimpleStmtContext,0)


        def SEMI(self):
            return self.getToken(GoParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def exprCaseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExprCaseClauseContext)
            else:
                return self.getTypedRuleContext(GoParser.ExprCaseClauseContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_exprSwitchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSwitchStmt" ):
                listener.enterExprSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSwitchStmt" ):
                listener.exitExprSwitchStmt(self)




    def exprSwitchStmt(self):

        localctx = GoParser.ExprSwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exprSwitchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(GoParser.SWITCH)
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 452
                self.simpleStmt()
                self.state = 453
                self.match(GoParser.SEMI)


            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 457
                self.expression(0)


            self.state = 460
            self.match(GoParser.L_CURLY)
            self.state = 464
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GoParser.DEFAULT or _la==GoParser.CASE:
                self.state = 461
                self.exprCaseClause()
                self.state = 466
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 467
            self.match(GoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprCaseClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprSwitchCase(self):
            return self.getTypedRuleContext(GoParser.ExprSwitchCaseContext,0)


        def COLON(self):
            return self.getToken(GoParser.COLON, 0)

        def statementList(self):
            return self.getTypedRuleContext(GoParser.StatementListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_exprCaseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprCaseClause" ):
                listener.enterExprCaseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprCaseClause" ):
                listener.exitExprCaseClause(self)




    def exprCaseClause(self):

        localctx = GoParser.ExprCaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exprCaseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.exprSwitchCase()
            self.state = 470
            self.match(GoParser.COLON)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.BREAK) | (1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.SELECT) | (1 << GoParser.DEFER) | (1 << GoParser.GO) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.GOTO) | (1 << GoParser.SWITCH) | (1 << GoParser.CONST) | (1 << GoParser.FALLTHROUGH) | (1 << GoParser.IF) | (1 << GoParser.TYPE) | (1 << GoParser.CONTINUE) | (1 << GoParser.FOR) | (1 << GoParser.RETURN) | (1 << GoParser.VAR) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_CURLY) | (1 << GoParser.L_BRACKET) | (1 << GoParser.SEMI) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 471
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprSwitchCaseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(GoParser.CASE, 0)

        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def DEFAULT(self):
            return self.getToken(GoParser.DEFAULT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_exprSwitchCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSwitchCase" ):
                listener.enterExprSwitchCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSwitchCase" ):
                listener.exitExprSwitchCase(self)




    def exprSwitchCase(self):

        localctx = GoParser.ExprSwitchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exprSwitchCase)
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.match(GoParser.CASE)
                self.state = 475
                self.expressionList()
                pass
            elif token in [GoParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.match(GoParser.DEFAULT)
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


    class TypeSwitchStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(GoParser.SWITCH, 0)

        def typeSwitchGuard(self):
            return self.getTypedRuleContext(GoParser.TypeSwitchGuardContext,0)


        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def simpleStmt(self):
            return self.getTypedRuleContext(GoParser.SimpleStmtContext,0)


        def SEMI(self):
            return self.getToken(GoParser.SEMI, 0)

        def typeCaseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.TypeCaseClauseContext)
            else:
                return self.getTypedRuleContext(GoParser.TypeCaseClauseContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_typeSwitchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSwitchStmt" ):
                listener.enterTypeSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSwitchStmt" ):
                listener.exitTypeSwitchStmt(self)




    def typeSwitchStmt(self):

        localctx = GoParser.TypeSwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_typeSwitchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(GoParser.SWITCH)
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 480
                self.simpleStmt()
                self.state = 481
                self.match(GoParser.SEMI)


            self.state = 485
            self.typeSwitchGuard()
            self.state = 486
            self.match(GoParser.L_CURLY)
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GoParser.DEFAULT or _la==GoParser.CASE:
                self.state = 487
                self.typeCaseClause()
                self.state = 492
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 493
            self.match(GoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSwitchGuardContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self):
            return self.getTypedRuleContext(GoParser.PrimaryExprContext,0)


        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def TYPE(self):
            return self.getToken(GoParser.TYPE, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def DECLARE_ASSIGN(self):
            return self.getToken(GoParser.DECLARE_ASSIGN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_typeSwitchGuard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSwitchGuard" ):
                listener.enterTypeSwitchGuard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSwitchGuard" ):
                listener.exitTypeSwitchGuard(self)




    def typeSwitchGuard(self):

        localctx = GoParser.TypeSwitchGuardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_typeSwitchGuard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 495
                self.match(GoParser.IDENTIFIER)
                self.state = 496
                self.match(GoParser.DECLARE_ASSIGN)


            self.state = 499
            self.primaryExpr(0)
            self.state = 500
            self.match(GoParser.DOT)
            self.state = 501
            self.match(GoParser.L_PAREN)
            self.state = 502
            self.match(GoParser.TYPE)
            self.state = 503
            self.match(GoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeCaseClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSwitchCase(self):
            return self.getTypedRuleContext(GoParser.TypeSwitchCaseContext,0)


        def COLON(self):
            return self.getToken(GoParser.COLON, 0)

        def statementList(self):
            return self.getTypedRuleContext(GoParser.StatementListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_typeCaseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeCaseClause" ):
                listener.enterTypeCaseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeCaseClause" ):
                listener.exitTypeCaseClause(self)




    def typeCaseClause(self):

        localctx = GoParser.TypeCaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_typeCaseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.typeSwitchCase()
            self.state = 506
            self.match(GoParser.COLON)
            self.state = 508
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.BREAK) | (1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.SELECT) | (1 << GoParser.DEFER) | (1 << GoParser.GO) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.GOTO) | (1 << GoParser.SWITCH) | (1 << GoParser.CONST) | (1 << GoParser.FALLTHROUGH) | (1 << GoParser.IF) | (1 << GoParser.TYPE) | (1 << GoParser.CONTINUE) | (1 << GoParser.FOR) | (1 << GoParser.RETURN) | (1 << GoParser.VAR) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_CURLY) | (1 << GoParser.L_BRACKET) | (1 << GoParser.SEMI) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 507
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSwitchCaseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(GoParser.CASE, 0)

        def typeList(self):
            return self.getTypedRuleContext(GoParser.TypeListContext,0)


        def DEFAULT(self):
            return self.getToken(GoParser.DEFAULT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_typeSwitchCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSwitchCase" ):
                listener.enterTypeSwitchCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSwitchCase" ):
                listener.exitTypeSwitchCase(self)




    def typeSwitchCase(self):

        localctx = GoParser.TypeSwitchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_typeSwitchCase)
        try:
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                self.match(GoParser.CASE)
                self.state = 511
                self.typeList()
                pass
            elif token in [GoParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.match(GoParser.DEFAULT)
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


    class TypeListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.Type_Context)
            else:
                return self.getTypedRuleContext(GoParser.Type_Context,i)


        def NIL_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NIL_LIT)
            else:
                return self.getToken(GoParser.NIL_LIT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_typeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeList" ):
                listener.enterTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeList" ):
                listener.exitTypeList(self)




    def typeList(self):

        localctx = GoParser.TypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_typeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.FUNC, GoParser.INTERFACE, GoParser.MAP, GoParser.STRUCT, GoParser.CHAN, GoParser.IDENTIFIER, GoParser.L_PAREN, GoParser.L_BRACKET, GoParser.STAR, GoParser.RECEIVE]:
                self.state = 515
                self.type_()
                pass
            elif token in [GoParser.NIL_LIT]:
                self.state = 516
                self.match(GoParser.NIL_LIT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 526
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GoParser.COMMA:
                self.state = 519
                self.match(GoParser.COMMA)
                self.state = 522
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [GoParser.FUNC, GoParser.INTERFACE, GoParser.MAP, GoParser.STRUCT, GoParser.CHAN, GoParser.IDENTIFIER, GoParser.L_PAREN, GoParser.L_BRACKET, GoParser.STAR, GoParser.RECEIVE]:
                    self.state = 520
                    self.type_()
                    pass
                elif token in [GoParser.NIL_LIT]:
                    self.state = 521
                    self.match(GoParser.NIL_LIT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 528
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(GoParser.SELECT, 0)

        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def commClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.CommClauseContext)
            else:
                return self.getTypedRuleContext(GoParser.CommClauseContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_selectStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStmt" ):
                listener.enterSelectStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStmt" ):
                listener.exitSelectStmt(self)




    def selectStmt(self):

        localctx = GoParser.SelectStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_selectStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(GoParser.SELECT)
            self.state = 530
            self.match(GoParser.L_CURLY)
            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GoParser.DEFAULT or _la==GoParser.CASE:
                self.state = 531
                self.commClause()
                self.state = 536
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 537
            self.match(GoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commCase(self):
            return self.getTypedRuleContext(GoParser.CommCaseContext,0)


        def COLON(self):
            return self.getToken(GoParser.COLON, 0)

        def statementList(self):
            return self.getTypedRuleContext(GoParser.StatementListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_commClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommClause" ):
                listener.enterCommClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommClause" ):
                listener.exitCommClause(self)




    def commClause(self):

        localctx = GoParser.CommClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_commClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.commCase()
            self.state = 540
            self.match(GoParser.COLON)
            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.BREAK) | (1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.SELECT) | (1 << GoParser.DEFER) | (1 << GoParser.GO) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.GOTO) | (1 << GoParser.SWITCH) | (1 << GoParser.CONST) | (1 << GoParser.FALLTHROUGH) | (1 << GoParser.IF) | (1 << GoParser.TYPE) | (1 << GoParser.CONTINUE) | (1 << GoParser.FOR) | (1 << GoParser.RETURN) | (1 << GoParser.VAR) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_CURLY) | (1 << GoParser.L_BRACKET) | (1 << GoParser.SEMI) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 541
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommCaseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(GoParser.CASE, 0)

        def sendStmt(self):
            return self.getTypedRuleContext(GoParser.SendStmtContext,0)


        def recvStmt(self):
            return self.getTypedRuleContext(GoParser.RecvStmtContext,0)


        def DEFAULT(self):
            return self.getToken(GoParser.DEFAULT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_commCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommCase" ):
                listener.enterCommCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommCase" ):
                listener.exitCommCase(self)




    def commCase(self):

        localctx = GoParser.CommCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_commCase)
        try:
            self.state = 550
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 544
                self.match(GoParser.CASE)
                self.state = 547
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 545
                    self.sendStmt()
                    pass

                elif la_ == 2:
                    self.state = 546
                    self.recvStmt()
                    pass


                pass
            elif token in [GoParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                self.match(GoParser.DEFAULT)
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


    class RecvStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def DECLARE_ASSIGN(self):
            return self.getToken(GoParser.DECLARE_ASSIGN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_recvStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecvStmt" ):
                listener.enterRecvStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecvStmt" ):
                listener.exitRecvStmt(self)




    def recvStmt(self):

        localctx = GoParser.RecvStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_recvStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 552
                self.expressionList()
                self.state = 553
                self.match(GoParser.ASSIGN)

            elif la_ == 2:
                self.state = 555
                self.identifierList()
                self.state = 556
                self.match(GoParser.DECLARE_ASSIGN)


            self.state = 560
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GoParser.FOR, 0)

        def block(self):
            return self.getTypedRuleContext(GoParser.BlockContext,0)


        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def forClause(self):
            return self.getTypedRuleContext(GoParser.ForClauseContext,0)


        def rangeClause(self):
            return self.getTypedRuleContext(GoParser.RangeClauseContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)




    def forStmt(self):

        localctx = GoParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(GoParser.FOR)
            self.state = 566
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 563
                self.expression(0)

            elif la_ == 2:
                self.state = 564
                self.forClause()

            elif la_ == 3:
                self.state = 565
                self.rangeClause()


            self.state = 568
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.SEMI)
            else:
                return self.getToken(GoParser.SEMI, i)

        def simpleStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.SimpleStmtContext)
            else:
                return self.getTypedRuleContext(GoParser.SimpleStmtContext,i)


        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_forClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForClause" ):
                listener.enterForClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForClause" ):
                listener.exitForClause(self)




    def forClause(self):

        localctx = GoParser.ForClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_forClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 570
                self.simpleStmt()


            self.state = 573
            self.match(GoParser.SEMI)
            self.state = 575
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 574
                self.expression(0)


            self.state = 577
            self.match(GoParser.SEMI)
            self.state = 579
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.SEMI) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 578
                self.simpleStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANGE(self):
            return self.getToken(GoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def DECLARE_ASSIGN(self):
            return self.getToken(GoParser.DECLARE_ASSIGN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_rangeClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeClause" ):
                listener.enterRangeClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeClause" ):
                listener.exitRangeClause(self)




    def rangeClause(self):

        localctx = GoParser.RangeClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_rangeClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.state = 581
                self.expressionList()
                self.state = 582
                self.match(GoParser.ASSIGN)

            elif la_ == 2:
                self.state = 584
                self.identifierList()
                self.state = 585
                self.match(GoParser.DECLARE_ASSIGN)


            self.state = 589
            self.match(GoParser.RANGE)
            self.state = 590
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GO(self):
            return self.getToken(GoParser.GO, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_goStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoStmt" ):
                listener.enterGoStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoStmt" ):
                listener.exitGoStmt(self)




    def goStmt(self):

        localctx = GoParser.GoStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_goStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(GoParser.GO)
            self.state = 593
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(GoParser.TypeNameContext,0)


        def typeLit(self):
            return self.getTypedRuleContext(GoParser.TypeLitContext,0)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_type_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_" ):
                listener.enterType_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_" ):
                listener.exitType_(self)




    def type_(self):

        localctx = GoParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_type_)
        try:
            self.state = 601
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 595
                self.typeName()
                pass
            elif token in [GoParser.FUNC, GoParser.INTERFACE, GoParser.MAP, GoParser.STRUCT, GoParser.CHAN, GoParser.L_BRACKET, GoParser.STAR, GoParser.RECEIVE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 596
                self.typeLit()
                pass
            elif token in [GoParser.L_PAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 597
                self.match(GoParser.L_PAREN)
                self.state = 598
                self.type_()
                self.state = 599
                self.match(GoParser.R_PAREN)
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


    class TypeNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def qualifiedIdent(self):
            return self.getTypedRuleContext(GoParser.QualifiedIdentContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_typeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeName" ):
                listener.enterTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeName" ):
                listener.exitTypeName(self)




    def typeName(self):

        localctx = GoParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_typeName)
        try:
            self.state = 605
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 603
                self.match(GoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 604
                self.qualifiedIdent()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeLitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayType(self):
            return self.getTypedRuleContext(GoParser.ArrayTypeContext,0)


        def structType(self):
            return self.getTypedRuleContext(GoParser.StructTypeContext,0)


        def pointerType(self):
            return self.getTypedRuleContext(GoParser.PointerTypeContext,0)


        def functionType(self):
            return self.getTypedRuleContext(GoParser.FunctionTypeContext,0)


        def interfaceType(self):
            return self.getTypedRuleContext(GoParser.InterfaceTypeContext,0)


        def sliceType(self):
            return self.getTypedRuleContext(GoParser.SliceTypeContext,0)


        def mapType(self):
            return self.getTypedRuleContext(GoParser.MapTypeContext,0)


        def channelType(self):
            return self.getTypedRuleContext(GoParser.ChannelTypeContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_typeLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeLit" ):
                listener.enterTypeLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeLit" ):
                listener.exitTypeLit(self)




    def typeLit(self):

        localctx = GoParser.TypeLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_typeLit)
        try:
            self.state = 615
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 607
                self.arrayType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 608
                self.structType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 609
                self.pointerType()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 610
                self.functionType()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 611
                self.interfaceType()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 612
                self.sliceType()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 613
                self.mapType()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 614
                self.channelType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(GoParser.L_BRACKET, 0)

        def arrayLength(self):
            return self.getTypedRuleContext(GoParser.ArrayLengthContext,0)


        def R_BRACKET(self):
            return self.getToken(GoParser.R_BRACKET, 0)

        def elementType(self):
            return self.getTypedRuleContext(GoParser.ElementTypeContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_arrayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayType" ):
                listener.enterArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayType" ):
                listener.exitArrayType(self)




    def arrayType(self):

        localctx = GoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.match(GoParser.L_BRACKET)
            self.state = 618
            self.arrayLength()
            self.state = 619
            self.match(GoParser.R_BRACKET)
            self.state = 620
            self.elementType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLengthContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_arrayLength

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLength" ):
                listener.enterArrayLength(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLength" ):
                listener.exitArrayLength(self)




    def arrayLength(self):

        localctx = GoParser.ArrayLengthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_arrayLength)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_elementType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementType" ):
                listener.enterElementType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementType" ):
                listener.exitElementType(self)




    def elementType(self):

        localctx = GoParser.ElementTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_elementType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(GoParser.STAR, 0)

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_pointerType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointerType" ):
                listener.enterPointerType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointerType" ):
                listener.exitPointerType(self)




    def pointerType(self):

        localctx = GoParser.PointerTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_pointerType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            self.match(GoParser.STAR)
            self.state = 627
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(GoParser.INTERFACE, 0)

        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def methodSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.MethodSpecContext)
            else:
                return self.getTypedRuleContext(GoParser.MethodSpecContext,i)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_interfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceType" ):
                listener.enterInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceType" ):
                listener.exitInterfaceType(self)




    def interfaceType(self):

        localctx = GoParser.InterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_interfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.match(GoParser.INTERFACE)
            self.state = 630
            self.match(GoParser.L_CURLY)
            self.state = 636
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 631
                    self.methodSpec()
                    self.state = 632
                    self.eos() 
                self.state = 638
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

            self.state = 639
            self.match(GoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SliceTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(GoParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(GoParser.R_BRACKET, 0)

        def elementType(self):
            return self.getTypedRuleContext(GoParser.ElementTypeContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_sliceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSliceType" ):
                listener.enterSliceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSliceType" ):
                listener.exitSliceType(self)




    def sliceType(self):

        localctx = GoParser.SliceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_sliceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.match(GoParser.L_BRACKET)
            self.state = 642
            self.match(GoParser.R_BRACKET)
            self.state = 643
            self.elementType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP(self):
            return self.getToken(GoParser.MAP, 0)

        def L_BRACKET(self):
            return self.getToken(GoParser.L_BRACKET, 0)

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def R_BRACKET(self):
            return self.getToken(GoParser.R_BRACKET, 0)

        def elementType(self):
            return self.getTypedRuleContext(GoParser.ElementTypeContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_mapType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapType" ):
                listener.enterMapType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapType" ):
                listener.exitMapType(self)




    def mapType(self):

        localctx = GoParser.MapTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_mapType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self.match(GoParser.MAP)
            self.state = 646
            self.match(GoParser.L_BRACKET)
            self.state = 647
            self.type_()
            self.state = 648
            self.match(GoParser.R_BRACKET)
            self.state = 649
            self.elementType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChannelTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementType(self):
            return self.getTypedRuleContext(GoParser.ElementTypeContext,0)


        def CHAN(self):
            return self.getToken(GoParser.CHAN, 0)

        def RECEIVE(self):
            return self.getToken(GoParser.RECEIVE, 0)

        def getRuleIndex(self):
            return GoParser.RULE_channelType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChannelType" ):
                listener.enterChannelType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChannelType" ):
                listener.exitChannelType(self)




    def channelType(self):

        localctx = GoParser.ChannelTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_channelType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.state = 651
                self.match(GoParser.CHAN)
                pass

            elif la_ == 2:
                self.state = 652
                self.match(GoParser.CHAN)
                self.state = 653
                self.match(GoParser.RECEIVE)
                pass

            elif la_ == 3:
                self.state = 654
                self.match(GoParser.RECEIVE)
                self.state = 655
                self.match(GoParser.CHAN)
                pass


            self.state = 658
            self.elementType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodSpecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def parameters(self):
            return self.getTypedRuleContext(GoParser.ParametersContext,0)


        def result(self):
            return self.getTypedRuleContext(GoParser.ResultContext,0)


        def typeName(self):
            return self.getTypedRuleContext(GoParser.TypeNameContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_methodSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodSpec" ):
                listener.enterMethodSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodSpec" ):
                listener.exitMethodSpec(self)




    def methodSpec(self):

        localctx = GoParser.MethodSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_methodSpec)
        try:
            self.state = 668
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 660
                if not noTerminatorAfterParams(2):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "noTerminatorAfterParams(2)")
                self.state = 661
                self.match(GoParser.IDENTIFIER)
                self.state = 662
                self.parameters()
                self.state = 663
                self.result()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 665
                self.typeName()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 666
                self.match(GoParser.IDENTIFIER)
                self.state = 667
                self.parameters()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(GoParser.FUNC, 0)

        def signature(self):
            return self.getTypedRuleContext(GoParser.SignatureContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_functionType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionType" ):
                listener.enterFunctionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionType" ):
                listener.exitFunctionType(self)




    def functionType(self):

        localctx = GoParser.FunctionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_functionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 670
            self.match(GoParser.FUNC)
            self.state = 671
            self.signature()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignatureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(GoParser.ParametersContext,0)


        def result(self):
            return self.getTypedRuleContext(GoParser.ResultContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_signature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignature" ):
                listener.enterSignature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignature" ):
                listener.exitSignature(self)




    def signature(self):

        localctx = GoParser.SignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_signature)
        try:
            self.state = 678
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 673
                if not noTerminatorAfterParams(1):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "noTerminatorAfterParams(1)")
                self.state = 674
                self.parameters()
                self.state = 675
                self.result()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 677
                self.parameters()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(GoParser.ParametersContext,0)


        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResult" ):
                listener.enterResult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResult" ):
                listener.exitResult(self)




    def result(self):

        localctx = GoParser.ResultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_result)
        try:
            self.state = 682
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 680
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 681
                self.type_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def parameterDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ParameterDeclContext)
            else:
                return self.getTypedRuleContext(GoParser.ParameterDeclContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = GoParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self.match(GoParser.L_PAREN)
            self.state = 696
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.ELLIPSIS) | (1 << GoParser.STAR) | (1 << GoParser.RECEIVE))) != 0):
                self.state = 685
                self.parameterDecl()
                self.state = 690
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 686
                        self.match(GoParser.COMMA)
                        self.state = 687
                        self.parameterDecl() 
                    self.state = 692
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

                self.state = 694
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GoParser.COMMA:
                    self.state = 693
                    self.match(GoParser.COMMA)




            self.state = 698
            self.match(GoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def ELLIPSIS(self):
            return self.getToken(GoParser.ELLIPSIS, 0)

        def getRuleIndex(self):
            return GoParser.RULE_parameterDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterDecl" ):
                listener.enterParameterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterDecl" ):
                listener.exitParameterDecl(self)




    def parameterDecl(self):

        localctx = GoParser.ParameterDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_parameterDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 701
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.state = 700
                self.identifierList()


            self.state = 704
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GoParser.ELLIPSIS:
                self.state = 703
                self.match(GoParser.ELLIPSIS)


            self.state = 706
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self):
            return self.getTypedRuleContext(GoParser.PrimaryExprContext,0)


        def unaryExpr(self):
            return self.getTypedRuleContext(GoParser.UnaryExprContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GoParser.ExpressionContext,i)


        def STAR(self):
            return self.getToken(GoParser.STAR, 0)

        def DIV(self):
            return self.getToken(GoParser.DIV, 0)

        def MOD(self):
            return self.getToken(GoParser.MOD, 0)

        def LSHIFT(self):
            return self.getToken(GoParser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(GoParser.RSHIFT, 0)

        def AMPERSAND(self):
            return self.getToken(GoParser.AMPERSAND, 0)

        def BIT_CLEAR(self):
            return self.getToken(GoParser.BIT_CLEAR, 0)

        def PLUS(self):
            return self.getToken(GoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GoParser.MINUS, 0)

        def OR(self):
            return self.getToken(GoParser.OR, 0)

        def CARET(self):
            return self.getToken(GoParser.CARET, 0)

        def EQUALS(self):
            return self.getToken(GoParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(GoParser.NOT_EQUALS, 0)

        def LESS(self):
            return self.getToken(GoParser.LESS, 0)

        def LESS_OR_EQUALS(self):
            return self.getToken(GoParser.LESS_OR_EQUALS, 0)

        def GREATER(self):
            return self.getToken(GoParser.GREATER, 0)

        def GREATER_OR_EQUALS(self):
            return self.getToken(GoParser.GREATER_OR_EQUALS, 0)

        def LOGICAL_AND(self):
            return self.getToken(GoParser.LOGICAL_AND, 0)

        def LOGICAL_OR(self):
            return self.getToken(GoParser.LOGICAL_OR, 0)

        def getRuleIndex(self):
            return GoParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 140
        self.enterRecursionRule(localctx, 140, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 711
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.state = 709
                self.primaryExpr(0)
                pass

            elif la_ == 2:
                self.state = 710
                self.unaryExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 730
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 728
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
                    if la_ == 1:
                        localctx = GoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 713
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 714
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.DIV) | (1 << GoParser.MOD) | (1 << GoParser.LSHIFT) | (1 << GoParser.RSHIFT) | (1 << GoParser.BIT_CLEAR) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 715
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = GoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 716
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 717
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.OR) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 718
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = GoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 719
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 720
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.EQUALS) | (1 << GoParser.NOT_EQUALS) | (1 << GoParser.LESS) | (1 << GoParser.LESS_OR_EQUALS) | (1 << GoParser.GREATER) | (1 << GoParser.GREATER_OR_EQUALS))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 721
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = GoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 722
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 723
                        self.match(GoParser.LOGICAL_AND)
                        self.state = 724
                        self.expression(3)
                        pass

                    elif la_ == 5:
                        localctx = GoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 725
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 726
                        self.match(GoParser.LOGICAL_OR)
                        self.state = 727
                        self.expression(2)
                        pass

             
                self.state = 732
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(GoParser.OperandContext,0)


        def conversion(self):
            return self.getTypedRuleContext(GoParser.ConversionContext,0)


        def primaryExpr(self):
            return self.getTypedRuleContext(GoParser.PrimaryExprContext,0)


        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def index(self):
            return self.getTypedRuleContext(GoParser.IndexContext,0)


        def slice(self):
            return self.getTypedRuleContext(GoParser.SliceContext,0)


        def typeAssertion(self):
            return self.getTypedRuleContext(GoParser.TypeAssertionContext,0)


        def arguments(self):
            return self.getTypedRuleContext(GoParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_primaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)



    def primaryExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GoParser.PrimaryExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 142
        self.enterRecursionRule(localctx, 142, self.RULE_primaryExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 736
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.state = 734
                self.operand()
                pass

            elif la_ == 2:
                self.state = 735
                self.conversion()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 749
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GoParser.PrimaryExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                    self.state = 738
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 745
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
                    if la_ == 1:
                        self.state = 739
                        self.match(GoParser.DOT)
                        self.state = 740
                        self.match(GoParser.IDENTIFIER)
                        pass

                    elif la_ == 2:
                        self.state = 741
                        self.index()
                        pass

                    elif la_ == 3:
                        self.state = 742
                        self.slice()
                        pass

                    elif la_ == 4:
                        self.state = 743
                        self.typeAssertion()
                        pass

                    elif la_ == 5:
                        self.state = 744
                        self.arguments()
                        pass

             
                self.state = 751
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,75,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self):
            return self.getTypedRuleContext(GoParser.PrimaryExprContext,0)


        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def PLUS(self):
            return self.getToken(GoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GoParser.MINUS, 0)

        def EXCLAMATION(self):
            return self.getToken(GoParser.EXCLAMATION, 0)

        def CARET(self):
            return self.getToken(GoParser.CARET, 0)

        def STAR(self):
            return self.getToken(GoParser.STAR, 0)

        def AMPERSAND(self):
            return self.getToken(GoParser.AMPERSAND, 0)

        def RECEIVE(self):
            return self.getToken(GoParser.RECEIVE, 0)

        def getRuleIndex(self):
            return GoParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)




    def unaryExpr(self):

        localctx = GoParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 755
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 752
                self.primaryExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 753
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 754
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConversionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def COMMA(self):
            return self.getToken(GoParser.COMMA, 0)

        def getRuleIndex(self):
            return GoParser.RULE_conversion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConversion" ):
                listener.enterConversion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConversion" ):
                listener.exitConversion(self)




    def conversion(self):

        localctx = GoParser.ConversionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_conversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 757
            self.type_()
            self.state = 758
            self.match(GoParser.L_PAREN)
            self.state = 759
            self.expression(0)
            self.state = 761
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GoParser.COMMA:
                self.state = 760
                self.match(GoParser.COMMA)


            self.state = 763
            self.match(GoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(GoParser.LiteralContext,0)


        def operandName(self):
            return self.getTypedRuleContext(GoParser.OperandNameContext,0)


        def methodExpr(self):
            return self.getTypedRuleContext(GoParser.MethodExprContext,0)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)




    def operand(self):

        localctx = GoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_operand)
        try:
            self.state = 772
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 765
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 766
                self.operandName()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 767
                self.methodExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 768
                self.match(GoParser.L_PAREN)
                self.state = 769
                self.expression(0)
                self.state = 770
                self.match(GoParser.R_PAREN)
                pass


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

        def basicLit(self):
            return self.getTypedRuleContext(GoParser.BasicLitContext,0)


        def compositeLit(self):
            return self.getTypedRuleContext(GoParser.CompositeLitContext,0)


        def functionLit(self):
            return self.getTypedRuleContext(GoParser.FunctionLitContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = GoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_literal)
        try:
            self.state = 777
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.NIL_LIT, GoParser.DECIMAL_LIT, GoParser.OCTAL_LIT, GoParser.HEX_LIT, GoParser.FLOAT_LIT, GoParser.IMAGINARY_LIT, GoParser.RUNE_LIT, GoParser.RAW_STRING_LIT, GoParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 774
                self.basicLit()
                pass
            elif token in [GoParser.MAP, GoParser.STRUCT, GoParser.IDENTIFIER, GoParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 775
                self.compositeLit()
                pass
            elif token in [GoParser.FUNC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 776
                self.functionLit()
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


    class BasicLitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIL_LIT(self):
            return self.getToken(GoParser.NIL_LIT, 0)

        def integer(self):
            return self.getTypedRuleContext(GoParser.IntegerContext,0)


        def string_(self):
            return self.getTypedRuleContext(GoParser.String_Context,0)


        def FLOAT_LIT(self):
            return self.getToken(GoParser.FLOAT_LIT, 0)

        def IMAGINARY_LIT(self):
            return self.getToken(GoParser.IMAGINARY_LIT, 0)

        def RUNE_LIT(self):
            return self.getToken(GoParser.RUNE_LIT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_basicLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasicLit" ):
                listener.enterBasicLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasicLit" ):
                listener.exitBasicLit(self)




    def basicLit(self):

        localctx = GoParser.BasicLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_basicLit)
        try:
            self.state = 785
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 779
                self.match(GoParser.NIL_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 780
                self.integer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 781
                self.string_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 782
                self.match(GoParser.FLOAT_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 783
                self.match(GoParser.IMAGINARY_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 784
                self.match(GoParser.RUNE_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_LIT(self):
            return self.getToken(GoParser.DECIMAL_LIT, 0)

        def OCTAL_LIT(self):
            return self.getToken(GoParser.OCTAL_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(GoParser.HEX_LIT, 0)

        def IMAGINARY_LIT(self):
            return self.getToken(GoParser.IMAGINARY_LIT, 0)

        def RUNE_LIT(self):
            return self.getToken(GoParser.RUNE_LIT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = GoParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 787
            _la = self._input.LA(1)
            if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)))) != 0)):
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


    class OperandNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def qualifiedIdent(self):
            return self.getTypedRuleContext(GoParser.QualifiedIdentContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_operandName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperandName" ):
                listener.enterOperandName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperandName" ):
                listener.exitOperandName(self)




    def operandName(self):

        localctx = GoParser.OperandNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_operandName)
        try:
            self.state = 791
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 789
                self.match(GoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 790
                self.qualifiedIdent()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedIdentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.IDENTIFIER)
            else:
                return self.getToken(GoParser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_qualifiedIdent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedIdent" ):
                listener.enterQualifiedIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedIdent" ):
                listener.exitQualifiedIdent(self)




    def qualifiedIdent(self):

        localctx = GoParser.QualifiedIdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_qualifiedIdent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 793
            self.match(GoParser.IDENTIFIER)
            self.state = 794
            self.match(GoParser.DOT)
            self.state = 795
            self.match(GoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositeLitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalType(self):
            return self.getTypedRuleContext(GoParser.LiteralTypeContext,0)


        def literalValue(self):
            return self.getTypedRuleContext(GoParser.LiteralValueContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_compositeLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompositeLit" ):
                listener.enterCompositeLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompositeLit" ):
                listener.exitCompositeLit(self)




    def compositeLit(self):

        localctx = GoParser.CompositeLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_compositeLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 797
            self.literalType()
            self.state = 798
            self.literalValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structType(self):
            return self.getTypedRuleContext(GoParser.StructTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(GoParser.ArrayTypeContext,0)


        def L_BRACKET(self):
            return self.getToken(GoParser.L_BRACKET, 0)

        def ELLIPSIS(self):
            return self.getToken(GoParser.ELLIPSIS, 0)

        def R_BRACKET(self):
            return self.getToken(GoParser.R_BRACKET, 0)

        def elementType(self):
            return self.getTypedRuleContext(GoParser.ElementTypeContext,0)


        def sliceType(self):
            return self.getTypedRuleContext(GoParser.SliceTypeContext,0)


        def mapType(self):
            return self.getTypedRuleContext(GoParser.MapTypeContext,0)


        def typeName(self):
            return self.getTypedRuleContext(GoParser.TypeNameContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_literalType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralType" ):
                listener.enterLiteralType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralType" ):
                listener.exitLiteralType(self)




    def literalType(self):

        localctx = GoParser.LiteralTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_literalType)
        try:
            self.state = 809
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 800
                self.structType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 801
                self.arrayType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 802
                self.match(GoParser.L_BRACKET)
                self.state = 803
                self.match(GoParser.ELLIPSIS)
                self.state = 804
                self.match(GoParser.R_BRACKET)
                self.state = 805
                self.elementType()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 806
                self.sliceType()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 807
                self.mapType()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 808
                self.typeName()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def elementList(self):
            return self.getTypedRuleContext(GoParser.ElementListContext,0)


        def COMMA(self):
            return self.getToken(GoParser.COMMA, 0)

        def getRuleIndex(self):
            return GoParser.RULE_literalValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralValue" ):
                listener.enterLiteralValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralValue" ):
                listener.exitLiteralValue(self)




    def literalValue(self):

        localctx = GoParser.LiteralValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 811
            self.match(GoParser.L_CURLY)
            self.state = 816
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_CURLY) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 812
                self.elementList()
                self.state = 814
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GoParser.COMMA:
                    self.state = 813
                    self.match(GoParser.COMMA)




            self.state = 818
            self.match(GoParser.R_CURLY)
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

        def keyedElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.KeyedElementContext)
            else:
                return self.getTypedRuleContext(GoParser.KeyedElementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_elementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementList" ):
                listener.enterElementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementList" ):
                listener.exitElementList(self)




    def elementList(self):

        localctx = GoParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_elementList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 820
            self.keyedElement()
            self.state = 825
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,85,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 821
                    self.match(GoParser.COMMA)
                    self.state = 822
                    self.keyedElement() 
                self.state = 827
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,85,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyedElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(GoParser.ElementContext,0)


        def key(self):
            return self.getTypedRuleContext(GoParser.KeyContext,0)


        def COLON(self):
            return self.getToken(GoParser.COLON, 0)

        def getRuleIndex(self):
            return GoParser.RULE_keyedElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyedElement" ):
                listener.enterKeyedElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyedElement" ):
                listener.exitKeyedElement(self)




    def keyedElement(self):

        localctx = GoParser.KeyedElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_keyedElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 831
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                self.state = 828
                self.key()
                self.state = 829
                self.match(GoParser.COLON)


            self.state = 833
            self.element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def literalValue(self):
            return self.getTypedRuleContext(GoParser.LiteralValueContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = GoParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_key)
        try:
            self.state = 838
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 835
                self.match(GoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 836
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 837
                self.literalValue()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def literalValue(self):
            return self.getTypedRuleContext(GoParser.LiteralValueContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = GoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_element)
        try:
            self.state = 842
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.FUNC, GoParser.INTERFACE, GoParser.MAP, GoParser.STRUCT, GoParser.CHAN, GoParser.NIL_LIT, GoParser.IDENTIFIER, GoParser.L_PAREN, GoParser.L_BRACKET, GoParser.EXCLAMATION, GoParser.PLUS, GoParser.MINUS, GoParser.CARET, GoParser.STAR, GoParser.AMPERSAND, GoParser.RECEIVE, GoParser.DECIMAL_LIT, GoParser.OCTAL_LIT, GoParser.HEX_LIT, GoParser.FLOAT_LIT, GoParser.IMAGINARY_LIT, GoParser.RUNE_LIT, GoParser.RAW_STRING_LIT, GoParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 840
                self.expression(0)
                pass
            elif token in [GoParser.L_CURLY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 841
                self.literalValue()
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


    class StructTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(GoParser.STRUCT, 0)

        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def fieldDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.FieldDeclContext)
            else:
                return self.getTypedRuleContext(GoParser.FieldDeclContext,i)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_structType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructType" ):
                listener.enterStructType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructType" ):
                listener.exitStructType(self)




    def structType(self):

        localctx = GoParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_structType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 844
            self.match(GoParser.STRUCT)
            self.state = 845
            self.match(GoParser.L_CURLY)
            self.state = 851
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,89,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 846
                    self.fieldDecl()
                    self.state = 847
                    self.eos() 
                self.state = 853
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,89,self._ctx)

            self.state = 854
            self.match(GoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def anonymousField(self):
            return self.getTypedRuleContext(GoParser.AnonymousFieldContext,0)


        def string_(self):
            return self.getTypedRuleContext(GoParser.String_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_fieldDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDecl" ):
                listener.enterFieldDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDecl" ):
                listener.exitFieldDecl(self)




    def fieldDecl(self):

        localctx = GoParser.FieldDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_fieldDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 861
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
            if la_ == 1:
                self.state = 856
                if not noTerminatorBetween(2):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "noTerminatorBetween(2)")
                self.state = 857
                self.identifierList()
                self.state = 858
                self.type_()
                pass

            elif la_ == 2:
                self.state = 860
                self.anonymousField()
                pass


            self.state = 864
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                self.state = 863
                self.string_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RAW_STRING_LIT(self):
            return self.getToken(GoParser.RAW_STRING_LIT, 0)

        def INTERPRETED_STRING_LIT(self):
            return self.getToken(GoParser.INTERPRETED_STRING_LIT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_string_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_" ):
                listener.enterString_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_" ):
                listener.exitString_(self)




    def string_(self):

        localctx = GoParser.String_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_string_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 866
            _la = self._input.LA(1)
            if not(_la==GoParser.RAW_STRING_LIT or _la==GoParser.INTERPRETED_STRING_LIT):
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


    class AnonymousFieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(GoParser.TypeNameContext,0)


        def STAR(self):
            return self.getToken(GoParser.STAR, 0)

        def getRuleIndex(self):
            return GoParser.RULE_anonymousField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonymousField" ):
                listener.enterAnonymousField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonymousField" ):
                listener.exitAnonymousField(self)




    def anonymousField(self):

        localctx = GoParser.AnonymousFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_anonymousField)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 869
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GoParser.STAR:
                self.state = 868
                self.match(GoParser.STAR)


            self.state = 871
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionLitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(GoParser.FUNC, 0)

        def signature(self):
            return self.getTypedRuleContext(GoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(GoParser.BlockContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_functionLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionLit" ):
                listener.enterFunctionLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionLit" ):
                listener.exitFunctionLit(self)




    def functionLit(self):

        localctx = GoParser.FunctionLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_functionLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 873
            self.match(GoParser.FUNC)
            self.state = 874
            self.signature()
            self.state = 875
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(GoParser.L_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def R_BRACKET(self):
            return self.getToken(GoParser.R_BRACKET, 0)

        def getRuleIndex(self):
            return GoParser.RULE_index

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex" ):
                listener.enterIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex" ):
                listener.exitIndex(self)




    def index(self):

        localctx = GoParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 877
            self.match(GoParser.L_BRACKET)
            self.state = 878
            self.expression(0)
            self.state = 879
            self.match(GoParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SliceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(GoParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(GoParser.R_BRACKET, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COLON)
            else:
                return self.getToken(GoParser.COLON, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_slice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSlice" ):
                listener.enterSlice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSlice" ):
                listener.exitSlice(self)




    def slice(self):

        localctx = GoParser.SliceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_slice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 881
            self.match(GoParser.L_BRACKET)
            self.state = 897
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,96,self._ctx)
            if la_ == 1:
                self.state = 883
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                    self.state = 882
                    self.expression(0)


                self.state = 885
                self.match(GoParser.COLON)
                self.state = 887
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                    self.state = 886
                    self.expression(0)


                pass

            elif la_ == 2:
                self.state = 890
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                    self.state = 889
                    self.expression(0)


                self.state = 892
                self.match(GoParser.COLON)
                self.state = 893
                self.expression(0)
                self.state = 894
                self.match(GoParser.COLON)
                self.state = 895
                self.expression(0)
                pass


            self.state = 899
            self.match(GoParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeAssertionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_typeAssertion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeAssertion" ):
                listener.enterTypeAssertion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeAssertion" ):
                listener.exitTypeAssertion(self)




    def typeAssertion(self):

        localctx = GoParser.TypeAssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_typeAssertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 901
            self.match(GoParser.DOT)
            self.state = 902
            self.match(GoParser.L_PAREN)
            self.state = 903
            self.type_()
            self.state = 904
            self.match(GoParser.R_PAREN)
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

        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def ELLIPSIS(self):
            return self.getToken(GoParser.ELLIPSIS, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = GoParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 906
            self.match(GoParser.L_PAREN)
            self.state = 921
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 913
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
                if la_ == 1:
                    self.state = 907
                    self.expressionList()
                    pass

                elif la_ == 2:
                    self.state = 908
                    self.type_()
                    self.state = 911
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,97,self._ctx)
                    if la_ == 1:
                        self.state = 909
                        self.match(GoParser.COMMA)
                        self.state = 910
                        self.expressionList()


                    pass


                self.state = 916
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GoParser.ELLIPSIS:
                    self.state = 915
                    self.match(GoParser.ELLIPSIS)


                self.state = 919
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GoParser.COMMA:
                    self.state = 918
                    self.match(GoParser.COMMA)




            self.state = 923
            self.match(GoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def receiverType(self):
            return self.getTypedRuleContext(GoParser.ReceiverTypeContext,0)


        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_methodExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodExpr" ):
                listener.enterMethodExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodExpr" ):
                listener.exitMethodExpr(self)




    def methodExpr(self):

        localctx = GoParser.MethodExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_methodExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 925
            self.receiverType()
            self.state = 926
            self.match(GoParser.DOT)
            self.state = 927
            self.match(GoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(GoParser.TypeNameContext,0)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def STAR(self):
            return self.getToken(GoParser.STAR, 0)

        def receiverType(self):
            return self.getTypedRuleContext(GoParser.ReceiverTypeContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_receiverType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReceiverType" ):
                listener.enterReceiverType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReceiverType" ):
                listener.exitReceiverType(self)




    def receiverType(self):

        localctx = GoParser.ReceiverTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_receiverType)
        try:
            self.state = 938
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 929
                self.typeName()
                pass
            elif token in [GoParser.L_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 930
                self.match(GoParser.L_PAREN)
                self.state = 934
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [GoParser.STAR]:
                    self.state = 931
                    self.match(GoParser.STAR)
                    self.state = 932
                    self.typeName()
                    pass
                elif token in [GoParser.IDENTIFIER, GoParser.L_PAREN]:
                    self.state = 933
                    self.receiverType()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 936
                self.match(GoParser.R_PAREN)
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


    class EosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(GoParser.SEMI, 0)

        def EOF(self):
            return self.getToken(GoParser.EOF, 0)

        def getRuleIndex(self):
            return GoParser.RULE_eos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEos" ):
                listener.enterEos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEos" ):
                listener.exitEos(self)




    def eos(self):

        localctx = GoParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_eos)
        try:
            self.state = 944
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 940
                self.match(GoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 941
                self.match(GoParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 942
                if not lineTerminatorAhead():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "lineTerminatorAhead()")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 943
                if not checkPreviousTokenText("}"):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "checkPreviousTokenText(\"}\")")
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
        self._predicates[64] = self.methodSpec_sempred
        self._predicates[66] = self.signature_sempred
        self._predicates[70] = self.expression_sempred
        self._predicates[71] = self.primaryExpr_sempred
        self._predicates[88] = self.fieldDecl_sempred
        self._predicates[98] = self.eos_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def methodSpec_sempred(self, localctx:MethodSpecContext, predIndex:int):
            if predIndex == 0:
                return noTerminatorAfterParams(2)
         

    def signature_sempred(self, localctx:SignatureContext, predIndex:int):
            if predIndex == 1:
                return noTerminatorAfterParams(1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def primaryExpr_sempred(self, localctx:PrimaryExprContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         

    def fieldDecl_sempred(self, localctx:FieldDeclContext, predIndex:int):
            if predIndex == 8:
                return noTerminatorBetween(2)
         

    def eos_sempred(self, localctx:EosContext, predIndex:int):
            if predIndex == 9:
                return lineTerminatorAhead()
         

            if predIndex == 10:
                return checkPreviousTokenText("}")
         




