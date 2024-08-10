from token_type import TokenType


class Token:
    def __int__(self, type: 'TokenType', lexeme, literal, line):
        # Initializing and assigning the attributes of tokens
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f"{self.type} {self.lexeme} {self.literal}"
