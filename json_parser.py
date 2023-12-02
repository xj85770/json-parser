import sys
import re

def lex(json_input):
    # Lexer to tokenize various elements including brackets
    tokens = re.findall(r'[{}\[\]:,]|\btrue\b|\bfalse\b|\bnull\b|"[^"]*"|\d+', json_input)
    return tokens

def parse_object(tokens):
    if not tokens or tokens.pop(0) != '{':
        return False, tokens
    if tokens[0] == '}':
        tokens.pop(0)
        return True, tokens

    while True:
        key, tokens = parse_value(tokens)
        if not isinstance(key, str) or not tokens or tokens.pop(0) != ':':
            return False, tokens
        result, tokens = parse_value(tokens)
        if not result:
            return False, tokens

        if not tokens or (tokens[0] != ',' and tokens[0] != '}'):
            return False, tokens
        if tokens[0] == '}':
            tokens.pop(0)
            return True, tokens
        tokens.pop(0)  # Remove comma

def parse_array(tokens):
    if not tokens or tokens.pop(0) != '[':
        return False, tokens
    if tokens[0] == ']':
        tokens.pop(0)
        return True, tokens

    while True:
        result, tokens = parse_value(tokens)
        if not result:
            return False, tokens

        if not tokens or (tokens[0] != ',' and tokens[0] != ']'):
            return False, tokens
        if tokens[0] == ']':
            tokens.pop(0)
            return True, tokens
        tokens.pop(0)  # Remove comma

def parse_value(tokens):
    if not tokens:
        return False, tokens

    token = tokens.pop(0)
    if token == '{':
        return parse_object(['{'] + tokens)
    elif token == '[':
        return parse_array(['['] + tokens)
    elif token in ['true', 'false', 'null'] or token.isdigit() or (token.startswith('"') and token.endswith('"')):
        return True, tokens
    return False, tokens

def parse(tokens):
    result, remaining_tokens = parse_object(tokens)
    return result and not remaining_tokens

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            json_input = file.read()
            tokens = lex(json_input)
            is_valid = parse(tokens)

            if is_valid:
                print(f"Valid JSON: {file_path}")
                return 0
            else:
                print(f"Invalid JSON: {file_path}")
                return 1

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python json_parser.py <file_path>")
        sys.exit(1)

    exit_code = main(sys.argv[1])
    sys.exit(exit_code)
