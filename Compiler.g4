grammar Compiler;

// Parser Rules
prog: PROGRAM ID PVIG decls cmdcomp PONTO;
decls: VAR listdecl | ;
listdecl: decltip | decltip listdecl;
decltip: listid DPONTOS tip PVIG;
listid: ID | ID VIG listid;
tip: ID | BOOLEAN | STRING;
cmdcomp: BEGIN listcmd END;
listcmd: cmd | cmd PVIG listcmd;
cmd: cmdif | cmdwhile | cmdread | cmdwrite | cmdatrib | cmdcomp;
cmdif: IF expr THEN cmd elsepart;
elsepart: ELSE cmd | ;
cmdwhile: WHILE expr DO cmd;
cmdread: READ ( listid );
cmdwrite: WRITE ( listw );
listw: elemw | elemw VIG listw;
elemw: expr | CADEIA;
cmdatrib: ID ATRIB expr;
expr: term expr1;
expr1: OPREL term expr1 | ;
term: factor term1;
term1: OPAD factor term1 | ;
factor: primary factor1;
factor1: OPMULT primary factor1 | ;
primary: ID | CTE | ABPAR expr FPAR | TRUE | FALSE | OPNEG primary;

// Palavras reservadas
PROGRAM : 'PROGRAM';
INTEGER : 'INTEGER';
BOOLEAN : 'BOOLEAN';
BEGIN   : 'BEGIN';
END     : 'END';
WHILE   : 'WHILE';
DO      : 'DO';
READ    : 'READ';
VAR     : 'VAR';
FALSE   : 'FALSE';
TRUE    : 'TRUE';
WRITE   : 'WRITE';
STRING  : 'STRING';
IF      : 'IF';
THEN    : 'THEN';
ELSE    : 'ELSE';

// Operadores
OPAD : '+' | '-';
OPMULT : '*' | '/';
OPDIV : '\\';
OPREL : '>' | '<' | '>=' | '<=' | '==' | '<>';
OPLOG : 'OR' | 'AND';
OPNEG : '~';

// Símbolos
PVIG : ';';
PONTO : '.';
DPONTOS : ':';
VIG : ',';
ABPAR : '(';
FPAR : ')';
ATRIB : ':=';

ID      : ([a-zA-Z][_]*[a-zA-Z0-9_]*);
CTE     : [+-]?[0-9]+;
CADEIA  : '"' (~'"')* '"';

// Comentários
COMMENT : '//' ~[\r\n]* -> skip;

// Espaços em branco
WS : [ \t\r\n]+ -> skip;