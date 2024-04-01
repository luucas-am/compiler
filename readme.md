# Python + Antlr Compiler

Compiler created using python and antlr.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install antlr.

```bash
pip install antlr4-python3-runtime
```

## Usage
Create an ANTLR grammar file (e.g., MyGrammar.g4)
```g4
grammar MyGrammar;

// Lexer Rules
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;
INT        : [0-9]+;
PLUS       : '+';
MINUS      : '-';
TIMES      : '*';
DIVIDE     : '/';
LPAREN     : '(';
RPAREN     : ')';

// Ignore whitespace 
WS         : [ \t\r\n]+ -> skip; 
```

Then run the command
```bash
antlr4 MyGrammar.g4
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)