global tempID
global tempList
global operadorList
global opA_list
global opB_list
global temp
global operandosList
global saltos
from tablaSimbolos import *
global tempFOR
global PC
global temp_exe
global save_PC

operadorList = []
opA_list = []
opB_list = []
tempList = []
operandosList = []
saltos = []
temp_exe = [0] * 41
temp = list(range(100, 141))

def print_cuadruplo():
    for i in range(len(operadorList)):
        print( str(i), '|', operadorList[i], ' | ', opA_list[i], ' | ', opB_list[i], ' | ', tempList[i])

def generaCuadruplo(x):
    operadorList.append(x)
    opB_list.append(operandosList.pop())
    opA_list.append(operandosList.pop())
    #Validaciones
    if (x != '='):
        tempList.append(temp.pop(0))
        operandosList.append(tempList[len(tempList)-1])
    else:
        tempList.append('-')
    if (opA_list[len(opA_list)-1] >= 100 and opA_list[len(opA_list)-1] < 300):
        temp.append(opA_list[len(opA_list)-1])
    if (opB_list[len(opB_list)-1] >= 100 and opB_list[len(opB_list)-1] < 300):
        temp.append(opB_list[len(opB_list)-1])

def generaCuadruploInput(x):
    #Recibe input y genera cuadruplo de asignacion
    operadorList.append('input')
    opA_list.append(x)
    opB_list.append('-')
    tempList.append('-')

def generaCuadruploFOR(x):
    global tempID
    operadorList.append(x)
    #Obtiene numero
    opB_list.append(operandosList.pop())
    #Obtiene ID y guarda
    tempID = operandosList.pop()
    opA_list.append(tempID)
    #Guarda var en un temporal
    tempList.append(temp.pop(0))
    operandosList.append(tempList[len(tempList)-1])
    #print('operandosTermina',operandosList)

#Funcion que obtiene el index de una variable
def obtainIndex(x):
    return ID_table.index(x)+1

def dimensionadas_VECTOR():
    x = operandosList.pop(len(operandosList)-2)
    #print('GENERACION DE CUADRUPLOS:',operandosList) #Queda el index en la lista de cuadruplos
    # operadorList.append('+')
    # opA_list.append(operandosList.pop())
    # opB_list.append(tempList[len(tempList)-1])
    # tempList.append(temp.pop(0))
    # operandosList.append(tempList[len(tempList)-1])
    # temp.append(tempList[len(tempList)-1])

    #Sumar index con la base
    operadorList.append('+')
    opA_list.append(operandosList.pop())
    opB_list.append(values_table[obtainIndex(x)-1][1]*(-1))
    tempList.append(temp.pop(0))
    operandosList.append(tempList[len(tempList)-1]+200)
    temp.append(tempList[len(tempList)-1])
    #print('sale',operandosList)

def dimensionadas_MATRIX():
    x = operandosList.pop(len(operandosList)-3)
    #print('llega:',operandosList)
    operadorList.append('*')
    opA_list.append(operandosList.pop())
    opB_list.append(values_table[obtainIndex(x)-1][3]*(-1))
    tempList.append(temp.pop(0))
    temp.append(tempList[len(tempList)-1])
    #print('1:',operandosList)

    operadorList.append('+')
    opA_list.append(operandosList.pop())
    opB_list.append(tempList[len(tempList)-1])
    tempList.append(temp.pop(0))
    operandosList.append(tempList[len(tempList)-1])
    temp.append(tempList[len(tempList)-1])

    #Sumar con la base
    operadorList.append('+')
    opA_list.append(operandosList.pop())
    opB_list.append(values_table[obtainIndex(x)-1][4]*(-1))
    tempList.append(temp.pop(0))
    operandosList.append(tempList[len(tempList)-1]+200)
    temp.append(tempList[len(tempList)-1])
    #print(operandosList)

