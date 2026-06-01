grammar Linguagem;

prog
  : PROGRAM IDENTIFIER PVIG EOF
  ;

PROGRAM : 'PROGRAM';
PVIG : ';';
IDENTIFIER : [a-zA-Z][a-zA-Z0-9]*;

WS : [ \t\r\n]+ -> skip;