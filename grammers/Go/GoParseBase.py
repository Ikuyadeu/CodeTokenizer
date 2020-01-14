from antlr4 import *

class GoParserBase(Parser):
    def lineTerminatorAhead(self) -> bool:
        """
        Returns {@code true} iff on the current index of the parser's
        token stream a token exists on the {@code HIDDEN} channel which
        either is a line terminator, or is a multi line comment that
        contains a line terminator.

        :return: {@code true} iff on the current index of the parser's
        token stream a token exists on the {@code HIDDEN} channel which
        either is a line terminator, or is a multi line comment that
        contains a line terminator.
        """
        from .GoParser import GoParser

        # Get the token ahead of the current index.
        possibleIndexEosToken: Token = self.getCurrentToken().tokenIndex - 1
        ahead: Token = self._input.get(possibleIndexEosToken)

        if ahead.channel != Lexer.HIDDEN:
            # We're only interested in tokens on the HIDDEN channel.
            return False

        if ahead.type == GoParser.TERMINATOR:
            # There is definitely a line terminator ahead.
            return True

        if ahead.type == GoParser.WS:
            # Get the token ahead of the current whitespaces.
            possibleIndexEosToken = self.getCurrentToken().tokenIndex - 2
            ahead = self._input.get(possibleIndexEosToken)

        # Get the token's text and type.
        text = ahead.text
        tokenType = ahead.type

        # Check if the token is, or contains a line terminator.
        return ((tokenType == GoParser.COMMENT and (text.contains("\r") or text.contains("\n"))) or
                (tokenType == GoParser.TERMINATOR))
    def noTerminatorBetween(self, tokenOffset) -> bool:
        s = self.getTokenStream()
        stream = s.(CommonTokenStream)
        

    def noTerminatorAfterParams(self, tokenOffset) -> bool:
        pass

    def checkPreviousTokenText(self, text) -> bool:
        stream = self.getTokenStream()
        return stream.__lt__(1)