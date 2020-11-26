from symbol_table import *

dimFlag = False
dimID = 0
Tf = 0
ID = 0
cont = 0
texto = []
saltos = []
indexCuadruplo = []
operandos = []
operador = []
operando1 = []
operando2 = []
resultado = []
temporales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
listTemporales = list(range(100, 141))


def dimCarac(p, num):
    global tableID
    i = 1
    if p == "array":
        dim = (operandos.pop() * (-1))
        while i <= num:
            tableValue[len(tableID) - (num - i) - 1] = [dim, len(dimValue)]
            for x in range(dim):
                dimValue.append(0)
            i += 1
    elif p == "matrix":
        dim2 = (operandos.pop() * (-1))
        dim = (operandos.pop() * (-1))
        while i <= num:
            tableValue[len(tableID) - (num - i) - 1] = [dim, dim2, len(dimValue)]
            for x in range(dim * dim2):
                dimValue.append(0)
            i += 1
    else:
        dim3 = (operandos.pop() * (-1))
        dim2 = (operandos.pop() * (-1))
        dim = (operandos.pop() * (-1))
        m1 = dim2 * dim3
        while i <= num:
            tableValue[len(tableID) - (num - i) - 1] = [dim, dim2, dim3, len(dimValue), m1]
            for x in range(m1 * dim):
                dimValue.append(0)
            i += 1


def genCuadruplo(x):
    global operando1
    global operando2
    global operandos
    global operador
    global listTemporales
    global resultado
    global cont
    indexCuadruplo.append(cont)
    cont += 1
    operando2.append(operandos.pop())
    operando1.append(operandos.pop())
    operador.append(x)

    if x == "=":
        resultado.append("--")
    else:
        resultado.append(listTemporales.pop(0))
        operandos.append(resultado[resultado.__len__() - 1])

    if 99 < operando1[operando1.__len__() - 1] < 200:
        listTemporales.append(operando1[operando1.__len__() - 1])
    elif operando1[operando1.__len__() - 1] > 199:
        listTemporales.append(operando1[operando1.__len__() - 1] - 100)

    if 99 < operando2[operando2.__len__() - 1] < 200:
        listTemporales.append(operando2[operando2.__len__() - 1])
    elif operando2[operando2.__len__() - 1] > 199:
        listTemporales.append(operando2[operando2.__len__() - 1] - 100)


def pushOperandos(x):
    global operandos
    operandos.append(x)


def gotofalso():
    global saltos
    global cont
    global operando1
    global operando2
    global operador
    global resultado
    indexCuadruplo.append(cont)
    cont += 1
    operador.append("gotofalso")
    operando1.append(operandos.pop())
    operando2.append("--")
    resultado.append("--")
    saltos.append(cont - 1)


def goto():
    global cont
    global saltos
    global operando1
    global operando2
    global operador
    global resultado
    indexCuadruplo.append(cont)
    cont += 1
    operador.append("goto")
    operando1.append("--")
    operando2.append("--")
    resultado.append("--")
    operando2[saltos.pop()] = cont
    saltos.append(cont - 1)


def finIF():
    global operando2
    global saltos
    global cont
    operando2[saltos.pop()] = cont


def genCuadruploCLS():
    global cont
    global operando1
    global operando2
    global operador
    global resultado
    indexCuadruplo.append(cont)
    cont += 1
    operador.append("CLS")
    operando1.append("--")
    operando2.append("--")
    resultado.append("--")


def origen():
    global cont
    saltos.append(cont)


def finWhile():
    global cont
    global saltos
    global operando1
    global operando2
    global operador
    global resultado
    indexCuadruplo.append(cont)
    cont += 1
    operando2[saltos.pop()] = cont
    operador.append("goto")
    operando1.append("--")
    operando2.append(saltos.pop())
    resultado.append("--")


def finDoWhile():
    global saltos
    global cont
    global operando1
    global operando2
    global operador
    global resultado
    indexCuadruplo.append(cont)
    cont += 1
    operador.append("gotofalso")
    operando1.append(operandos.pop())
    operando2.append(saltos.pop())
    resultado.append("--")


def genCuadruploFor(x):
    global operando1
    global operando2
    global operandos
    global operador
    global listTemporales
    global resultado
    global cont
    global ID
    indexCuadruplo.append(cont)
    cont += 1
    operando2.append(operandos.pop())
    ID = operandos.pop()
    operando1.append(ID)
    operador.append(x)
    resultado.append("--")
    operandos.append(operando1[operando1.__len__() - 1])

    if operando1[operando1.__len__() - 1] > 99:
        listTemporales.append(operando1[operando1.__len__() - 1])

    if operando2[operando2.__len__() - 1] > 99:
        listTemporales.append(operando2[operando2.__len__() - 1])