def dimensionadas_CUBE():
    x = operandosList.pop(len(operandosList)-4)
    operadorList.append('*')
    opA_list.append(operandosList.pop())
    opB_list.append(values_table[obtainIndex(x)-1][4]*(-1))
    tempList.append(temp.pop(0))
    temp.append(tempList[len(tempList)-1])
    #print('1:',operandosList)
    #b * m2
    operadorList.append('*')
    opA_list.append(operandosList.pop())
    opB_list.append(values_table[obtainIndex(x)-1][5]*(-1))
    tempList.append(temp.pop(0))
    operandosList.append(tempList[len(tempList)-2])
    operandosList.append(tempList[len(tempList)-1])
    temp.append(tempList[len(tempList)-1])
    #Sumar esos dos
    operadorList.append('+')
    opA_list.append(operandosList.pop())
    opB_list.append(operandosList.pop())
    tempList.append(temp.pop(0))
    operandosList.append(tempList[len(tempList)-1])
    temp.append(tempList[len(tempList)-1])

    #Sumar con el ultimo (3 dimensiones completas)
    operadorList.append('+')
    opA_list.append(operandosList.pop())
    opB_list.append(operandosList.pop())
    tempList.append(temp.pop(0))
    operandosList.append(tempList[len(tempList)-1])
    temp.append(tempList[len(tempList)-1])

    #Sumar con la base
    operadorList.append('+')
    opA_list.append(operandosList.pop())
    opB_list.append(values_table[obtainIndex(x)-1][6]*(-1))
    tempList.append(temp.pop(0))
    operandosList.append(tempList[len(tempList)-1]+200)
    temp.append(tempList[len(tempList)-1])
    #print(operandosList)

#Codigo intermedio de ifs
def gotoFalse(x):
    #If - 1
    #For - 2
    #While -3
    #/DOWHILE - 4
    #operador: goto - - -
    operadorList.append('gotoF')
    opA_list.append(operandosList.pop())
    opB_list.append('-')
    tempList.append('-')
    if (x == 1):
        saltos.append(len(tempList)-1)
    elif (x == 2):
        saltos.append(len(tempList)-1)
        saltos.append(len(tempList)-2)
    elif (x ==3):
        #opB_list[len(tempList)-1] = saltos.pop()
        saltos.append(len(tempList)-2)
        saltos.append(len(tempList)-1)
        temp.append(opA_list[len(opA_list)-1])
    # else:
    #     opB_list[len(opB_list)-1] = saltos.pop()
    #print("Lista de saltos:", saltos)
def gotoFalseDW():
    operadorList.append('gotoFDW')
    opA_list.append(operandosList.pop())
    opB_list.append(saltos.pop())
    tempList.append('-')
    temp.append(opA_list[len(opA_list)-1])

def goto(x):
    operadorList.append('goto')
    opA_list.append('-')
    opB_list.append('-')
    tempList.append('-')
    opB_list[saltos.pop()] = len(tempList)
    if (x == 3):
        #print(operadorList[len(tempList)-1])
        opB_list[len(tempList)-1] = saltos.pop()
        #temp.append(opB_list[len(opB_list)-1])
    else:
        saltos.append(len(tempList)-1)
def endIf():
    opB_list[saltos.pop()] = len(tempList)
#agregar a donde voy a saltar en el goto
def endProgram():
    operadorList.append('end')
    opA_list.append('-')
    opB_list.append('-')
    tempList.append('-')
def startProgram():
    operadorList.append('goto')
    opA_list.append('-')
    opB_list.append('-')
    tempList.append('-')
#INCOMPLETOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Function when FOR finishes
def endFor():
    global tempID
    #Actualizar variable controladora
    #Cuadruplo: + variable temp-global 1 temp
    #print('operandosFor',operandosList)
    operadorList.append('+')
    indentifier = operandosList.pop()
    opA_list.append(indentifier) #cambiar estoooo
    opB_list.append(-1)
    tempList.append(temp.pop(0))
    #Agrega ultimo operando a la lista para usarse en el siguiente cuadruplo
    operandosList.append(tempList[len(tempList)-1])
    #Igualar valor a variable controladora
    #Cuadruplo: = ID valor(temp)
    operadorList.append('=')
    opA_list.append(indentifier)
    opB_list.append(operandosList.pop())
    tempList.append('-')
    temp.append(opB_list[len(opB_list)-1]) #Regresa temp a la lista
    #gotoFOR
    retorno = saltos.pop()
    operadorList.append('goto')
    opA_list.append('-')
    opB_list.append(retorno)
    tempList.append('-')
    opB_list[saltos.pop()] = len(tempList)

#def endProcedure:
    #crear goto a donde nos quedamos en los calls
#EJECUCIOOOOOOOONN
def execution():
    global save_PC
    PC = 0
    #print(operadorList[PC],opA_list[PC],opB_list[PC],tempList[PC])
    while (operadorList[PC] != 'end'):
        #print('PC: ', PC)
        #print(dim_values)
        if (opA_list[PC] == '-'):
            pass
        elif (int(opA_list[PC]) < 1): #es una constante
            a = int(opA_list[PC])*(-1)
        elif (int(opA_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
            a = temp_exe[int(opA_list[PC])-100]
        elif (int(opA_list[PC]) >= 1 and opA_list[PC] <= 100 ): # es
            #buscar index en
            if (operadorList[PC] == '='):
                a = int(opA_list[PC])
            else:
                a =  values_table[int(opA_list[PC])-1]
        elif (int(opA_list[PC]) >= 300):
            #print('value',dim_values[temp_exe[int(opA_list[PC])-300]])
            #print(len(dim_values))
            a = dim_values[temp_exe[int(opA_list[PC])-300]]
            #print(a)

        if (opB_list[PC] == '-'):
            pass
        elif (int(opB_list[PC]) < 1): #es una constante
            b = opB_list[PC]*(-1)
        elif (int(opB_list[PC]) >= 100 and int(opB_list[PC]) < 300): #es un temporal
            b = int(opB_list[PC])-100
        elif (int(opB_list[PC]) >= 1 and int(opB_list[PC]) <= 100 ): # es
            #print(int(opB_list[PC]))
            if (operadorList[PC] == r'>=|<=|>|<|==|!='):
                b =  values_table[int(opB_list[PC])]
            else:
                b = opB_list[PC]
        elif (int(opB_list[PC]) >= 300):
            b = dim_values[temp_exe[int(opB_list[PC])-300]]

        #if (opA_list[PC] != '-'):
            #print('a: ',a)
        #if (opB_list[PC] != '-'):
            #print('b: ',b)

        if (operadorList[PC] == '+'):

            if (int(opA_list[PC]) < 1): #es una constante
                a = opA_list[PC]*(-1)
            elif (int(opA_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                a = temp_exe[int(opA_list[PC])-100]
            elif (int(opA_list[PC]) >= 1 and opA_list[PC] <= 100 ): #es una variable
                a = values_table[int(opA_list[PC])-1]
            elif (int(opA_list[PC]) >= 300): #es dim
                a = dim_values[temp_exe[int(opA_list[PC])-300]]
            if (int(opB_list[PC]) < 1): #es una constante
                b = opB_list[PC]*(-1)
            elif (int(opB_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                b = temp_exe[int(opB_list[PC])-100]
            elif (int(opB_list[PC]) >= 1 and opB_list[PC] <= 100 ):
                b = values_table[int(opB_list[PC]-1)]
            elif (int(opB_list[PC]) >= 300):
                b = dim_values[temp_exe[int(opB_list[PC])-300]]
            temp_exe[int(tempList[PC])-100] = int(a+b) if (isinstance(a, int) and isinstance(b, int)) else float(a+b)
            #print('suma: ', a, '+', b, '=', a+b)
            PC += 1

        elif (operadorList[PC] == '-'):

            if (int(opA_list[PC]) < 1): #es una constante
                a = opA_list[PC]*(-1)
            elif (int(opA_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                a = temp_exe[int(opA_list[PC])-100]
            elif (int(opA_list[PC]) >= 1 and opA_list[PC] <= 100 ):
                a = values_table[int(opA_list[PC])-1]
            elif (int(opA_list[PC]) >= 300):
                a = dim_values[temp_exe[int(opA_list[PC])-300]]
            if (int(opB_list[PC]) < 1): #es una constante
                b = opB_list[PC]*(-1)
            elif (int(opB_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                b = temp_exe[int(opB_list[PC])-100]
            elif (int(opB_list[PC]) >= 1 and opB_list[PC] <= 100 ):
                b = values_table[int(opB_list[PC]-1)]
            elif (int(opB_list[PC]) >= 300):
                b = dim_values[temp_exe[int(opB_list[PC])-300]]
            temp_exe[int(tempList[PC])-100] = int(a-b) if (isinstance(a, int) and isinstance(b, int)) else float(a-b)
            PC += 1

        elif (operadorList[PC] == '*'):

            if (int(opA_list[PC]) < 1): #es una constante
                a = opA_list[PC]*(-1)
            elif (int(opA_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                a = temp_exe[int(opA_list[PC])-100]
            elif (int(opA_list[PC]) >= 1 and opA_list[PC] <= 100 ):
                a = values_table[int(opA_list[PC])-1]
            elif (int(opA_list[PC]) >= 300):
                a = dim_values[temp_exe[int(opA_list[PC])-300]]
            if (int(opB_list[PC]) < 1): #es una constante
                b = opB_list[PC]*(-1)
            elif (int(opB_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                b = temp_exe[int(opB_list[PC])-100]
            elif (int(opB_list[PC]) >= 1 and opB_list[PC] <= 100 ):
                b = values_table[int(opB_list[PC]-1)]
            elif (int(opB_list[PC]) >= 300):
                b = dim_values[temp_exe[int(opB_list[PC])-300]]
            temp_exe[int(tempList[PC])-100] = int(a*b) if (isinstance(a, int) and isinstance(b, int)) else float(a*b)
            #print('mul: ', a, '*', b, '=', a*b)
            PC += 1

        elif (operadorList[PC] == '/'):
            #print('entro al div')
            if (int(opA_list[PC]) < 1): #es una constante
                a = opA_list[PC]*(-1)
            elif (int(opA_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                a = temp_exe[int(opA_list[PC])-100]
            elif (int(opA_list[PC]) >= 1 and opA_list[PC] <= 100 ):
                a = values_table[int(opA_list[PC])-1]
            elif (int(opA_list[PC]) >= 300):
                a = dim_values[temp_exe[int(opA_list[PC])-300]]
            if (int(opB_list[PC]) < 1): #es una constante
                b = opB_list[PC]*(-1)
            elif (int(opB_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                b = temp_exe[int(opB_list[PC])-100]
            elif (int(opB_list[PC]) >= 1 and opB_list[PC] <= 100 ):
                b = values_table[int(opB_list[PC]-1)]
            elif (int(opB_list[PC]) >= 300):
                b = dim_values[temp_exe[int(opB_list[PC])-300]] #checa si las variables dimensionadas
            #print(a,b)
            temp_exe[int(tempList[PC])-100] = int(a/b) if (isinstance(a, int) and isinstance(b, int)) else float(a/b)
            PC += 1

        elif (operadorList[PC] == '>='):

            if (int(opA_list[PC]) < 1): #es una constante
                a = opA_list[PC]*(-1)
            elif (int(opA_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                a = temp_exe[int(opA_list[PC])-100]
            elif (int(opA_list[PC]) >= 1 and opA_list[PC] <= 100 ):
                a = values_table[int(opA_list[PC])-1]
            elif (int(opA_list[PC]) >= 300):
                a = dim_values[temp_exe[int(opA_list[PC])-300]]
            if (int(opB_list[PC]) < 1): #es una constante
                b = opB_list[PC]*(-1)
            elif (int(opB_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                b = temp_exe[int(opB_list[PC])-100]
            elif (int(opB_list[PC]) >= 1 and opB_list[PC] <= 100 ):
                b = values_table[int(opB_list[PC]-1)]
            elif (int(opB_list[PC]) >= 300):
                b = dim_values[temp_exe[int(opB_list[PC])-300]] #checa si las variables dimensionadas

            temp_exe[int(tempList[PC])-100] = a>=b
            PC += 1
        elif (operadorList[PC] == '<='):

            if (int(opA_list[PC]) < 1): #es una constante
                a = opA_list[PC]*(-1)
            elif (int(opA_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                a = temp_exe[int(opA_list[PC])-100]
            elif (int(opA_list[PC]) >= 1 and opA_list[PC] <= 100 ):
                a = values_table[int(opA_list[PC])-1]
            elif (int(opA_list[PC]) >= 300):
                a = dim_values[temp_exe[int(opA_list[PC])-300]]
            if (int(opB_list[PC]) < 1): #es una constante
                b = opB_list[PC]*(-1)
            elif (int(opB_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                b = temp_exe[int(opB_list[PC])-100]
            elif (int(opB_list[PC]) >= 1 and opB_list[PC] <= 100 ):
                b = values_table[int(opB_list[PC]-1)]
            elif (int(opB_list[PC]) >= 300):
                b = dim_values[temp_exe[int(opB_list[PC])-300]] #checa si las variables dimensionadas

            #print('menor o igual AQUI')
            temp_exe[int(tempList[PC])-100] = a<=b
            #print(temp_exe[int(tempList[PC])-100])
            PC += 1
        elif (operadorList[PC] == '>'):

            if (int(opA_list[PC]) < 1): #es una constante
                a = opA_list[PC]*(-1)
            elif (int(opA_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                a = temp_exe[int(opA_list[PC])-100]
            elif (int(opA_list[PC]) >= 1 and opA_list[PC] <= 100 ):
                a = values_table[int(opA_list[PC])-1]
            elif (int(opA_list[PC]) >= 300):
                a = dim_values[temp_exe[int(opA_list[PC])-300]]
            if (int(opB_list[PC]) < 1): #es una constante
                b = opB_list[PC]*(-1)
            elif (int(opB_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                b = temp_exe[int(opB_list[PC])-100]
            elif (int(opB_list[PC]) >= 1 and opB_list[PC] <= 100 ):
                b = values_table[int(opB_list[PC]-1)]
            elif (int(opB_list[PC]) >= 300):
                b = dim_values[temp_exe[int(opB_list[PC])-300]] #checa si las variables dimensionadas
            #print('a',a,'b',b)
            temp_exe[int(tempList[PC])-100] = a>b
            PC += 1
        elif (operadorList[PC] == '<'):

            if (int(opA_list[PC]) < 1): #es una constante
                a = opA_list[PC]*(-1)
            elif (int(opA_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                a = temp_exe[int(opA_list[PC])-100]
            elif (int(opA_list[PC]) >= 1 and opA_list[PC] <= 100 ):
                a = values_table[int(opA_list[PC])-1]
            elif (int(opA_list[PC]) >= 300):
                a = dim_values[temp_exe[int(opA_list[PC])-300]]
            if (int(opB_list[PC]) < 1): #es una constante
                b = opB_list[PC]*(-1)
            elif (int(opB_list[PC]) >= 100 and int(opA_list[PC]) < 300): #es un temporal
                b = temp_exe[int(opB_list[PC])-100]
            elif (int(opB_list[PC]) >= 1 and opB_list[PC] <= 100 ):
                b = values_table[int(opB_list[PC]-1)]
            elif (int(opB_list[PC]) >= 300):
                a = dim_values[temp_exe[int(opB_list[PC])-300]] #checa si las variables dimensionadas
            #print(type(a),type(b))
            temp_exe[int(tempList[PC])-100] = a<b
            PC += 1

        elif (operadorList[PC] == '=='):
            temp_exe[int(tempList[PC])-100] = a==b
            PC += 1
        elif (operadorList[PC] == '!='):
            temp_exe[int(tempList[PC])-100] = a!=b
            PC += 1
        elif (operadorList[PC] == '='):
            #print('entro')
            if (int(opA_list[PC]) >= 300): # si es dim
                #checar el valor del temp en temp_pexe y eso poner en el resultado
                if (int(opB_list[PC]) >= 100 and int(opB_list[PC]) < 300 ):
                    dim_values[temp_exe[opA_list[PC]-300]] = temp_exe[int(opB_list[PC])-100]
                    #print("aquiiii",temp_exe[b])
                elif (int(opB_list[PC]) <= 0): # es una constante
                    dim_values[temp_exe[opA_list[PC]-300]] = opB_list[PC]*(-1)
                elif (int(opB_list[PC]) > 0 and int(opB_list[PC]) < 100):
                    dim_values[temp_exe[opA_list[PC]-300]] = values_table[int(opB_list[PC])-1]
                else: #Es una variable dimensionada
                    dim_values[temp_exe[opA_list[PC]-300]] = dim_values[temp_exe[opB_list[PC]-300]]#checar el valor del operador b en la lista de valores
            else: # si es una variable
                if (int(opB_list[PC]) >= 100 and int(opB_list[PC]) < 300 ):
                    values_table[int(opA_list[PC])-1] = temp_exe[b]
                    #print("aquiiii",temp_exe[b])
                elif (int(opB_list[PC]) <= 0): # es una constante
                    values_table[int(opA_list[PC])-1] = opB_list[PC]*(-1)
                elif (int(opB_list[PC]) >= 300): #esdim
                    values_table[int(opA_list[PC])-1] = dim_values[temp_exe[int(opB_list[PC])-300]]
                else:
                    values_table[int(opA_list[PC])-1] = values_table[int(opB_list[PC])-1]#checar el valor del operador b en la lista de valores
            PC += 1
            #print(PC)
        elif (operadorList[PC] == 'goto'):
            PC = opB_list[PC]
        elif (operadorList[PC] == 'gotoF'):
            if (a):
                PC += 1
            else:
                PC = opB_list[PC]
        elif (operadorList[PC] == 'gotoFDW'):
            #print('gotoFalsoDF: ', a)
            if (a):
                PC = opB_list[PC]
            else:
                PC += 1
        elif (operadorList[PC] == 'call'):
            save_PC = PC + 1
            PC = int(opB_list[PC])
            #print('pccount:',save_PC)
        elif (operadorList[PC] == 'end'):
            #print('end of program')
            break;
        elif (operadorList[PC] == 'verify'):
            if (opA_list[PC] < 1):
                var = opA_list[PC]*(-1)
            elif (int(opA_list[PC]) >= 1 and int(opA_list[PC]) < 100): # es una variable
                var = values_table[opA_list[PC]-1]
            if (var < opB_list[PC] or var > tempList[PC]):
                raise Exception('Index out of range.')
            PC += 1
        elif (operadorList[PC] == 'endProcedure'):
            #Regresar a donde se quedamo
            PC = save_PC
        elif (operadorList[PC] == 'output'):
            if (opA_list[PC] < 1):
                print(opA_list[PC]*(-1))
            elif (int(opA_list[PC]) >= 1 and int(opA_list[PC]) < 100): # es una variable
                print(values_table[opA_list[PC]-1])
            else: #es dimensionada
                print(dim_values[temp_exe[int(opA_list[PC])-300]])
            PC += 1
        elif (operadorList[PC] == 'input'):
            #op A es el index de la variable
            inp = input('Ingrese entrada: ')
            values_table[opA_list[PC]-1] = int(inp) if type_table[opA_list[PC]-1] == 'INT' else float(inp)

            PC += 1
        #else:
            #print('entra aqui')
        #print('PC', PC)
        #print(temp_exe)
        #print_table()
