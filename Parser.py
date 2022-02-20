from string import digits
from Tokens import leer_archivo

nombre = 'prueba.txt' #nombre del texto ejemplo
lista_tokens = leer_archivo(nombre)
print(lista_tokens) 


def leer(nombre):
    file = open(nombre,'r')
    linea = file.readlines()
    lista_l = []
    puntos_cardinales = [':north',':east',':west',':south']
    r = 'Si'
    for l in linea:
        lista_l.append(l.strip())
        #print(l.strip())
    #print(linea)
    print(lista_l)
    file.close
    for li in lista_l:
        i = 0
        while i<len(li):
            print( li)
            if li[i] == '(' and li[i] in lista_tokens:
                if (li[i+1]+li[i+2]+li[i+3]+li[i+4]) == 'move' and (li[i+1]+li[i+2]+li[i+3]+li[i+4]) in lista_tokens:
                    if li[i+5] == ')':
                        r = 'No'
                    elif li[i+7] != ')':
                        r = 'No'
                elif ((li[i+1]+li[i+2]+li[i+3]+li[i+4]+li[i+5]+li[i+6])) == 'defvar' and ((li[i+1]+li[i+2]+li[i+3]+li[i+4]+li[i+5]+li[i+6])) in lista_tokens:
                    if li[i+8] == '':
                        r = 'No'
                    if li[i+8] == '(':
                        r = 'No'
                    if li[i+8] == ')':
                        r = 'No'
                    if li[len(li)-2] not in digits:
                        r='No'
                elif (li[i+1]+li[i+2]+li[i+3]+li[i+4]+li[i+5]) == 'defun' and (li[i+1]+li[i+2]+li[i+3]+li[i+4]+li[i+5]) in lista_tokens:
                    if li[i+7] == '':
                        r='No'
                    if li[i+7]=='(':
                        r='No'
                elif (li[i+1]+li[i+2]+li[i+3]+li[i+4]+li[i+5]+li[i+6]+li[i+7]+li[i+8]) == 'facing-p' and ((li[i+1]+li[i+2]+li[i+3]+li[i+4]+li[i+5]+li[i+6]+li[i+7]+li[i+8])) in puntos_cardinales and (li[i+1]) in lista_tokens:
                    if (li[i+3]) != ')':
                        r = 'No'
                elif (li[i+1]+li[i+2]+li[i+3]+li[i+4]) == 'face' and (li[i+1]+li[i+2]+li[i+3]+li[i+4]) in lista_tokens:
                    if (len(li)-1) != ')':
                        r = 'No'
                    if li[i+6]!=':':
                        r= 'No'                    
                elif (li[i+1]+li[i+2]+li[i+3]+li[i+4]) == 'turn' and (li[i+1]+li[i+2]+li[i+3]+li[i+4]) in lista_tokens :

                    if (len(li)-1) != ')':
                        r = 'No'
                    if li[i+6]!=':':
                        r= 'No'
                    if li[i+7] != ('l' or 'r' or 'a'):
                        r='No'
                elif (li[i+1]+li[i+2]+li[i+3]) == 'put' and (li[i+1]+li[i+2]+li[i+3]) in lista_tokens:
                    if (li[i+2]) != '':
                        r = 'No'
                elif (li[i+1]+li[i+2]+li[i+3]+li[i+4]) == 'pick' and (li[i+1]+li[i+2]+li[i+3]+li[i+4]) in lista_tokens:
                    if (li[i+2]) != '':
                        r = 'No'

            i += 1


    return r
print(leer(nombre))
