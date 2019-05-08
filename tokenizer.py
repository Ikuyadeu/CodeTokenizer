import sys
from collections import Counter
from antlr4 import TerminalNode, InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ConsoleErrorListener
from difflib import ndiff


class TokeNizer():
    IGNORE_CONTENTS = ["NEWLINE", "INDENT", "DEDENT", "ENDMARKER"]
    IGNORE_CONTENTS = ["ENDMARKER"]

    CONTENT = 0
    SYMBOL = 1

    LCS_FLAG = 0
    DIFF_FLAG = 1
    LD_FLAG = 2

    def __init__(self, language: str):
        self.LANGUAGE = language
        if self.LANGUAGE == "Python":
            from .grammers.Python.Python3Parser import Python3Parser as Parser
            from .grammers.Python.Python3Lexer import Python3Lexer as Lexer
            self.VOCABULARY = Parser.symbolicNames
        elif self.LANGUAGE == "Java":
            from .grammers.Java.JavaParser import JavaParser as Parser
            from .grammers.Java.JavaLexer import JavaLexer as Lexer
            self.VOCABULARY = Parser.symbolicNames
        elif self.LANGUAGE == "JavaScript":
            from .grammers.JavaScript.JavaScriptParser import JavaScriptParser as Parser
            from .grammers.JavaScript.JavaScriptLexer import JavaScriptLexer as Lexer
            self.VOCABULARY = Parser.symbolicNames
        elif self.LANGUAGE == "CPP":
            from .grammers.CPP.CPP14Parser import CPP14Parser as Parser
            from .grammers.CPP.CPP14Lexer import CPP14Lexer as Lexer
            self.VOCABULARY = Parser.symbolicNames
        elif self.LANGUAGE == "Ruby":
            return
        else:
            print("Unknown Language, so solve as Python")
            from .grammers.Python.Python3Parser import Python3Parser as Parser
            from .grammers.Python.Python3Lexer import Python3Lexer as Lexer
            self.VOCABULARY = Parser.symbolicNames

        self.Parser = Parser
        self.Lexer = Lexer

    def getTokens(self, code):
        if self.LANGUAGE == "Ruby":
            import subprocess, json
            exclude_tokens = ["\n", " "]

            try:
                out = subprocess.Popen(['ruby', 'tokenizer.rb'], 
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT)
                stdout, _ = out.communicate(input=code.encode())
            except:
                return []
            s = json.loads(stdout.decode('utf-8'))
            strings = [x["string"] for x in s if x["string"] not in exclude_tokens]
            return strings
        return self.makeTokens(self.getTree(code), [])

    def getPureTokens(self, code):
        return [x[0] for x in self.getTokens(code) if not (x[0].startswith("<") and x[0].endswith(">"))]

    def set_code(self, code_a: str, code_b: str):
        self.code_a = code_a
        self.code_b = code_b
        self.tokens_a = self.makeTokens(self.getTree(code_a), [])
        self.tokens_b = self.makeTokens(self.getTree(code_b), [])

    def set_diff(self, flag: int):
        if flag == self.LCS_FLAG:
            self.diff = self.makeNotLCS()
        elif flag == self.DIFF_FLAG:
            self.diff = self.makeNotDup()
        elif flag == self.LD_FLAG:
            self.diff = self.makeLD()
        else:
            self.diff = self.makeNotDup()

    def isInstanceChange(self, instance_name):
        return any([token[self.SYMBOL] == instance_name for token in self.diff])

    def getTokenCount(self, code: str):
        tree = self.getTree(code)
        tokens = self.makeTokens(tree, [])
        return len(tokens)

    def getTree(self, code: str):
        code = code.strip()
        lexer = self.Lexer(InputStream(code))
        stream = CommonTokenStream(lexer)
        parser = self.Parser(stream)
        parser.removeErrorListeners()
        if self.LANGUAGE == "Python":
            tree = parser.file_input()
        elif self.LANGUAGE == "Java":
            tree = parser.compilationUnit()
        elif self.LANGUAGE == "JavaScript":
            tree = parser.program()
        elif self.LANGUAGE == "CPP":
            tree = parser.translationunit()
        else:
            tree = parser.single_input()

        return tree

    def makeTokens(self, tree, tokens: list):
        if isinstance(tree, TerminalNode):
            symbollic_name = self.VOCABULARY[tree.symbol.type]
            if symbollic_name not in self.IGNORE_CONTENTS:
                token = (tree.getText(), symbollic_name)
                tokens.append(token)
        for i in range(tree.getChildCount()):
            tree2 = tree.getChild(i)
            self.makeTokens(tree2, tokens)
        return tokens

    def makeNotLCS(self):
        """
        Not Longest Commmon SubSequence(not SubString)
        """
        lcl_result = Counter(self.makeLCS())
        sub_lcl_a = list((Counter(self.tokens_a) - lcl_result).elements())
        sub_lcl_b = list((Counter(self.tokens_b) - lcl_result).elements())
        return sub_lcl_a + sub_lcl_b

    def makeLCS(self):
        """
        Longest Commmon SubSequence(not SubString)
        """
        lengths = [[0 for j in range(len(self.tokens_b)+1)]
                   for i in range(len(self.tokens_a)+1)]
        # row 0 and column 0 are initialized to 0 already
        for i, x in enumerate(self.tokens_a):
            for j, y in enumerate(self.tokens_b):
                if x == y:
                    lengths[i+1][j+1] = lengths[i][j] + 1
                else:
                    lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
        # read the substring out from the matrix
        result = []
        x, y = len(self.tokens_a), len(self.tokens_b)
        while x != 0 and y != 0:
            if lengths[x][y] == lengths[x-1][y]:
                x -= 1
            elif lengths[x][y] == lengths[x][y-1]:
                y -= 1
            else:
                assert self.tokens_a[x-1] == self.tokens_b[y-1]
                result.append(self.tokens_a[x-1])
                x -= 1
                y -= 1
        return result

    def makeLD(self):
        """
        Levenshtein Distance
        """
        s = self.tokens_a
        t = self.tokens_b
        rows = len(s)+1
        cols = len(t)+1
        dist = [[0 for x in range(cols)] for x in range(rows)]
        dist2 = [[[] for x in range(cols)] for x in range(rows)]
        # source prefixes can be transformed into empty strings
        # by deletions:
        for i in range(1, rows):
            dist[i][0] = i
            # dist2[i][0].append(s[i - 1])
            dist2[i][0] = dist2[i-1][0] + [s[i-1]]
        # target prefixes can be created from an empty source string
        # by inserting the characters
        for i in range(1, cols):
            dist[0][i] = i
            # dist2[0][i] = dist2[0][i-1] + [t[i-1]]
            dist2[0][i].append(t[i - 1])
        col0 = 0
        row0 = 0
        for col in range(1, cols):
            col0 = col
            for row in range(1, rows):
                row0 = row
                deletion = dist[row-1][col] + 1
                insertion = dist[row][col-1] + 1
                substitution = dist[row-1][col-1] + int(s[row-1] != t[col-1])
                values = [substitution, insertion, deletion]
                dist[row][col] = min(values)
                if dist[row][col] == substitution:
                    if s[row-1] != t[col-1]:
                        # print([s[row-1], t[col-1]])
                        dist2[row][col] = dist2[row-1][col-1] + [t[col-1]]
                    else:
                        dist2[row][col] = dist2[row-1][col-1]
                elif dist[row][col] == insertion:
                    dist2[row][col] = dist2[row][col-1] + [t[col-1]]
                elif dist[row][col] == deletion:
                    dist2[row][col] = dist2[row-1][col] + [s[row-1]]

        return dist2[row0][col0]

    def makeNotDup(self):
        c_a = Counter(self.tokens_a)
        c_b = Counter(self.tokens_b)
        return list((c_a - c_b).elements()) + list((c_b - c_a).elements())

    def make_change_set(self, source, target):
        change_set = {}
        try:
            change_set = {
                "a": self.getPureTokens(source),
                "b": self.getPureTokens(target)
            }
        except Exception as identifier:
            print(identifier)
            return -1

        # Skip Operation of New file, Remove file, Adjust Space
        if len(change_set["a"]) == 0 or\
            len(change_set["b"]) == 0 or\
                change_set["a"] == change_set["b"]:
            return -1
        diffs = list(
            ndiff(change_set["a"], change_set["b"], charjunk=IS_CHARACTER_JUNK))
        return clean_diff(diffs)


def IS_CHARACTER_JUNK(ch, ws=" \t\n"):
    return ch in ws


def clean_diff(diffs):
    return [x for x in diffs if not x.startswith("?")]


def main():
    code = [["a=0", "if a.isEmpty():"], ["print(\"hello\")"], [
        """
        a= b
        b=c
        c=0
        """]]
    TN = TokeNizer("Python")
    print(TN.getPureTokens(code[2][0]))


if __name__ == '__main__':
    main()
