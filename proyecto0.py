# -*- coding: utf-8 -*-

archivo = open('prueba1.txt' , 'r')

variables = {}

funciones = []

almacenamiento = {}

posiciones=[':around',':left', ':right']
posiciones2=[':front',':left', ':right',':back']
puntos_cardinales=[':north',':east',':west',':south']
objetos=['Balloons', 'Chips']

def main (archivo):
    
    for linea in archivo:
        solucion= False
        linea_leida = recorrido(linea)
        
        if linea_leida == True:
            solucion = True
        else:
            solucion
            break
    
    print(solucion)
    
def recorrido(linea):
    
    linea = linea.lstrip(' ')
    lista_linea = linea.split(' ')
    lista_linea[0]= lista_linea[0].strip('\n')
    solucion = False
    boolean = ["BLOCKEDP","!BLOCKEDP", " BLOCKEDP", " !BLOCKEDP"]
    var = (lista_linea[0].strip(")"))
    
        
    if lista_linea[0] == '':
        solucion = True
        
    elif lista_linea[0] == '(defvar':
        respuesta = defvar(lista_linea,variables)
        if respuesta == True:
            solucion = True
        else:
            solucion
        
    elif lista_linea[0] == '(move':
        respuesta = move(lista_linea,variables)
        if respuesta == True:
            solucion = True
        else:
            solucion
            
        
    elif lista_linea[0] == '(=':
        respuesta = equal(lista_linea,variables)
        if respuesta == True:
            solucion = True
        else:
            solucion
            
                
    elif lista_linea[0] == '(turn':
        respuesta = turn(lista_linea,variables)
        if respuesta == True:
            solucion = True
        else:
            solucion
            
                
    elif lista_linea[0] == '(face':
        respuesta = face(lista_linea)
        if respuesta == True:
            solucion = True
        else:
            solucion
            
                
    elif lista_linea[0] == '(put':
        respuesta = put(lista_linea,variables)
        if respuesta == True:
            solucion = True
        else:
            solucion
            
                
    elif lista_linea[0] == '(pick':
        respuesta = pick(lista_linea,variables)
        if respuesta == True:
            solucion = True
        else:
            solucion
    
    elif lista_linea[0] == '(move-dir':
        respuesta = move_dir(lista_linea,variables)
        if respuesta == True:
            solucion = True
        else:
            solucion

    elif lista_linea[0] == '(run-dirs':
        respuesta = run_dirs(lista_linea,variables)
        if respuesta == True:
            solucion = True
        else:
            solucion

    elif lista_linea[0] == '(move-face':
        respuesta = move_face(lista_linea,variables)
        if respuesta == True:
            solucion = True
        else:
            solucion
    elif lista_linea[0] == '(skip':
        respuesta = skip(lista_linea)
        if respuesta == True:
            solucion = True
        else:
            solucion    

    elif lista_linea[0] == 'IF' and (lista_linea[1] in boolean) and (lista_linea[2][0] == "["):
        respuesta = if_command(linea)
        if respuesta == True:
            solucion = True
        else:
            solucion
                        
            
    elif lista_linea[0] == '(BLOCK' or lista_linea[0] == '( BLOCK':
        respuesta = block(linea)
        if respuesta == True:
            solucion = True
        else:
            solucion
            
    elif (lista_linea[0] == '(REPEAT'or lista_linea[0] == '( REPEAT') and (lista_linea[1].isdigit() == True) :
        respuesta = repeat(linea)
        if respuesta == True:
            solucion = True
        else:
            solucion
    
    elif lista_linea[0] == 'TO':
        respuesta = to_end(linea,lista_linea)
        if respuesta == True:
            solucion = True
        else:
            solucion
            
    elif str(var) in funciones:
        solucion = True

    else:
        solucion = False
        
    return solucion

        

# Función para comando 'defvar'
def defvar(lista:list, variables:dict):
    tamanio = len(lista)
    respuesta = False
    if tamanio == 3:
        lista[2]= lista[2].strip('\n')
        lista[2]=lista[2].strip(')')
        if (lista[2].isdigit() == True) and (lista[1].isdigit() == False):
            respuesta = True
            variables[lista[1]] = lista[2]
    return respuesta
    


# Función para comando 'move'
def move(lista:list, variables:dict):
    tamanio = len(lista)
    respuesta = False
    if tamanio == 2:
        lista[1]= lista[1].strip('\n')
        lista[1]= lista[1].lstrip(")")
        if lista[1].isdigit() == True:
            respuesta = True
        elif (lista[1].isdigit() == False) and (lista[1].islower()== True):
            for elemento in variables:
                if lista[1] == elemento:
                    respuesta = True
    
    return respuesta