def forAction3():
    global operandos
    global operador
    global operando1
    global operando2
    global resultado
    global listTemporales
    global cont
    global ID
    global Tf
    indexCuadruplo.append(cont)
    cont += 1
    operador.append("=")
    operando1.append(listTemporales.pop(0))  # liberar
    operando2.append(operandos.pop())
    resultado.append("--")
    operandos.append(operando1[operando1.__len__() - 1])
    indexCuadruplo.append(cont)
    cont += 1
    Tf = operandos.pop()
    operador.append("<=")
    operando1.append(ID)
    operando2.append(Tf)
    resultado.append(listTemporales.pop(0))
    operandos.append(resultado[resultado.__len__() - 1])
    indexCuadruplo.append(cont)
    cont += 1
    operador.append("gotofalso")
    operando1.append(operandos.pop())
    operando2.append("--")
    resultado.append("--")
    listTemporales.append(operando1[operando1.__len__() - 1])
    saltos.append(cont - 2)


def finFor():
    global operandos
    global operador
    global operando1
    global operando2
    global resultado
    global listTemporales
    global cont
    global ID
    global tf
    indexCuadruplo.append(cont)
    cont += 1
    ID = operandos.pop()
    operador.append("+")
    operando1.append(ID)
    operando2.append(-1)
    resultado.append(listTemporales.pop(0))
    operandos.append(resultado[resultado.__len__() - 1])
    indexCuadruplo.append(cont)
    cont += 1
    operador.append("=")
    operando1.append(ID)
    operando2.append(operandos.pop())
    resultado.append("--")
    # operandos.append(resultado[resultado.__len__() - 1])
    listTemporales.append(operando2[operando2.__len__() - 1])
    indexCuadruplo.append(cont)
    cont += 1
    retorno = saltos.pop()
    operador.append("goto")
    operando1.append("--")
    operando2.append(retorno)
    resultado.append("--")
    operando2[retorno + 1] = cont
    listTemporales.append(Tf)


def genCuadruploGOSUB(ID):
    global operador
    global operando1
    global operando2
    global resultado
    global cont
    indexCuadruplo.append(cont)
    cont += 1
    operador.append("gotosub")
    operando1.append("--")
    operando2.append(tableValue[ID - 1])
    resultado.append("--")


def SP_insert(ID):
    global cont
    SP_insertID(ID, cont)


def genCuadruploINPUT(var):
    global operador
    global operando1
    global operando2
    global resultado
    global cont
    global texto
    indexCuadruplo.append(cont)
    cont += 1
    texto.append(var[1:(len(var) - 1)])
    operador.append("INPUT")
    operando1.append(texto.__len__() - 1)
    operando2.append(operandos.pop())
    resultado.append("--")


def genCuadruploPRINT(var):
    global operador
    global operando1
    global operando2
    global resultado
    global cont
    global texto
    global indexCuadruplo
    indexCuadruplo.append(cont)
    cont += 1
    texto.append(var[1:(len(var) - 1)])
    if var == " ":
        operando1.append("--")
        operando2.append(operandos.pop())
    else:
        operando1.append(texto.__len__() - 1)
        operando2.append("--")

    operador.append("PRINT")
    resultado.append("--")


def genFirstGoto():
    global operador
    global operando1
    global operando2
    global resultado
    global cont
    global indexCuadruplo
    indexCuadruplo.append(cont)
    cont += 1
    operador.append("goto")
    operando1.append("--")
    operando2.append("--")
    resultado.append("--")


def rellenarFirstGoto():
    global cont
    global operando2
    operando2[0] = cont


def finDePrograma():
    global operador
    global operando1
    global operando2
    global resultado
    global cont
    global indexCuadruplo
    indexCuadruplo.append(cont)
    operador.append("finprograma")
    operando1.append("--")
    operando2.append("--")
    resultado.append("--")


def spReturn():
    global operador
    global operando1
    global operando2
    global resultado
    global cont
    global indexCuadruplo
    indexCuadruplo.append(cont)
    cont += 1
    operador.append("return")
    operando1.append("--")
    operando2.append("--")
    resultado.append("--")


def dimensionadas_ARRAY():
    global indexCuadruplo
    global dimID
    global cont
    indexCuadruplo.append(cont)
    cont += 1
    s1 = operandos.pop()
    dimID = operandos.pop()
    carID = tableValue[dimID - 1]
    operando1.append(s1)
    operando2.append(carID[0] * (-1))
    resultado.append("--")
    operador.append("verficar")

    indexCuadruplo.append(cont)
    cont += 1
    operador.append("+")
    operando1.append(s1)
    operando2.append(carID[1] * (-1))
    resultado.append(listTemporales.pop(0))
    operandos.append(resultado[len(resultado) - 1] + 100)


