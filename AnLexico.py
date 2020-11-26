import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = ['ID','NUMBER','FLOATNUMBER','PLUS','MINUS','DIVIDE','TIMES',
        'PUNTOYCOMA','COMA','ASSIGN','MAYORQUE','MENORQUE',
        'DIFF','ESIGUAL','MAYORIGUAL','MENORIGUAL','AND','NOT','OR',
        'LPAR','RPAR','RELATIONAL','LBRACKET','RBRACKET']

reservadas = ['START','FINISH','DECLARATION','ENDECLARATION','MODULE',
            'BEGIN','END','IF','IFELSE','FOR','DO','WHILE','DWHILE','ELSE',
            'INT','VECTOR','MATRIX','CUBE','FLOAT',
            'STRING','INPUT','OUTPUT','IN','MAIN','CALL']

tokens = tokens+reservadas

t_ignore = ' \t\r\f\v'

t_RELATIONAL = r'>=|<=|>|<|==|!='
t_COMA = r'\,'
t_PLUS = r'\+'
# t_DIFF = r"!\="
# t_ESIGUAL = r"\=\="
# t_MAYORIGUAL = r"\>\="
# t_MENORIGUAL = r'<\='
t_ASSIGN = '='
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PUNTOYCOMA = r';'
# t_MAYORQUE = r'\>'
# t_MENORQUE = '<'
t_AND = r'\&'
t_OR = r'\|'
t_NOT = r'\!'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

def t_ccode_nonspace(t):
    r'\s+'
    pass

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*' #puede comenzar con cualquier digito
    if t.value.upper() in reservadas:
        t_value = t.value.upper()
        t.type = t.value
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno = 10#+= len(t.value)

#Commentario empieza con gato seguido de cualquier letra
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
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.sikip(1)

lexer = lex.lex()
