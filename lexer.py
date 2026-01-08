import re

def lexer_analysis(filename):
    with open(filename, "r") as file:
        code = file.read()

    token_specification = [
        ('KEYWORD', r'\b(if|else|for|in|print|break|int|input|range)\b'),
        ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
        ('NUMBER', r'\b\d+\b'),
        ('OPERATOR', r'[=<>%+]'),
        ('SEPARATOR', r'[():]'),
        ('STRING', r'"[^"]*"'),
        ('NEWLINE', r'\n'),
        ('SKIP', r'[ \t]+'),
        ('MISMATCH', r'.')
    ]

    tok_regex = '|'.join(f'(?P<{name}>{pattern})'
                         for name, pattern in token_specification)

    print("LEXICAL ANALYSIS OUTPUT:\n")

    for match in re.finditer(tok_regex, code):
        token_type = match.lastgroup
        token_value = match.group()

        if token_type in ('SKIP', 'NEWLINE'):
            continue
        elif token_type == 'MISMATCH':
            print(f'INVALID TOKEN -> {token_value}')
        else:
            print(f'{token_type:12} -> {token_value}')


lexer_analysis("prime_program.txt")
