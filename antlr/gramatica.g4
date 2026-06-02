grammar gramatica;

prog
    : PROGRAM IDENTIFIER PVIG decls cmdComp PONTO EOF
    ;

decls
    : VAR listDecl
    |
    ;

listDecl
    : declTip+
    ;

declTip
    : listId DPONTOS tip PVIG
    ;

listId
    : IDENTIFIER (VIG IDENTIFIER)*
    ;

tip
    : INTEGER
    | BOOLEAN
    ;

cmdComp
    : BEGIN listCmd END
    ;

listCmd
    : cmd*
    ;

cmd
    : cmdIf
    | cmdWhile
    | cmdRead
    | cmdWrite
    | cmdAtrib
    | cmdComp
    ;

cmdIf
    : IF expr THEN cmd (ELSE cmd)?
    ;

cmdWhile
    : WHILE expr DO cmd
    ;

cmdRead
    : READ ABPAR listId FPAR PVIG
    ;

cmdWrite
    : WRITE ABPAR (expr | CADEIA) FPAR PVIG
    ;

cmdAtrib
    : IDENTIFIER ATRIB expr PVIG
    ;

expr
    : exprRel (OPLOG exprRel)*
    ;

exprRel
    : exprArit (OPREL exprArit)?
    ;

exprArit
    : termo (OPAD termo)*
    ;

termo
    : fator (OPMULT fator)*
    ;

fator
    : IDENTIFIER
    | CTE
    | TRUE
    | FALSE
    | OPNEG fator
    | ABPAR expr FPAR
    ;

PROGRAM : [Pp][Rr][Oo][Gg][Rr][Aa][Mm];
INTEGER : [Ii][Nn][Tt][Ee][Gg][Ee][Rr];
BOOLEAN : [Bb][Oo][Oo][Ll][Ee][Aa][Nn];
BEGIN   : [Bb][Ee][Gg][Ii][Nn];
END     : [Ee][Nn][Dd];
WHILE   : [Ww][Hh][Ii][Ll][Ee];
DO      : [Dd][Oo];
READ    : [Rr][Ee][Aa][Dd];
VAR     : [Vv][Aa][Rr];
FALSE   : [Ff][Aa][Ll][Ss][Ee];
TRUE    : [Tt][Rr][Uu][Ee];
WRITE   : [Ww][Rr][Ii][Tt][Ee];
IF      : [Ii][Ff];
THEN    : [Tt][Hh][Ee][Nn];
ELSE    : [Ee][Ll][Ss][Ee];

OPREL
    : '<='
    | '>='
    | '=='
    | '<>'
    | '<'
    | '>'
    ;

OPAD
    : '+'
    | '-'
    ;

OPMULT
    : '*'
    | '/'
    ;

OPLOG
    : [Oo][Rr]
    | [Aa][Nn][Dd]
    ;

OPNEG : '~';

PVIG    : ';';
PONTO   : '.';
DPONTOS : ':';
VIG     : ',';
ABPAR   : '(';
FPAR    : ')';
ATRIB   : ':=';

CTE
    : [+-]? [0-9]+
    ;

CADEIA
    : '"' ~["\r\n]* '"'
    ;

IDENTIFIER
    : [a-zA-Z] [a-zA-Z0-9]*
    ;

COMENTARIO
    : '/' .*? '/' -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;