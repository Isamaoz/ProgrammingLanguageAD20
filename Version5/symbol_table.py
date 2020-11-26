global tableID
global tableType
global tableValue
global repetido
global indice
global contador
global dimValue

dimValue = []
tableID = []
tableType = []
tableValue = []
indice = []
contador = 0
repetido = False

def insertType(p):
	global tableID
	global tableType
	global repetido
	global dimValue
	global operandos
	if not repetido:
		cont = 0
		while len(tableID) > len(tableType):
			cont+=1
			tableType.append(p)
			tableValue.append("--")
		return cont
def insertID(p):
	global contador
	global repetido
	global tableID
	contador+=1
	for x in tableID:
		if x == p:
			repetido = True
			print ("\nError, variable --"+str(p)+"-- is already declared")
			break
	if not repetido:
		tableID.append(p)
		indice.append(contador)

def SP_insertID(p, cont):
	global contador
	global repetido
	global tableID
	contador+=1
	for x in tableID:
		if x == p:
			repetido = True
			print ("\nError, variable --"+str(p)+"-- is already declared")
			break
	if not repetido:
		tableID.append(p)
		tableType.append("SP")
		tableValue.append(cont)
		indice.append(contador)


def imprimirSymbolTable():
	global repetido
	global tableType
	global tableID

	if not repetido:
		symboltable = "\n".join("{3} {0:3} {3} {1:8s} {3} {2:6s} {3}".format(w, x, y, '|')for w, x, y in zip(indice, tableID, tableType))
		print ("\nTabla de simbolos:\n\n")
		print (symboltable)
		print ("\n\n")
		print ("Table value")
		print (tableValue)
	else:
		tableID = []
		tableType = []
		print ("\nError in the symbol table")

	print(tableValue)

def buscar(id):
	return int(tableID.index(id) + 1)
