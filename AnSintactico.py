import ply.yacc as yacc
import os
import codecs
import re
from AnLexico import tokens
from sys import stdin
from codigoIntermedio import *
#dim de variables dimensionadas
#base


#No terminales start,
def p_program(p):
    '''
    program : st var_dec procedure main_block FINISH
    '''
    endProgram()
def p_program1(p):
    '''
    st : START
    '''
    PC = 0
    startProgram()
def p_variable_dec(p):
    '''
    var_dec : DECLARATION decl ENDECLARATION
            |
    '''

def p_decl(p):
    '''
    decl : type variable PUNTOYCOMA
         |  decl type variable PUNTOYCOMA
         |  decl dimtype PUNTOYCOMA

    '''
# def p_decl1(p):
#     '''
#     vec : VECTOR ID NUMBER
#     '''
#     type_table.append(p[1])
#     ID_table.append(p[2])
#     values_table.append([p[3],len(dim_values)])
#
#
# def p_decl2(p):
#     '''
#     mat : MATRIX variable NUMBER NUMBER
#     '''
#     set_type(p[1])
# def p_decl3(p):
#     '''
#     cub : MATRIX variable NUMBER
#     '''
#     set_type(p[1])
def p_variable(p):
    '''
    variable : ID
             | variable COMA ID
    '''
    # if (len(p)>2):
    #     ("hOLA:",p[3])
    # else:
    set_ID(p[3]) if len(p)>2 else set_ID(p[1])

def p_type(p):
    '''
    type : INT
         | FLOAT
    '''
    #print("hOLA:",p[1])
    set_type(p[1])
def p_type2(p):
    '''
    dimtype : VECTOR DCLVECTOR
    '''
    type_table.append(p[1])
def p_type3(p):
    '''
    dimtype : MATRIX DCLMATRIX
    '''
    type_table.append(p[1])
def p_type4(p):
    '''
    dimtype : CUBE DCLCUBE
    '''
    type_table.append(p[1])
def p_ddec(p):
    '''
    DCLVECTOR : ID NUMBER
    '''
    ID_table.append(p[1])
    values_table.append([p[2],len(dim_values)])
    for i in range(p[2]):
        dim_values.append(0)
def p_ddec1(p):
    '''
    DCLMATRIX : ID NUMBER NUMBER
    '''
    ID_table.append(p[1])
    values_table.append([p[2],p[3],len(dim_values)])
    for i in range(p[2]*p[3]):
        dim_values.append(0)
def p_ddec2(p):
    '''
    DCLCUBE : ID NUMBER NUMBER NUMBER
    '''
    # set_type(p[1])
    # dim_values.append([int(0)]*(p[3]*p[2]*p[4]))
def p_procedure(p):
    '''
    procedure : MODULE iddd beggg stat enddd procedure
                |
    '''
    #5endProcedure()
def p_procedureid(p):
    '''
    iddd : ID
    '''
    type_table.append('procedure')
    ID_table.append(p[1])
def p_procedure1(p):
    '''
    beggg : BEGIN
            |
    '''
    module = len(tempList)
    values_table.append(module)
    #agregar inicio del procedure
    #saltos.append(len(tempList))
def p_procedure2(p):
    '''
    enddd : END
            |
    '''
    #llamar al fin del procedure
    operadorList.append('endProcedure')
    opA_list.append('-')
    opB_list.append('-')
    tempList.append('-')
def p_estatutos(p):
    '''
    stat : estatuto stat
          |
    '''
def p_mainblock(p):
    '''
    main_block : MAIN be stat END
    '''
def p_mainblock1(p):
    '''
     be : BEGIN
    '''
    opB_list[0] = len(tempList)
def p_CALL(p):
     '''
     estatuto : CALL ID PUNTOYCOMA
     '''
     #generaCuadruplo del ID
     operadorList.append('call')

     opA_list.append('-')
     #print('pbIdx:',obtainIndex(p[2]))
     opB_list.append(values_table[obtainIndex(p[2])-1])
     tempList.append('-')
def p_Sif(p):
     '''
     estatuto : IF expresion beg stat els stat END
                | IF expresion beg stat END
     '''
     endIf()
def p_Sif1(p):
     '''
     beg : BEGIN
     '''
     gotoFalse(1)
def p_Sif2(p):
     '''
     els : ELSE
     '''
     goto(1)
def p_Saritmetico(p):
     '''
     estatuto : pid ASSIGN E PUNTOYCOMA
     '''
     generaCuadruplo(p[2])
     print(p[2])
def p_id(p):
    '''
    pid : ID
    '''
    operandosList.append(obtainIndex(p[1]))
# def p_id1(p):
#     '''
#     pid : vec
#         | mat
#         | cub
#     '''
def p_E1(p):
     '''
     E : E PLUS T
        | E MINUS T
     '''
     generaCuadruplo(p[2])

def p_E2(p):
     '''
     E : T
     '''
def p_T1(p):
     '''
     T : T TIMES F
        | T DIVIDE F
     '''
     generaCuadruplo(p[2])
def p_T2(p):
     '''
     T : F
     '''
def p_F1(p):
     '''
     F : OP
     '''
def p_F3(p):
     '''
     F : LPAR E RPAR
     '''
     #print(p[3])
def p_expresion(p):
     '''
     expresion : LPAR EL RPAR
     '''
def p_EL1(p):
     '''
     EL : EL OR TL
     '''
     generaCuadruplo(p[2])
