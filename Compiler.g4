grammar Compiler;

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