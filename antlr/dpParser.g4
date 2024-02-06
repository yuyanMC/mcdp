parser grammar dpParser;
options { tokenVocab=dpLexer; }

program
    : stat EOF
    ;

stat: dfunc stat
    | dfunc
    ;

dfunc : FUNC ID LBRAC (TYPE ID (COMMA TYPE ID)*)? RBRAC LCURLY command_with_raw* RCURLY ;

command_with_raw
    : RAW
    | command SEMI
    ;

command
    : define_var
    | call
    ;

define_var
    : VAR PLAYER TYPE ID
    | PLAYER VAR TYPE ID
    | VAR TYPE ID
    ;

call
    : (ID DOT)* ID LBRAC (paramter (COMMA paramter)*)? RBRAC
    ;

paramter
    : ID
    | string
    ;

string
    : DOUBLESTRING
    | SINGLESTRING
    ;