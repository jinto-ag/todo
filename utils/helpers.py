import operator
import keyword
import re


def get_operators():

    symbols = {
        "add": "+",
        "sub": "-",
        "mul": "*",
        "truediv": "/",
        "floordiv": "//",
        "mod": "%",
        "pow": "**",
        "and_": "and",
        "or_": "or",
        "xor": "xor",
        "lshift": "<<",
        "rshift": ">>",
        "not_": "not",
        "neg": "-",
        "pos": "+",
        "abs": "abs",
        "invert": "~",
        "lt": "<",
        "le": "<=",
        "eq": "==",
        "ne": "!=",
        "ge": ">=",
        "gt": ">",
    }

    operators = dir(operator)
    operator_symbols = [symbols[op] for op in operators if op in symbols]

    # Add additional operator symbols not in the operator module
    operator_symbols += [
        "in",
        "is",
        "[",
        "]",
        "(",
        ")",
        "{",
        "}",
        "@",
        ":",
        ",",
        ".",
        ";",
        "=",
    ]

    return operator_symbols


def is_keyword(name):
    return name in keyword.kwlist


def is_identifier(name):
    pattern_str = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    pattern = re.compile(pattern_str)
    return bool(pattern.match(name))


def is_operator(symbol):
    return symbol in get_operators()
