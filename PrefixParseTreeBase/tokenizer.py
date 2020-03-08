
class Tokenizer:
    def __init__(self, str_statement):
        self.statement = str_statement
        self.position = 0

    def get_next_token(self):
        i = self.position
        while i < len(self.statement) and self.statement[i] != " ":
            i += 1
        ret_val = self.statement[self.position:i]
        self.position = i + 1
        #print('Herna Tokenizer',ret_val)
        return ret_val
