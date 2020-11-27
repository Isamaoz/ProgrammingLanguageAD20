import ply.yacc as yacc
import os
import codecs
import re
from AnLexico import tokens
from sys import stdin
from codigoIntermedio import *
from inspect import currentframe, getframeinfo
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
         | dimtype PUNTOYCOMA
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
    values_table.append([p[2],p[3],p[2]*p[3],p[3],len(dim_values)])
    for i in range(p[2]*p[3]):
        dim_values.append(0)
def p_ddec2(p):
    '''
    DCLCUBE : ID NUMBER NUMBER NUMBER
    '''
    ID_table.append(p[1])
    values_table.append([p[2],p[3],p[4],p[2]*p[3]*p[4],p[3]*p[4],p[4],len(dim_values)])
    for i in range(p[2]*p[3]*p[4]):
        dim_values.append(0)
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
def p_id(p):
    '''
    pid : ID
    '''
    operandosList.append(obtainIndex(p[1]))
def p_id1(p):
    '''
    pid : vec1
        | mat1
        | cub1
    '''
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
     # print("aqui un float")
     # print(operandosList[len(operandosList)-1])
#Funciones que generan los cuadruplos
def p_OPDim(p):
     '''
     OP : vec1
        | mat1
        | cub1
     '''
     #genera cuadruplo vector
def p_OPVector1(p):
     '''
     vec1 : vec
     '''
     #Genera cuadruplo verify
     operadorList.append('verify')
     opA_list.append(operandosList[len(operandosList)-1]) #Agrega index a verificar
     idxid = obtainIndex(operandosList[len(operandosList)-2]) - 1 #Obtiene el index para buscar en la tabla de simbolos
     opB_list.append(0) # Entre 0 y -
     tempList.append(values_table[idxid][0]-1) #Agrega el valor en la lista de valores
     dimensionadas_VECTOR()
def p_OPVector2(p):
     '''
     vec : ID LBRACKET NUMBER RBRACKET
        | ID LBRACKET ID RBRACKET
     '''
     #print_table()
     if (type_table[obtainIndex(p[1])-1] == 'VECTOR'):
         operandosList.append(p[1])
     else:
         raise Exception('This variable is not a vector')
     operandosList.append(p[3]*(-1)) if isinstance(p[3], int) else operandosList.append(obtainIndex(p[3]))
# def p_OPMatrix(p):
#      '''
#      OP : mat1
#      '''
def p_OPMatrix2(p):
     '''
     mat1 : mat
     '''
     operadorList.append('verify')
     operadorList.append('verify')
     opA_list.append(operandosList[len(operandosList)-1]) # Se agregan los dos numeros a revisar a la lista de operadores
     opA_list.append(operandosList[len(operandosList)-2])
     idxid = obtainIndex(operandosList[len(operandosList)-3]) - 1
     opB_list.append(0)
     opB_list.append(0)
     tempList.append(values_table[idxid][0]-1)
     tempList.append(values_table[idxid][1]-1)
     dimensionadas_MATRIX()
def p_OPMatrix1(p):
     '''
     mat : ID LBRACKET NUMBER RBRACKET LBRACKET NUMBER RBRACKET
         | ID LBRACKET NUMBER RBRACKET LBRACKET ID RBRACKET
         | ID LBRACKET ID RBRACKET LBRACKET ID RBRACKET
         | ID LBRACKET ID RBRACKET LBRACKET NUMBER RBRACKET
     '''
     if (type_table[obtainIndex(p[1])-1] == 'MATRIX'):
        operandosList.append(p[1])
     else:
         raise Exception('This variable is not a matrix')
     operandosList.append(p[6]*(-1)) if isinstance(p[6], int) else operandosList.append(obtainIndex(p[6]))
     operandosList.append(p[3]*(-1)) if isinstance(p[3], int) else operandosList.append(obtainIndex(p[3]))
# def p_OPCube(p):
#      '''
#      OP : cub1
#      '''
def p_OPCube2(p):
     '''
     cub1 : cub
     '''
     operadorList.append('verify')
     operadorList.append('verify')
     operadorList.append('verify')
     opA_list.append(operandosList[len(operandosList)-1]) # Se agregan los dos numeros a revisar a la lista de operadores
     opA_list.append(operandosList[len(operandosList)-2])
     opA_list.append(operandosList[len(operandosList)-3])
     idxid = obtainIndex(operandosList[len(operandosList)-4]) - 1
     opB_list.append(0)
     opB_list.append(0)
     opB_list.append(0)
     tempList.append(values_table[idxid][0]-1)
     tempList.append(values_table[idxid][1]-1)
     tempList.append(values_table[idxid][2]-1)
     #print_cuadruplo()
     #print('Salen', operandosList)
     dimensionadas_CUBE()
def p_OPCube1(p):
     '''
     cub : ID LBRACKET NUMBER RBRACKET LBRACKET NUMBER RBRACKET LBRACKET NUMBER RBRACKET
         | ID LBRACKET NUMBER RBRACKET LBRACKET NUMBER RBRACKET LBRACKET ID RBRACKET
         | ID LBRACKET NUMBER RBRACKET LBRACKET  ID RBRACKET LBRACKET NUMBER RBRACKET
         | ID LBRACKET NUMBER RBRACKET LBRACKET ID RBRACKET LBRACKET ID RBRACKET
         | ID LBRACKET ID RBRACKET LBRACKET NUMBER RBRACKET LBRACKET NUMBER RBRACKET
         | ID LBRACKET ID RBRACKET LBRACKET NUMBER RBRACKET LBRACKET ID RBRACKET
         | ID LBRACKET ID RBRACKET LBRACKET ID RBRACKET LBRACKET NUMBER RBRACKET
         | ID LBRACKET ID RBRACKET LBRACKET ID RBRACKET LBRACKET ID RBRACKET
     '''
     if (type_table[obtainIndex(p[1])-1] == 'CUBE'):
        operandosList.append(p[1])
     else:
         raise Exception('This variable is not a CUBE')
     operandosList.append(p[9]*(-1)) if isinstance(p[9], int) else operandosList.append(obtainIndex(p[9]))
     operandosList.append(p[6]*(-1)) if isinstance(p[6], int) else operandosList.append(obtainIndex(p[6]))
     operandosList.append(p[3]*(-1)) if isinstance(p[3], int) else operandosList.append(obtainIndex(p[3]))
     #print('antes de sacar el id222', operandosList)
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
    #print(p)
    frameinfo = getframeinfo(currentframe())

    #print("Nombre del archivo: {} - linea {}",(frameinfo.filename, frameinfo.lineno))
    #print(p.lineno)
    if p == None:
        token = "end of file"
    else:
        #print(p)
        token = f"({p.value}) on line {str(p.lineno)}"

    print(f"Syntax error: Unexpected {token}")

#incluir test

test = os.getcwd()+"\\PF3.txt"
fp = codecs.open(test,"r","utf-8")
cadena = fp.read() #codigo fuente
fp.close()
parser = yacc.yacc('SLR') #
result = parser.parse(cadena)
#print_table()
#print_cuadruplo()
execution()
#print_table()
#NOTAAAA, LOS CUADRUPLOS SE ESTAN PARANDO EN LA ASIGNACION,
#DESPUES NO SE ESTAN GENERANDO LOS SIGUIENTES, CHECAR GRAMATICA