# Función para =
def equal(lista:list, variables:dict):
    tamanio = len(lista)
    respuesta = False
    if tamanio == 3:
        lista[2]= lista[2].strip('\n')
        lista[2]=lista[2].strip(')')
        if (lista[2].isdigit() == True) and (lista[1].isdigit() == False):
            respuesta = True
            variables[lista[1]] = lista[2]
    return respuesta


# Función para comando 'turn'
def turn(lista:list,variables:dict):
    tamanio = len(lista)
    respuesta = False
    if tamanio == 2:
        lista[1]= lista[1].strip('\n')
        lista[1]= lista[1].lstrip(")")
        if (lista[1] in posiciones):
            respuesta = True   
    return respuesta


# Función para comando 'face'
def face(lista:list):
    tamanio = len(lista)
    respuesta = False
    if tamanio == 2:
        lista[1]= lista[1].strip('\n')
        lista[1]= lista[1].strip(')')
        if lista[1] in puntos_cardinales:
            respuesta = True  
    return respuesta

# Función para comando 'put X n'
def put(lista:list,variables:dict):
    tamanio = len(lista)
    respuesta = False
    if tamanio == 3:
        lista[2]= lista[2].strip('\n')
        lista[2]= lista[2].lstrip(")")
        if lista[2].isdigit() == True and lista[1] in objetos:
            respuesta = True
        elif (lista[1].isdigit() == False) and (lista[1] in objetos):
            for elemento in variables:
                if lista[1] == elemento:
                    respuesta = True
    
    return respuesta

# Función para comando 'pick X n'
def pick(lista:list,variables:dict):
    tamanio = len(lista)
    respuesta = False
    if tamanio == 3:
        lista[2]= lista[2].strip('\n')
        lista[2]= lista[2].lstrip(")")
        if lista[2].isdigit() == True and lista[1] in objetos:
            respuesta = True
        elif (lista[1].isdigit() == False) and (lista[1] in objetos):
            for elemento in variables:
                if lista[1] == elemento:
                    respuesta = True
    
    return respuesta


#Función para 'move-dir n D'
def move_dir(lista:list,variables:dict):
    tamanio = len(lista)
    respuesta = False
    if tamanio == 3:
        lista[2]= lista[2].strip('\n')
        lista[2]= lista[2].lstrip(")")
        if lista[1].isdigit() == True and lista[2] in posiciones2:
            respuesta = True
        elif (lista[1].isdigit() == False) and (lista[2] in posiciones2):
            for elemento in variables:
                if lista[1] == elemento:
                    respuesta = True
    
    return respuesta

#Función para 'run-dirs Ds'
def run_dirs(lista:list,variables:dict):
    tamanio = len(lista)
    respuesta = False
    if tamanio == 2:
        lista[1]= lista[1].strip('\n')
        lista[1]= lista[1].lstrip(")")
        lista[1]=list(lista[1])
        if (isinstance(lista[1], list) == True) and len(lista[1]) > 0:
            for direccion in lista[1]:
                if direccion in posiciones2:
                    respuesta = True
    return respuesta

#Función para 'move-face n O'
def move_face(lista:list,variables:dict):
    tamanio = len(lista)
    respuesta = False
    if tamanio == 3:
        lista[2]= lista[2].strip('\n')
        lista[2]= lista[2].lstrip(")")
        if lista[1].isdigit() == True and lista[2] in puntos_cardinales:
            respuesta = True
        elif (lista[1].isdigit() == False) and (lista[2] in puntos_cardinales):
            for elemento in variables:
                if lista[1] == elemento:
                    respuesta = True 
    return respuesta



# Función para comando 'skip'
def skip(lista:list):
    tamanio = len(lista)
    respuesta = False
    if tamanio == 1:
        respuesta = True  
    return respuesta


# Función para comando 'IF'
def if_command(linea:str):
    
    respuesta = False
    centinela = True
    
    while centinela == True:
        
        if "[" in linea:
            pos = linea.find("[")
            linea = linea[pos+1:]
            if linea is None:
                linea = archivo.readline()
                solucion = recorrido(linea)
                if solucion == True:
                    respuesta = True
                else:
                    respuesta
                    break
            else:
                solucion = recorrido(linea)
                if solucion == True:
                    respuesta = True
                else:
                    respuesta
                    break
                
        elif "]" in linea:
            pos = linea.find("]")
            linea = linea[:pos]
            centinela = False
            solucion = recorrido(linea)
            if solucion == True:
                    respuesta = True
            else:
                    respuesta
                    break
                
        else:
            linea = archivo.readline()
            solucion = recorrido(linea)
            if solucion == True:
                    respuesta = True
            else:
                    respuesta
                    break
        
    return respuesta

