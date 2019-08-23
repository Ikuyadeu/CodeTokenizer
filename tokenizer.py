import sys
from collections import Counter
from antlr4 import TerminalNode, InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ConsoleErrorListener
from difflib import ndiff, SequenceMatcher, Differ, ndiff


class TokeNizer():
    IGNORE_CONTENTS = ["ENDMARKER","DEDENT"]
    IDENTIFIER_TAG = ""

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
            self.IDENTIFIER_TAG = "NAME"
            self.STRING_TAG = "STRING"  
            self.NUMBER_TAG = "NUMBER"
            self.VOCABULARY = Parser.symbolicNames
        elif self.LANGUAGE == "Java":
            from .grammers.Java.JavaParser import JavaParser as Parser
            from .grammers.Java.JavaLexer import JavaLexer as Lexer
            self.IDENTIFIER_TAG = "IDENTIFIER"
            self.STRING_TAG = "STRING_LITERAL"
            self.NUMBER_TAG = "DECIMAL_LITERAL"
            self.VOCABULARY = Parser.symbolicNames
        elif self.LANGUAGE == "JavaScript":
            from .grammers.JavaScript.JavaScriptParser import JavaScriptParser as Parser
            from .grammers.JavaScript.JavaScriptLexer import JavaScriptLexer as Lexer
            self.VOCABULARY = Parser.symbolicNames
            self.IDENTIFIER_TAG = "Identifier"
            self.STRING_TAG = "StringLiteral"
            self.NUMBER_TAG = "DecimalLiteral"
        elif self.LANGUAGE == "CPP":
            from .grammers.CPP.CPP14Parser import CPP14Parser as Parser
            from .grammers.CPP.CPP14Lexer import CPP14Lexer as Lexer
            self.VOCABULARY = Parser.symbolicNames
            self.IDENTIFIER_TAG = "Identifier"
            self.STRING_TAG = "Stringliteral"
            self.NUMBER_TAG = "Integerliteral"
        elif self.LANGUAGE == "Ruby":
            self.IDENTIFIER_TAG = "ident"
            self.STRING_TAG = "tstring_content"
            self.NUMBER_TAG = "int"
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

            try:
                out = subprocess.Popen(['ruby', 'tokenizer.rb'], 
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT)
                stdout, _ = out.communicate(input=code.encode())
            except:
                return []
            s = json.loads(stdout.decode('utf-8'))
            strings = self.makeRubySpace(s)
            return strings
        return self.makeTokens(self.getTree(code), [])

    def makeRubySpace(self, strings):
        tokens = []
        for i, s in enumerate([x for x in strings if x["string"] not in [" ", "\n"]]):
            if i > 0:
                before_index = tokens[-1][3] + len(tokens[-1][0])
            else:
                before_index = 0
            start = s["position"]["column"]
            space = start - before_index            
            tokens.append((s["string"], s["type"], space, start))
        return tokens

    def getPureTokens(self, code):
        try:
            if self.LANGUAGE == "Ruby":
                return [x for x in self.getTokens(code) if not (x[0].startswith("<") and x[0].endswith(">"))]
            return [x[0] for x in self.getTokens(code) if not (x[0].startswith("<") and x[0].endswith(">"))]
        except:
            return []

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
                if len(tokens) > 0:
                    before_index = tokens[-1][3] + len(tokens[-1][0])
                else:
                    before_index = 0
                start = tree.getPayload().start
                space = start - before_index
                string = tree.getText()
                if not string.startswith("<missing"):
                    tokens.append((string, symbollic_name, space, start))
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
        change_set = {
            "a": self.getPureTokens(source),
            "b": self.getPureTokens(target)
        }

        # Skip Operation of New file, Remove file, Adjust Space
        if len(change_set["a"]) == 0 or\
            len(change_set["b"]) == 0 or\
                change_set["a"] == change_set["b"]:
            return -1
        diffs = list(
            ndiff(change_set["a"], change_set["b"], charjunk=IS_CHARACTER_JUNK))
        return clean_diff(diffs)

    def make_change_set2(self, source, target):

        change_set = {}
        change_set = {
            "a": self.getPureTokens(source),
            "b": self.getPureTokens(target)
        }

        if len(change_set["a"]) == 0 or\
            len(change_set["b"]) == 0 or\
                change_set["a"] == change_set["b"]:
            return -1

        opcodes = SequenceMatcher(None, change_set["a"], change_set["b"]).get_opcodes()
        diffs = []

        for tag, a_i1, a_i2, b_i1, b_i2 in opcodes:
            symbol = opt_tag2symbol(tag)
            if symbol == "*":
                change_a = devide_token_sequence(change_set["a"][a_i1:a_i2])
                change_b = devide_token_sequence(change_set["b"][b_i1:b_i2])
                if len(change_a) <= 1 and len(change_a) <= 1:
                    sequence = [" ".join([symbol] + change_a[0] + ["-->"] + change_b[0])]
                else:
                    a_out =  [" ".join(["-"] + x) for x in change_a]
                    b_out =  [" ".join(["+"] + x) for x in change_b]
                    sequence = a_out + b_out
            elif symbol == "-":
                out = change_set["a"][a_i1:a_i2]
                sequence = [" ".join([symbol] + x) for x in devide_token_sequence(out)]
            elif symbol == "+":
                out = change_set["b"][b_i1:b_i2]
                sequence = [" ".join([symbol] + x) for x in devide_token_sequence(out)]
            elif symbol == "=":
                out = devide_token_sequence(change_set["b"][b_i1:b_i2])
                sequence = [" ".join([symbol] + x) for x in out]
                diffs.extend(sequence)
            else:
                continue
            diffs.extend(sequence)            
        return diffs

    def make_change_set_line(self, source, target):
        differ = Differ().compare(source, target)
        differ = ndiff(source.splitlines(keepends=True),
                       target.splitlines(keepends=True))
        previous_symbol = " "
        previous_tokens = []
        out = []
        for diff in differ:
            symbol = diff[0]
            if len(diff) < 3 or symbol == "?":
                continue
            if symbol == " ":
                continue
            elif symbol == "-":
                token = self.getPureTokens(diff[2:])
                if token == []:
                    continue
                if previous_symbol == "-":
                    out.append([("-", previous_tokens)])
                elif previous_symbol == "+":
                    changed_tokens = self.get_lines_diff(previous_tokens, token)
                    token = []
                    if changed_tokens != []:
                        out.append(changed_tokens)
            elif symbol == "+":
                token = self.getPureTokens(diff[2:])
                if token == []:
                    continue
                if previous_symbol == "+":
                    out.append([("+", previous_tokens)])
                if previous_symbol == "-":
                    changed_tokens = self.get_lines_diff(previous_tokens, token)
                    token = []
                    if changed_tokens != []:
                        out.append(changed_tokens)
            previous_symbol = symbol
            previous_tokens = token
        if previous_symbol in ["+", "-"]:
            out.append([{"tag": previous_symbol, "tokens": previous_tokens}])
        return out
    
    def get_lines_diff(self, previous_tokens, token):
        changed_tokens = []
        matcher = SequenceMatcher(None,
        previous_tokens, token)
        for tag, a_i1, a_i2, b_i1, b_i2 in matcher.get_opcodes():
            symbol2 = opt_tag2symbol(tag)
            if symbol2 == "*":
                changed_tokens.append({"tag": symbol2, "tokens": [previous_tokens[b_i1:b_i2], token[a_i1:a_i2]]})
            elif symbol2 == "-":
                changed_tokens.append({"tag": symbol2, "tokens": previous_tokens[a_i1:a_i2]})
            elif symbol2 == "+":
                changed_tokens.append({"tag": symbol2, "tokens": token[b_i1:b_i2]})
            elif symbol2 == "=":
                changed_tokens.append({"tag": symbol2, "tokens":  token[b_i1:b_i2]})
            else:
                continue
        return changed_tokens

    def get_abstract_tree_diff(self, source, target):
        tokens_a = clean_symbol(self.getTokens(source))
        tokens_b = clean_symbol(self.getTokens(target))

        abstract_index = 0
        abstracted_identifiers = {}
        for i, token_a in [x for x in enumerate(tokens_a)
                        if x[1][1] in [self.IDENTIFIER_TAG, self.STRING_TAG, self.NUMBER_TAG]]:
            if token_a[0] in abstracted_identifiers:
                tokens_a[i] = (f"${{{abstracted_identifiers[token_a[0]]}:{token_a[1]}}}", "ABSTRACT_SNIPPET", token_a[2], token_a[3])
                continue

            for j, token_b in [x for x in enumerate(tokens_b)
                            if x[1][1] in [self.IDENTIFIER_TAG, self.STRING_TAG, self.NUMBER_TAG]]:
                if token_b[0] in abstracted_identifiers:
                    tokens_b[j] = (f"${{{abstracted_identifiers[token_b[0]]}:{token_b[1]}}}", "ABSTRACT_SNIPPET", token_b[2], token_b[3])
                    continue
                elif token_a[0] == token_b[0] and i + 1 < len(tokens_a) and tokens_a[i+1][0] != "(":
                    tokens_a[i] = (f"${{{abstract_index}:{token_a[1]}}}", "ABSTRACT_SNIPPET", token_a[2], token_a[3])
                    tokens_b[j] = (f"${{{abstract_index}:{token_b[1]}}}", "ABSTRACT_SNIPPET", token_b[2], token_b[3])
                    abstracted_identifiers[token_a[0]] = abstract_index
                    abstract_index += 1
        non_abstracted_identifiers = {"condition": list(set([x[0] for x in tokens_a
                                                    if x[1] == self.IDENTIFIER_TAG])),
                                      "consequent": list(set([x[0] for x in tokens_b
                                                     if x[1] == self.IDENTIFIER_TAG]))}
        real_condition = tokens2Realcode(tokens_a)
        real_consequent = tokens2Realcode(tokens_b)
        if isIdentifiersReplace(real_condition, real_consequent, non_abstracted_identifiers):
            return {"condition": non_abstracted_identifiers["condition"][0],
                    "consequent": non_abstracted_identifiers["consequent"][0],
                    "identifiers": non_abstracted_identifiers}
        else:
            return {"condition": real_condition,
                    "consequent": real_consequent,
                    "identifiers": non_abstracted_identifiers}