def dimensionadas_MATRIX():
    global indexCuadruplo
    global dimID
    global cont
    indexCuadruplo.append(cont)
    cont += 1
    s2 = operandos.pop()
    s1 = operandos.pop()
    dimID = operandos.pop()
    carID = tableValue[dimID - 1]
    operando1.append(s1)
    operando2.append(carID[0] * (-1))
    resultado.append("--")
    operador.append("verficar")

    indexCuadruplo.append(cont)
    cont += 1
    operador.append("*")
    operando1.append(s1)
    operando2.append(carID[1] * (-1))
    resultado.append(listTemporales.pop(0))
    operandos.append(resultado[len(resultado) - 1])

    indexCuadruplo.append(cont)
    cont += 1
    operando1.append(s2)
    operando2.append(carID[1] * (-1))
    resultado.append("--")
    operador.append("verficar")

    indexCuadruplo.append(cont)
    cont += 1
    operando1.append(operandos.pop())
    operando2.append(s2)
    operador.append("+")
    resultado.append(listTemporales.pop(0))
    operandos.append(resultado[len(resultado) - 1])
    if operando1[operando1.__len__() - 1] > 99:
        listTemporales.append(operando1[operando1.__len__() - 1])

    indexCuadruplo.append(cont)
    cont += 1
    operando1.append(operandos.pop())
    operando2.append(carID[2] * (-1))
    operador.append("+")
    resultado.append(listTemporales.pop(0))
    operandos.append(resultado[len(resultado) - 1] + 100)
    if operando1[operando1.__len__() - 1] > 99:
        listTemporales.append(operando1[operando1.__len__() - 1])


def dimensionadas_CUBE():
    global indexCuadruplo
    global dimID
    global cont
    indexCuadruplo.append(cont)
    cont += 1
    s3 = operandos.pop()
    s2 = operandos.pop()
    s1 = operandos.pop()
    dimID = operandos.pop()
    carID = tableValue[dimID - 1]
    operando1.append(s1)
    operando2.append(carID[0] * (-1))
    resultado.append("--")
    operador.append("verficar")

    indexCuadruplo.append(cont)
    cont += 1
    operador.append("*")
    operando1.append(s1)
    operando2.append(carID[4] * (-1))
    resultado.append(listTemporales.pop(0))
    operandos.append(resultado[len(resultado) - 1])

    indexCuadruplo.append(cont)
    cont += 1
    operando1.append(s2)
    operando2.append(carID[1] * (-1))
    resultado.append("--")
    operador.append("verficar")

    indexCuadruplo.append(cont)
    cont += 1
    operador.append("*")
    operando1.append(s2)
    operando2.append(carID[2] * (-1))
    resultado.append(listTemporales.pop(0))
    operandos.append(resultado[len(resultado) - 1])

    indexCuadruplo.append(cont)
    cont += 1
    operando1.append(operandos.pop())
    operando2.append(operandos.pop())
    operador.append("+")
    resultado.append(listTemporales.pop(0))
    operandos.append(resultado[len(resultado) - 1])
    if operando1[operando1.__len__() - 1] > 99:
        listTemporales.append(operando1[operando1.__len__() - 1])
    if operando2[operando2.__len__() - 1] > 99:
        listTemporales.append(operando2[operando2.__len__() - 1])

    indexCuadruplo.append(cont)
    cont += 1
    operando1.append(s3)
    operando2.append(carID[2] * (-1))
    resultado.append("--")
    operador.append("verficar")

    indexCuadruplo.append(cont)
    cont += 1
    operando1.append(operandos.pop())
    operando2.append(s3)
    operador.append("+")
    resultado.append(listTemporales.pop(0))
    operandos.append(resultado[len(resultado) - 1])
    if operando1[operando1.__len__() - 1] > 99:
        listTemporales.append(operando1[operando1.__len__() - 1])

    indexCuadruplo.append(cont)
    cont += 1
    operando1.append(operandos.pop())
    operando2.append(carID[3] * (-1))
    operador.append("+")
    resultado.append(listTemporales.pop(0))
    operandos.append(resultado[len(resultado) - 1] + 100)
    if operando1[operando1.__len__() - 1] > 99:
        listTemporales.append(operando1[operando1.__len__() - 1])


def imprimirCuadruplos():
    cuadruplos = "\n".join("{5} {0:3} {5} {1:12} {5} {2:5} {5} {3:5} {5} {4:5} {5}"
                           .format(v, w, x, y, z, '|') for v, w, x, y, z, in zip(indexCuadruplo,
                                                                                 operador, operando1, operando2,
                                                                                 resultado))
    print("\nCuadruplos generados:\n\n" + cuadruplos + "\n")
    print("\n")
