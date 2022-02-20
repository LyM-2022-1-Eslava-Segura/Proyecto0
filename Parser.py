from Tokens import leer_archivo

nombre = 'prueba.txt' #nombre del texto ejemplo
lista_tokens = leer_archivo(nombre)
#print(lista_tokens) 
#        |_______->imprime una lista con los tokens del archivo

def leer(nombre):
    file = open(nombre,'r')
    linea = file.readlines()
    lista_l = []
    instrucciones_de_la_gramatica =['grab','drop','free','pick']
    puntos_cardinales = ['N','E','W','S']
    r = 'No hay errores de sintaxis'
    for l in linea:
        lista_l.append(l.strip())
        #print(l.strip())
    #print(linea)
    file.close
    for li in lista_l:
        i = 0
        while i<len(li):
            if li[i] == '(' and li[i] in lista_tokens:
                if li[i+1] == 'i' and li[i+2] == 'f':
                    if li[i+4] != '(' or '':
                        r = 'Error de sintaxis'
                    else:
                        if (li[i+6]+li[i+7]+li[i+8]) == 'not' and (li[i+6]+li[i+7]+li[i+8]) in lista_tokens:
                            if li[i+9] != '(' or '':
                                r = 'Error de sintaxis'
                                if (li[i+11]+li[i+12]+li[i+13]+li[i+14]+li[i+15]+li[i+16]+li[i+17]+li[i+18]+[i+19]) not in lista_tokens:
                                    r = 'Error de sintaxis'
                        if (li[i+6]+li[i+7]+li[i+8]) == 'can' and (li[i+6]+li[i+7]+li[i+8]) in lista_tokens:
                            if li[i+9] != '(' or '':
                                r = 'Error de sintaxis'
                                if (li[i+11]+li[i+12]+li[i+13]+li[i+14]+li[i+15]+li[i+16]+li[i+17]+li[i+18]+[i+19]) not in lista_tokens:
                                    r = 'Error de sintaxis'
                elif (li[i+1]) == 'walk' and (li[i+1]) in lista_tokens:
                    if li[i+5] == ')':
                        r = 'Error de sintaxis'
                    elif li[i+7] != ')':
                        r = 'Error de sintaxis'
                elif (li[i+1]) == 'define' and (li[i+1]) in lista_tokens:
                    if li[i+7] == '':
                        r = 'Error de sintaxis'
                    if li[i+7] == '(':
                        r = 'Error de sintaxis'
                    if li[i+7] == ')':
                        r = 'Error de sintaxis'
                elif (li[i+1]) == 'blocked?' and (li[i+1]) in lista_tokens:
                    if (li[i+2]) != ')':
                        r = 'Error de sintaxis'
                elif (li[i+1]) == 'facing?' and (li[i+2]) in puntos_cardinales and (li[i+1]) in lista_tokens:
                    if (li[i+3]) != ')':
                        r = 'Error de sintaxis'
                elif (li[i+1]) == 'look' and (li[i+2]) in puntos_cardinales and (li[i+1]) in lista_tokens:
                    if (li[i+3]) != ')':
                        r = 'Error de sintaxis'
                elif (li[i+1]) == 'rotate' and (li[i+1]) in lista_tokens:
                    if (li[i+2]) != '':
                        r = 'Error de sintaxis'
                elif (li[i+1]) == 'back' and (li[i+1]) in lista_tokens:
                    if (li[i+2]) != ')':
                        r = 'Error de sintaxis'
                elif (li[i+1]) == 'drop' and (li[i+1]) and (li[i+1]) in instrucciones_de_la_gramatica:
                    if (li[i+2]) != '':
                        r = 'Error de sintaxis'
                elif (li[i+1]) == 'grab' and (li[i+1]) in instrucciones_de_la_gramatica:
                    if (li[i+2]) != '':
                        r = 'Error de sintaxis'
                elif (li[i+1]) == 'grab' and (li[i+1]) in instrucciones_de_la_gramatica:
                    if (li[i+2]) != '':
                        r = 'Error de sintaxis'
                elif (li[i+1]) == 'free' and (li[i+1]) in instrucciones_de_la_gramatica:
                    if (li[i+2]) != '':
                        r = 'Error de sintaxis'
                elif (li[i+1]) == 'pick' and (li[i+1]) in instrucciones_de_la_gramatica:
                    if (li[i+2]) != '':
                        r = 'Error de sintaxis'

            i += 1


    return r
print(leer(nombre))