def tokens2Realcode(tokens):
    return "".join([" " * x[2] + x[0] for x in tokens])

def isIdentifiersReplace(condition, consequent, identifiers):
    condition_set = set(identifiers["condition"])
    consequent_set = set(identifiers["consequent"])
    origin_condition = list(condition_set - consequent_set)
    origin_consequent = list(consequent_set - condition_set)
    return len(origin_condition) == len(origin_consequent) == 1 and\
           condition.replace(origin_condition[0], origin_consequent[0]) == consequent

def opt_tag2symbol(opt_tag):
    if opt_tag == "replace":
        return "*"
    elif opt_tag == "delete":
        return "-"
    elif opt_tag == "insert":
        return "+"
    elif opt_tag == "equal":
        return "="
    else:
        return "?"

def devide_token_sequence(sequence):
    if " " not in sequence:
        return [sequence]
    new_sequence = []
    indexes = [i for i, x in enumerate(sequence) if x in [" ", "\n", "\t"]]
    previous_index = 0
    for index in indexes:
        new_sequence.append(sequence[previous_index+1:index])
        previous_index = index
    if previous_index + 1 != len(sequence):
        new_sequence.append(sequence[previous_index+1:])
    return new_sequence

def IS_CHARACTER_JUNK(ch, ws=" \t\n"):
    return ch in ws

