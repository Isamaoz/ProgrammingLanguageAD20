import ply.yacc as yacc
import codecs
from interpreter import *
from lexical_analyser import tokens

precendence = (
	('right', 'ASSING'),
	('left', 'NE'),
	('left', 'AND', 'OR', 'NOT'),
	('left', 'LT', 'LTE', 'GT', 'GTE'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	('left', 'LPARENT', 'RPARENT')
)

#Gramatica principal

def p_PROGRAM(p):
	'''
	program : PROGRAM1 ID VARIABLE SP SALTO STATUTES END SEMMICOLON
	'''
	finDePrograma()


def p_PROGRAM_PROGRAM1(p):
	'''
	PROGRAM1 : PROGRAM
	'''
	genFirstGoto()


def p_PROGRAM_SALTO(p):
	'''
	SALTO :
	'''
	rellenarFirstGoto()


def p_VARIABLE(p):
	'''
	VARIABLE : DIM IDLIST AS TIPO SEMMICOLON VARIABLE
	|
	'''


def p_SP(p):
	'''
	SP : SUBPROCEDURE ID2 STATUTES ENDSUB SEMMICOLON RETURN SP
	'''


def p_RETURN(p):
	'''
	RETURN :
	'''
	spReturn()


def p_SP_ID2(p):
	'''
	ID2 : ID
	'''
	SP_insert(p[1])


def p_SP_EMPTY(p):
	'''
	SP :
	'''

def p_STATUTES(p):
	'''
	STATUTES : STATEMENTS SEMMICOLON STATUTES
	|
	'''


def p_STATEMENTS_LET(p):
	'''
	STATEMENTS : LET VAR ASSIGN E
	'''
	genCuadruplo(p[3])


def p_STATEMENTS_PRINT(p):
	'''
	STATEMENTS : PRINT VALUE
	'''
	genCuadruploPRINT(p[2])


def p_STATEMENTS_INPUT(p):
	'''
	STATEMENTS : INPUT TEXT GTGT VAR
	'''
	genCuadruploINPUT(p[2])


def p_STATEMENTS_CLS(p):
	'''
	STATEMENTS : CLS
	'''
	genCuadruploCLS()


def p_STATEMENTS_IF(p):
	'''
	STATEMENTS : IF EL THEN1 STATUTES ELSE1 STATUTES ENDIF
	'''
	finIF()


def p_STATEMENTS_WHILE(p):
	'''
	STATEMENTS : WHILE1 EL DO1 STATUTES WHEND
	'''
	finWhile()


def p_STATEMENTS_DO(p):
	'''
	STATEMENTS : DO2 STATUTES LOOPUNTIL EL ENDO
	'''
	finDoWhile()


def p_STATEMENTS_FOR(p):
	'''
	STATEMENTS : FOR ID1 ASSIGN E TO1 E DO3 STATUTES NEXT
	'''
	finFor()


def p_STATEMENTS_GOSUB(p):
	'''
	STATEMENTS : GOSUB POINT ID
	'''
	genCuadruploGOSUB(buscar(p[3]))


def p_E(p):
	'''
	E : E PLUS T
	| E MINUS T
	'''
	genCuadruplo(p[2])


def p_E1(p):
	'''
	E : T
	'''


def p_T(p):
	'''
	T : T TIMES F
	| T DIVIDE F
	'''
	genCuadruplo(p[2])


def p_T1(p):
	'''
	T : F
	'''


def p_F(p):
	'''
	F : NUMBER
	'''
	pushOperandos(int(p[1])*(-1))


def p_F1(p):
	'''
	F : FLOATNUMBER
	'''
	pushOperandos(float(p[1])*(-1))


def p_F2(p):
	'''
	F : VAR
	'''


def p_F3(p):
	'''
	F : LPARENT E RPARENT
	'''


def p_EL(p):
	'''
	EL : EL OR TL
	'''
	genCuadruplo(p[2])


def p_EL1(p):
	'''
	EL : TL NOT
	| TL
	'''


def p_TL(p):
	'''
	TL : TL AND FL
	'''
	genCuadruplo(p[2])


def p_TL1(p):
	'''
	TL : FL
	'''


def p_FL(p):
	'''
	FL : OPERATOR OPREL OPERATOR
	'''
	genCuadruplo(p[2])


def p_FL1(p):
	'''
	FL : LPARENT EL RPARENT
	'''


def p_OPREL(p):
	'''
	OPREL : LT
	| LTE
	| GT
	| GTE
	| NE
	| EQUAL
	'''
	p[0] = p[1]


def p_OPERATOR(p):
	'''
	OPERATOR : VAR
	'''


def p_OPERATOR1(p):
	'''
	OPERATOR : NUMBER
	'''
	pushOperandos(int(p[1])*(-1))


def p_OPERATOR2(p):
	'''
	OPERATOR : FLOATNUMBER
	'''
	pushOperandos(float(p[1])*(-1))


def p_IDLIST(p):
	'''
	IDLIST : ID
	'''
	insertID(p[1])


def p_IDLIST2(p):
	'''
	IDLIST : IDLIST COMMA ID
	'''
	insertID(p[3])


def p_TIPO_SIMPLES(p):
	'''
	TIPO : WORD
	| FLOAT
	'''
	insertType(p[1])


def p_TIPO_DIM_ARRAY(p):
	'''
	TIPO : ARRAY DCLARRAY
	'''
	dimCarac(p[1],insertType(p[1]))


def p_TIPO_DIM_MATRIX(p):
	'''
	TIPO : MATRIX DCLMATRIX
	'''
	dimCarac(p[1],insertType(p[1]))


def p_TIPO_DIM_CUBE(p):
	'''
	TIPO : CUBE DCLCUBE
	'''
	dimCarac(p[1],insertType(p[1]))


def p_DCLARRAY(p):
	'''
	DCLARRAY : LBRACKET IDENTIFICATOR RBRACKET
	'''


def p_DCLMATRIX(p):
	'''
	DCLMATRIX : LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET
	'''


def p_DCLCUBE(p):
	'''
	DCLCUBE : LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET LBRACKET IDENTIFICATOR RBRACKET
	'''


def p_IDENTIFICATOR(p):
	'''
	IDENTIFICATOR : NUMBER
	'''
	pushOperandos(int(p[1])*(-1))


def p_IDENTIFICATOR_1(p):
	'''
	IDENTIFICATOR : ID
	'''
	pushOperandos(p[1])


def p_DCLARRAY_EJECUCION(p):
	'''
	DCLARRAY1 : LBRACKET IDENTIFICATOR1 RBRACKET
	'''
	dimensionadas_ARRAY()


def p_DCLMATRIX_EJECUCION(p):
	'''
	DCLMATRIX1 : LBRACKET IDENTIFICATOR1 RBRACKET LBRACKET IDENTIFICATOR1 RBRACKET
	'''
	dimensionadas_MATRIX()


def p_DCLCUBE_EJECUCION(p):
	'''
	DCLCUBE1 : LBRACKET IDENTIFICATOR1 RBRACKET LBRACKET IDENTIFICATOR1 RBRACKET LBRACKET IDENTIFICATOR1 RBRACKET
	'''
	dimensionadas_CUBE()


def p_IDENTIFICATOR_EJECUCION(p):
	'''
	IDENTIFICATOR1 : NUMBER
	'''
	pushOperandos(int(p[1])*(-1))


def p_IDENTIFICATOR_1_EJECUCION(p):
	'''
	IDENTIFICATOR1 : ID
	'''
	pushOperandos(buscar(p[1]))


def p_STATEMENTS_VAR(p):
	'''
	VAR : ID
	'''
	pushOperandos(buscar(p[1]))


def p_STATEMENTS_VAR1(p):
	'''
	VAR : ID PUSH DCLARRAY1
	| ID  PUSH DCLMATRIX1
	| ID PUSH DCLCUBE1
	'''


def p_PUSH(p):
	'''
	PUSH :
	'''
	pushOperandos(buscar(p[-1]))


def p_STATEMENTS_IF_ELSE1(p):
	'''
	ELSE1 : ELSE
	'''
	goto()


def p_STATEMENTS_IF_ELSE1_EMPTY(p):
	'''
	ELSE1 :
	'''


def p_STATEMENTS_IF_THEN1(p):
	'''
	THEN1 : THEN
	'''
	gotofalso()


def p_STATEMENTS_WHILE_WHILE1(p):
	'''
	WHILE1 : WHILE
	'''
	origen()


def p_STATEMENTS_WHILE_DO1(p):
	'''
	DO1 : DO
	'''
	gotofalso()


def p_STATEMENTS_DO_DO2(p):
	'''
	DO2 : DO
	'''
	origen()


def p_STATEMENTS_FOR_ID(p):
	'''
	ID1 : ID
	'''
	pushOperandos(buscar(p[1]))


def p_STATEMENTS_FOR_TO(p):
	'''
	TO1 : TO
	'''
	genCuadruploFor("=")


def p_STATEMENTS_FOR_DO(p):
	'''
	DO3 : DO
	'''
	forAction3()


def p_VALUE(p):
	'''
	VALUE : LPARENT VAR RPARENT
	'''
	p[0] = " "


def p_VALUE1(p):
	'''
	VALUE : TEXT
	'''
	p[0] = p[1]


def p_TEXT(p):
	'''
	TEXT : LPARENT STRING RPARENT
	'''
	p[0] = p[2]


def p_TEXT1(p):
	'''
	TEXT :
	'''


def p_error(p):
	print("Incorrect grammar\n", p)
	print("Error in the line "+str(p.lineno))


test = os.getcwd()+"\\ProgramasPrueba\\prueba4.txt"
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()
parser = yacc.yacc('SLR')
result = parser.parse(cadena)
# imprimirCuadruplos()
ejecution()
# imprimirSymbolTable()