# Función para comando 'BLOCK'
def block(linea:str):
    
    respuesta = False
    centinela = True
    
    while centinela == True:
        
        if "(" in linea:
            pos = linea.find("K")
            linea = linea[pos+1:]
            if linea is None:
                linea = archivo.readline()
                solucion = recorrido(linea)
                if solucion == True:
                    respuesta = True
                else:
                    respuesta
                    break
            else:
                solucion = recorrido(linea)
                if solucion == True:
                    respuesta = True
                else:
                    respuesta
                    break
                
        elif ")" in linea:
            pos = linea.find(")")
            linea = linea[:pos]
            centinela = False
            solucion = recorrido(linea)
            if solucion == True:
                    respuesta = True
            else:
                    respuesta
                    break
                
        else:
            linea = archivo.readline()
            solucion = recorrido(linea)
            if solucion == True:
                    respuesta = True
            else:
                    respuesta
                    break
        
    return respuesta
            
    
# Función para comando 'REPEAT'
def repeat(linea:str):
    
    respuesta = False
    centinela = True
    
    while centinela == True:
        
        if "[" in linea:
            pos = linea.find("[")
            linea = linea[pos+1:]
            if linea is None:
                linea = archivo.readline()
                solucion = recorrido(linea)
                if solucion == True:
                    respuesta = True
                else:
                    respuesta
                    break
            else:
                solucion = recorrido(linea)
                if solucion == True:
                    respuesta = True
                else:
                    respuesta
                    break
                
        elif "]" in linea:
            pos = linea.find("]")
            linea = linea[pos]
            solucion = recorrido(linea)
            if solucion == True:
                    respuesta = True
            else:
                    respuesta
                    break
                
        elif ")" in linea:
            pos = linea.find(")")
            linea = linea[:pos]
            centinela = False
            solucion = recorrido(linea)
            if solucion == True:
                    respuesta = True
            else:
                    respuesta
                    break
                
        else:
            linea = archivo.readline()
            solucion = recorrido(linea)
            if solucion == True:
                    respuesta = True
            else:
                    respuesta
                    break
        
    return respuesta

def to_end(linea:str,lista:list):
    
    
    
    funcion= []
    nombre = lista[1].strip("\n")
    funciones.append(nombre)
    
    respuesta = False
    centinela = True
    
    while centinela == True:
        
        linea = linea.strip("\n")
        linea = linea.strip(" ")
        lista = linea.split(" ")
        
        if ":" in linea:
            pos = linea.find(":")
            linea = linea[pos:]
            if linea is None:
                linea = archivo.readline()
                solucion = recorrido(linea)
                if solucion == True:
                   respuesta = True
                else:
                    respuesta
                    break
            else:
                parametros = linea.split(' ')
                for i in range (0,len(parametros)):
                    parametro = parametros[i].lstrip(":")
                    funcion.append(parametro)
                    variables[parametro] = 0
                linea = archivo.readline()
        
        elif "TO" in linea and len(lista) == 2:
            linea = linea[:0]
            solucion = recorrido(linea)
            if solucion == True:
                    respuesta = True
            else:
                    respuesta
                    break
            linea = archivo.readline()
            

        elif "OUTPUT" in linea: 
            pos = linea.find("T",3,8)
            linea = linea[pos+1:]
            if linea is None:
                linea = archivo.readline()
                solucion = recorrido(linea)
                if solucion == True:
                    respuesta = True
                else:
                    respuesta
                    break
            else:
                solucion = recorrido(linea)
                if solucion == True:
                    respuesta = True
                else:
                    respuesta
                    break
                
        elif "END" in linea:
            pos = linea.find("D")
            linea = linea[:pos+1]
            centinela = False
            solucion = recorrido(linea)
            if solucion == True:
                    respuesta = True
            else:
                    respuesta
                    break
                
                
        else:
            linea = archivo.readline()
            solucion = recorrido(linea)
            if solucion == True:
                    respuesta = True
            else:
                    respuesta
                    break
                
    almacenamiento[nombre] = funcion
        
    return respuesta
            



main(archivo)
archivo.close()