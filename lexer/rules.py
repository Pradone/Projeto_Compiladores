RESERVADAS = {
    "PROGRAM",
    "INTEGER",
    "BOOLEAN",
    "BEGIN",
    "END",
    "WHILE",
    "DO",
    "READ",
    "VAR",
    "FALSE",
    "TRUE",
    "WRITE",
    "IF",
    "THEN",
    "ELSE",
}

OPERADORES_SIMPLES = {
    "+": ("OPAD", "MAIS"),
    "-": ("OPAD", "MENOS"),
    "*": ("OPMULT", "VEZES"),
    "/": ("OPMULT", "DIV"),
    "<": ("OPREL", "MENOR"),
    ">": ("OPREL", "MAIOR"),
    "~": ("OPNEG", "NEG"),
}

SIMBOLOS = {
    ";": "PVIG",
    ".": "PONTO",
    ":": "DPONTOS",
    ",": "VIG",
    "(": "ABPAR",
    ")": "FPAR",
}

OPERADORES_COMPOSTOS = {
    "<=": ("OPREL", "MENIG"),
    ">=": ("OPREL", "MAIG"),
    "==": ("OPREL", "IGUAL"),
    "<>": ("OPREL", "DIFER"),
    ":=": ("ATRIB", None),
}
