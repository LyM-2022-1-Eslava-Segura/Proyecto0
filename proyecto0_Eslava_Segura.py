# -*- coding: utf-8 -*-
# Proyecto 0 Lenguajes y máquinas 2022-1
# 
# Juan Andrés Eslava cod: 202012035
#
# Alejandro Segura cod: 
#

from ast import Break
from pickle import FALSE
from xmlrpc.client import boolean


archivo = open('prueba.txt' , 'r')

variables = {}

funciones = []

almacenamiento = {}

posiciones=[':around',':left', ':right']
posiciones2=[':front',':left', ':right',':back']
puntos_cardinales=[':north',':east',':west',':south']
objetos=['Balloons', 'Chips']
comandos=['(defvar','(=','(move','(turn','(face','(put','(pick','(move-dir','(run-dirs','(move-face','(skip']
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
    boolean = ["(facing-p","(can-put-p", "(can-pick-p", "(can-move-p", "(not"]
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

    elif lista_linea[0] == '(if':
        respuesta = if_command(linea)
        if respuesta == True:
            solucion = True
        else:
            solucion
                        
            
    elif lista_linea[0] == '(loop' and lista_linea[1] in boolean:
        respuesta = loop(linea)
        if respuesta == True:
            solucion = True
        else:
            solucion
            
    elif (lista_linea[0] == '(repeat') and (lista_linea[1].isdigit() == True) :
        respuesta = repeat_times(linea)
        if respuesta == True:
            solucion = True
        else:
            solucion
    
    elif lista_linea[0] == '(defun':
        respuesta = defun(linea,lista_linea)
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


# Función para comando 'if'
def if_command(linea:str):

    respuesta = False
    centinela = True
    
    while centinela == True:
        pos=linea.rfind(')')  
        linea[0].strip('(')
        while len(nueva_linea)!=0:
            linea.strip("\n")
            nueva_linea=archivo.readline()
        linea.replace(' ','')
        bloque=[] 
        condicion=[]
        for c in linea:
            if c =='('and len(condicion)==0:
                condicion.append(c)
            if len(condicion==1):
                p=c
                while p!=')':
                    condicion[0]+c
                    p==')'
        linea.strip(condicion[0])
        for c in linea:
            if c =='(' and len(bloque)==0:
                bloque.append(c)
            if len(bloque>1):
                j=c
                while j!=')':
                    bloque[0]+c
                    j=')'
        if ((condicion[0] in boolean) or (condicion[0] in funciones)) and len(bloque)==2:
            respuesta = True
            break
        else:
            respuesta = False
            break
        
    return respuesta   


# Función para comando 'loop'
def loop(linea: str):
    
    pos=linea.rfind(')')  
    linea[0].strip('(')
    while len(nueva_linea)!=0:
        linea.strip("\n")
        nueva_linea=archivo.readline()
        linea.replace(' ','')
    dicc={'(':1,
          ')':0}
    for c in linea:
        if c == '(':
            dicc['(']+=1
        if c == ')':
            dicc[')']+=1
    if dicc['(']==dicc[')']:
        respuesta = True
    else:
        respuesta=False
    if respuesta == True:
        cadena_completa=''
        bloque=[]
        condicion=[]
        pos= linea.find('(')
        while pos < len(linea):
            cadena_completa+=linea[pos]
            pos+=1
        bloque_con_condicion=cadena_completa.split(')')    
        condicion.append(bloque_con_condicion[0])
        i=1
        while i < len(bloque_con_condicion):
            bloque.append(bloque_con_condicion[i])
            i+=1
        if condicion[0] in boolean or condicion[0] in funciones:
            respuesta = True
        else: 
            respuesta = False 
        if respuesta == True:    
            for command in bloque:
                if (command.find(comandos[0]>=0)) or (command.find(comandos[1]>=0)) or (command.find(comandos[2]>=0)) or (command.find(comandos[3]>=0)) or (command.find(comandos[4]>=0)) or (command.find(comandos[5]>=0)) or (command.find(comandos[6]>=0)) or (command.find(comandos[7]>=0)) or (command.find(comandos[8]>=0)) or (command.find(comandos[9]>=0)) or (command.find(comandos[10]>=0)):
                    respuesta= True
                else:
                    respuesta=False
                    break
        
    return respuesta   
            
        

            
    
# Función para comando 'repeatTimes'
def repeat_times(linea:str):
    pos=linea.rfind(')')  
    linea[0].strip('(')
    while len(nueva_linea)!=0:
        linea.strip("\n")
        nueva_linea=archivo.readline()
    linea.replace(' ','')
    dicc={'(':1,
          ')':0}
    for c in linea:
        if c == '(':
            dicc['(']+=1
        if c == ')':
            dicc[')']+=1
    if dicc['(']==dicc[')']:
        respuesta = True
    else:
        respuesta=False
    if respuesta == True:
        bloque=''
        pos=linea.find('(')
        while pos < len(linea):
            bloque+=linea[pos]
            pos+=1
        list_bloque=bloque.split(')')
        for command in list_bloque:
            if (command.find(comandos[0]>=0)) or (command.find(comandos[1]>=0)) or (command.find(comandos[2]>=0)) or (command.find(comandos[3]>=0)) or (command.find(comandos[4]>=0)) or (command.find(comandos[5]>=0)) or (command.find(comandos[6]>=0)) or (command.find(comandos[7]>=0)) or (command.find(comandos[8]>=0)) or (command.find(comandos[9]>=0)) or (command.find(comandos[10]>=0)):
                respuesta= True
            else:
                respuesta=False
                break
    return respuesta
        
            

#Función para 'defun'
def defun(linea:str,lista:list):
    pass
            



main(archivo)
archivo.close()