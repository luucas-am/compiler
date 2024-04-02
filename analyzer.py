from antlr4 import *
from CompilerLexer import CompilerLexer
from CompilerParser import CompilerParser
from antlr4.tree.Trees import Trees

def valid_cte(token):
    if '+' in token.text or '-' in token.text:
        if len(token.text) > 3:
            print(f"line {token.line}:{token.column} constant length error at: {token.text}")
            return False
    else:
        if len(token.text) > 2:
            print(f"line {token.line}:{token.column} constant length error at: {token.text}")
            return False
    return True

def analyze(input_code:str):
    breakpoint()
    input_code = input_code.upper()
    input_stream = InputStream(input_code)
    lexer = CompilerLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CompilerParser(token_stream)

    tokens = lexer.getAllTokens()
    for token in tokens:
        token_name = lexer.ruleNames[token.type - 1]
        if token_name == 'ID':
            if len(token.text) > 16:
                token.text = token.text[:16] 
        elif token_name == 'CTE':
            if not valid_cte(token):
                continue

        print(f"Token Name: {token_name}, Token Type: {token.type}, Value: '{token.text}'")
    tree = parser.prog();
    tree_str = Trees.toStringTree(tree, None, parser)
    breakpoint()

if __name__ == '__main__':
    input_code = '''
    PROGRAM MyProgram; BEGIN READ (x) END .
    '''
    analyze(input_code)