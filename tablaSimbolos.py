global ID_table
global type_table
global values_table
global counter
global temp #Variable saves last type
global mod
global dim_values

#counter = 0
ID_table = []
type_table = []
values_table = []
dim_values = []

def set_ID(p):
    global ID_table
    if (p in ID_table):
        raise Exception("\nError, variable --"+str(p)+"-- is already declared")
    else:
        #print("Listo")
        ID_table.append(p)
        #print(p)
        #print(ID_table)
        type_table.append(temp)
        values_table.append(0) if (temp == 'INT') else values_table.append(0.0)

def set_type(p):
    global type_table
    global temp
    #print("Listo")
    temp = p
    #print(p)

def print_table():
    # symboltable = "\n".join("{2} {0:5s} {2} {1:20s} {2} {3:10}".format(w, x, '|', y) for w, x, y in zip(ID_table,type_table,values_table))
    # print(symboltable)

    for i in range(len(type_table)):
        print(type_table[i], ' | ', ID_table[i], ' | ', values_table[i])
    print('\n')
