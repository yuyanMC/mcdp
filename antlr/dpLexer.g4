// DELETE THIS CONTENT IF YOU PUT COMBINED GRAMMAR IN Parser TAB
lexer grammar dpLexer;
RAW: '%rawstart%'('a'|~[a])*'%rawend%';

AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;
EQ : '=' ;
COMMA : ',' ;
SEMI : ';' ;
LBRAC : '(' ;
RBRAC : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;
DOT : '.' ;
DOUBLESTRING : '"' ('\\"'|~["])* '"' ;
SINGLESTRING : '\'' ('\\\''|~['])* '\'' ;
FUNC : 'func' ;
TYPE : 'byte' | 'int' | 'long' | 'float' | 'double' | 'string' | 'Entity' | 'Player' ;
VAR : 'local' | 'global' ;
PLAYER : 'player' ;

INT : [0-9]+ ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;