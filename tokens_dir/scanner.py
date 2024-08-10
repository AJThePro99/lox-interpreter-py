from token_type import TokenType
from token_class import Token


class Scanner:
    # Creating a scanner class for tokenizing the cl arguments
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
# TODO: Scanner Implementation