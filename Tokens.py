
nombre = 'prueba.txt' #nombre del texto ejemplo

def leer_archivo(nombre):
    file = open(nombre,'r')
    linea = file.readlines()
    lista1 = []
    #print(linea)
    for l in linea:
        li = l.strip().lower()
        for i in li:
            n = i.strip()
            lista1.append(n)
    file.close
    letras = ['a','b','c','d','e','f','g','h','i','j','k',
            'm','n','l','o','p','q','r','s','t','u','v','w',
            'x','y','z','?']
    digitos = ['0','1','2','3','4','5','6','7','8','9']
    tokens = []
    tokens_sin_repetir = []
    tokens_true = []
    a = 0

    while a<len(lista1):
        n = 1
        boo = False
        
        if lista1[a] == '(' or lista1[a] == ')':
            if lista1[a] not in tokens:
                tokens.append(lista1[a])
        elif lista1[a] in digitos:
            if lista1[a] not in tokens:
                tokens.append(lista1[a])
        elif lista1[a] in letras:
            tok = ''
            tok += (lista1[a]) 
            while boo == False:
                if lista1[(a+n)] in letras:
                    tok += (lista1[(a+n)])
                    n += 1
                elif lista1[(a+n)] not in  letras:
                    tokens.append(tok)
                    boo = True
        a += 1
    c = 0

    while c<len(tokens):
        d = 0
        if tokens[c] == '(' or tokens[c] == ')' or tokens[c] in digitos:
            tokens_true.append(tokens[c])
            c += 1
        else:
            tokens_true.append(tokens[c])
            d = len(tokens[c])
            c += d
    for t in tokens_true:
        if t not in tokens_sin_repetir:
            tokens_sin_repetir.append(t)
    return tokens_sin_repetir
#print(leer_archivo('prueba.txt'))