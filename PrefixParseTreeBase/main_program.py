
import sys
from enum import Enum
from tokenizer import Tokenizer

class DivisionByZero(Exception):
    pass

class UnknownInTree(Exception):
    pass

class OutputFormat(Enum):
    PREFIX = 0
    INFIX = 1
    POSTFIX = 2
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class PrefixParseTree:
    def __init__(self):
        self.tree_value = 0


    def prefix_parser_recursive(self, tokenizer):
        token = tokenizer.get_next_token()
        # print(token) # debug line
        print('inapp tokenizer: ', token)
        if token.isdigit():
            return int(token)
        elif token == "+":
            return self.prefix_parser_recursive(tokenizer) + self.prefix_parser_recursive(tokenizer)
        elif token == "-":
            return self.prefix_parser_recursive(tokenizer) - self.prefix_parser_recursive(tokenizer)
        elif token == "*":
            return self.prefix_parser_recursive(tokenizer) * self.prefix_parser_recursive(tokenizer)
        elif token == "/":
            val1 = self.prefix_parser_recursive(tokenizer)
            val2 = self.prefix_parser_recursive(tokenizer)
            if(val2 == 0):
                raise DivisionByZero
            return val1 / val2
        
        return 0

    def operator_check(self, opertator):
        if opertator == '+' or opertator =='-' or opertator == '*' or opertator == '/':
            return True
        else:
            return False

    def load_statement_string(self, statement):
        tree_stack = []
        tokenizer = Tokenizer(statement)
        self.tree_value = self.prefix_parser_recursive(tokenizer)

        for x in statement:
            if self.operator_check(x) == False:
                temp_char = BinaryTree(x)
                tree_stack.append(temp_char)
            else:
                #  Pop two top node
                temp_char = BinaryTree(x)
                temp_1 = tree_stack.pop()
                temp_2 = tree_stack.pop()
                #  make childrens
                temp_char.right = temp_1
                temp_char.left = temp_2
                #  add subsection
                tree_stack.append(temp_char)
            #  make root
            root = tree_stack.pop()
            print(root)
            return root


    def set_format(self, out_format):
        self.format = out_format

    def root_value(self):
        return self.tree_value

    def simplify_tree(self):
        pass

    def solve_tree(self, root_value):
        pass

    def __str__(self):
        if self.format == 0:
            pass
        if self.format == 1:
            pass
        if self.format == 2:
            pass
        else:
            return ""


# This is a tester function to test that
# the output and/or error message from the
# prefix_tree operations are correct.
def test_prefix_parser(str_statement, solve = False, root_value = 0):

    if solve == True:
        prefix_tree = PrefixParseTree()
        prefix_tree.load_statement_string(str_statement)
        print("PREFIX: " + str(prefix_tree))
        print("The value of x if the root_value is " + str(root_value) + " is: " + str(prefix_tree.solve_tree(root_value)))
    else:
        prefix_tree = PrefixParseTree()
        prefix_tree.load_statement_string(str_statement)
        print("PREFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.INFIX)
        print("INFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.POSTFIX)
        print("POSTFIX: " + str(prefix_tree))

        str_print = "The value of the tree is: "
        try:
            str_print += str(prefix_tree.root_value())
        except DivisionByZero:
            str_print += str("A division by zero occurred")
        except UnknownInTree:
            str_print += str("There is an unknown value in the tree")
        print(str_print)

        print("SIMPLIFIED:")
        prefix_tree.simplify_tree()
        prefix_tree.set_format(OutputFormat.PREFIX)
        print("PREFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.INFIX)
        print("INFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.POSTFIX)
        print("POSTFIX: " + str(prefix_tree))

    print("\n\n")


if __name__ == "__main__":
    #org_out = sys.stdout
    #fout = open(sys.path[0] + "/parse_out.txt", "w+")
    #sys.stdout = fout
    #f = open(sys.path[0] + "/prefix_statements.txt", "r")
    #previous_line = None
    #for line in f:
    #    some_split = line.split()
    #    if some_split[0] == "solve":
    #        test_prefix_parser(previous_line.strip(), True, int(some_split[1]))
    #    test_prefix_parser(line.strip())
    #    previous_line = line
    #f.close()
    #sys.stdout = org_out
    #fout.close()
    tt = PrefixParseTree()
    tt.load_statement_string('* + 7 0 * 6 2 ')
    print(tt.root_value())
    
