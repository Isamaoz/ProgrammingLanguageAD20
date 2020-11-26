import ply.lex as lex

tokens = ['ID', 'NUMBER', 'FLOATNUMBER', 'COMMA', 'SEMMICOLON', 'LPARENT', 'RPARENT', 'ASSIGN', 'PLUS', 'MINUS',
		'TIMES', 'DIVIDE', 'NE', 'LT', 'LTE', 'POINT', 'GT', 'GTE', 'RBRACKET', 'LBRACKET', 'EQUAL', 'STRING',
		'OR', 'AND', 'NOT', 'GTGT']

reserved = {'program': 'PROGRAM',
			'dim': 'DIM',
			'as': 'AS',
			'end': 'END',
			'subprocedure': 'SUBPROCEDURE',
			'endsub': 'ENDSUB',
			'let': 'LET',
			'print': 'PRINT',
			'input': 'INPUT',
			'cls': 'CLS',
			'if': 'IF',
			'then': 'THEN',
			'else': 'ELSE',
			'endif': 'ENDIF',
			'while': 'WHILE',
			'whend': 'WHEND',
			'do': 'DO',
			'loopuntil': 'LOOPUNTIL',
			'endo': 'ENDO',
			'for': 'FOR',
			'to': 'TO',
			'next': 'NEXT',
			'gosub': 'GOSUB',
			'word': 'WORD',
			'float': 'FLOAT',
			'array': 'ARRAY',
			'matrix': 'MATRIX',
			'cube': 'CUBE'}

tokens = tokens+list(reserved.values())

t_ignore = '\t\r\v\f '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_NE = '<>'
t_LT = '<'
t_LTE = '<='
t_GT = '>'
t_GTE = '>='
t_LPARENT = '\('
t_RPARENT = '\)'
t_COMMA = ','
t_POINT = '\.'
t_SEMMICOLON = ';'
t_LBRACKET = '\['
t_RBRACKET = '\]'
t_OR = '\|\|'
t_AND = '&&'
t_NOT = '!'
t_GTGT = '>>'
t_EQUAL = '=='


def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value, 'ID')
	return t


def t_STRING(t):
	r'["][\\a-zA-Z 0-9:!@#$%^&*()\-+=/?¿<>,~`|ñ/\.]+["]'
	return t


def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)


def t_COMMENT(t):
	r'\#.*'
	pass


def t_FLOATNUMBER(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t


def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t


def t_error(t):
	print("Illegal character ", t.value[0])
	t.lexer.skip(1)


lexer = lex.lex()