def p_EL2(p):
     '''
     EL : TL NOT
     '''
     generaCuadruplo(p[2])
def p_EL3(p):
     '''
     EL : TL
     '''
def p_TL1(p):
     '''
     TL : TL AND FL
     '''
     generaCuadruplo(p[2])
def p_TL2(p):
     '''
     TL : FL
     '''
def p_FL1(p):
     '''
     FL : OP opLogico OP
     '''
     generaCuadruplo(p[2])
def p_FL2(p):
     '''
     FL : LPAR EL LPAR
     '''
def p_opLogico(p):
     '''
     opLogico : RELATIONAL

     '''
     p[0] = p[1]
def p_OP2(p):
     '''
     OP : NUMBER
     '''
     operandosList.append(int(p[1])*(-1))
def p_OP3(p):
     '''
     OP : FLOATNUMBER
     '''
     operandosList.append(float(p[1])*(-1))
     print("aqui un float")
     print(operandosList[len(operandosList)-1])
#Funciones que generan los cuadruplos
def p_OPVector(p):
     '''
     OP : vec
     '''
     print('sos',p[1])
     # if p[3].isdigit():
     #     #es un numero, hacer gramatica multiplicando por 1
     #     operadorList.append(obtainIndexDim()+300)
     #     #meter id index
     # else:
     #     print('nada por aqui')
         #es un id, hay que encontrar el index
        #numero que reconoci dentro del corchete
    #generaCruadruploVec()
    #verify
    #suma entre el numero que recupere del .txt +
     #operandosList.append(float(p[1])*(-1))
def p_OPVector1(p):
     '''
     vec : ID LBRACKET NUMBER RBRACKET
        | ID LBRACKET ID RBRACKET
     '''
     print('sos',p[1])
def p_OPMatrix(p):
     '''
     OP : mat
     '''
     #operandosList.append(float(p[1])*(-1))
def p_OPMatrix(p):
     '''
     mat : ID LBRACKET OP RBRACKET LBRACKET OP RBRACKET
     '''
     #operandosList.append(float(p[1])*(-1))
def p_OPCube(p):
     '''
     OP : cub
     '''
     #operandosList.append(float(p[1])*(-1))
def p_OPCube1(p):
     '''
     cub : ID LBRACKET OP RBRACKET LBRACKET OP RBRACKET LBRACKET OP RBRACKET
     '''
def p_OP1(p):
     '''
     OP : ID
     '''
     operandosList.append(obtainIndex(p[1]))
def p_Sfor(p):
    '''
    estatuto : FOR expresion_for beg1 stat END
    '''
    endFor()
def p_Sfor1(p):
     '''
     beg1 : BEGIN
     '''
     gotoFalse(2)
def p_expresion_for(p):
     '''
     expresion_for : LPAR id1 IN numb RPAR
                    | LPAR id1 IN idx RPAR
     '''
     generaCuadruploFOR('<')
def p_expresion_for1(p):
     '''
     numb : NUMBER
     '''
     operandosList.append(int(p[1])*(-1))
def p_expresion_for4(p):
     '''
     numb : FLOATNUMBER
     '''
     operandosList.append(float(p[1])*(-1))
def p_expresion_for2(p):
     '''
     idx : ID
     '''
     #meter ID en la lista de operandos
     #operador < index del id numero temp
     operandosList.append(obtainIndex(p[1]))
def p_expresion_for3(p):
     '''
     id1 : ID
     '''
     #meter ID en la lista de operandos
     #operador < index del id numero temp
     operandosList.append(obtainIndex(p[1]))
def p_Swhile(p):
    '''
    estatuto : WHILE expresion BB stat END
    '''
    goto(3)
def p_Swhile1(p):
    '''
    BB : BEGIN
    '''
    gotoFalse(3)
#IMPORTANTE
#En la siguiente parte del codigo, la primera iteracion del dowhile
# siempre debe ser verdadera, se empieza a checar desde la segunda
def p_Sdowhile(p):
    '''
    estatuto : doo stat wh expresion
    '''
    gotoFalseDW()
def p_Sdowhile1(p):
    '''
    doo : DO
    '''
    #guardar do en la lista de saltos
    saltos.append(len(tempList))
def p_Sdowhile2(p):
    '''
    wh : DWHILE
    '''
def p_Soutput(p):
    '''
    estatuto : OUTPUT OP PUNTOYCOMA
    '''
    operadorList.append('output')
    opA_list.append(operandosList.pop())
    opB_list.append('-')
    tempList.append('-')
def p_Sinput(p):
    '''
    estatuto : INPUT ID PUNTOYCOMA
    '''
    generaCuadruploInput(obtainIndex(p[2]))
def p_error(p):
    print(p.lineno)
    if p == None:
        token = "end of file"
    else:
        #print(p)
        token = f"({p.value}) on line {str(p.lineno)}"

    print(f"Syntax error: Unexpected {token}")

#incluir test

test = os.getcwd()+"\\P2.txt"
fp = codecs.open(test,"r","utf-8")
cadena = fp.read() #codigo fuente
fp.close()
parser = yacc.yacc('SLR') #
result = parser.parse(cadena)
print_table()
#print(dim_values)
print_cuadruplo()
#print(operandosList)
#print(temp)
execution()
print_table()
#print(temp_exe)
#No estoy segura si tengo que actualizar estas variables en la tabla