def clean_diff(diffs):
    return [x for x in diffs if not x.startswith("?")]

def clean_symbol(tokens):
    return [("\n", "NEWLINE", x[2], x[3]) if x[1] == "NEWLINE" else\
            ("\t", "INDENT", x[2], x[3]) if x[1] == "INDENT" else x for x in tokens]


def main():
    code = [[
"""for i in range(len(my_array)):
    element = my_array[i]
    for a in b:
        pass""",
"""for i, element in enumerate(my_array):"""],
["""

for (i in range(len(my_array))){
    element = my_array[i]}""",
"""

for (i, element in enumerate(my_array)){}"""],
[
""" 
def some_method(arg1=:default, arg2=nil, arg3=[])
  a = c
end
""",
"""
def some_method(arg1 = :default, arg2 = nil, arg3 = [])
  a = b
end
"""
],
[
"""
tf.scalar_summary('regularization_loss', regularization_loss,
name='regularization_loss')
""",
"""
tf.summary.scalar('regularization_loss', regularization_loss)
"""
],
[
"""
print("hello", 2)
""",
"""
printf("hello", hhh)
"""
],
[
"""
    bisect_tests(options.bisect, options, options.modules, options.parallel)
""",
"""
    bisect_tests(
        options.bisect, options, options.modules, options.parallel,
        options.start_at, options.start_after,
    )
"""
]

]
    TN = TokeNizer("Python")
    expect_out = [
    {
        "condition": ["for ${1:i} in range(len(${2:my_array})):",
                       "\t${3:element} = ${2:array}[${1:element}]"],
        "consequent": ["for ${1:i}, ${3:element} in enumerate(${2:my_array}):"]
    }
    ]

    target = code[5]
    result = TN.get_abstract_tree_diff(target[0], target[1])
    condition = result["condition"]
    consequent = result["consequent"]
    # print(result)

    print(f"inputA:\n{target[0]}")
    print(condition)
    print(f"inputB:\n{target[1]}")
    print(consequent)




if __name__ == '__main__':
    main()
