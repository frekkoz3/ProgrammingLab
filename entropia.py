import math

class elemento():
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return self.type

    def __repr__(self):
        return self.type

def crealista(numerored, numeroblu):
    lista = []
    for i in range (1, numerored+numeroblu+1):
        if i>numeroblu:
            rosso = elemento('rosso')
            lista.append(rosso)
        else:
            blu = elemento('blu')
            lista.append(blu)
    return lista
    
def entropiarelativa(lista, type):
    c = 0 
    for element in lista:
        if element.type == type:
            c = c+1
    if c == 0:
        return 0
    value = c / len(lista)
    return -1 * math.log2(value)

def media(a, b):
    return (a + b)/2
    
for i in range (0, 21):
    lista = crealista(5, 20-i)
    print('caso numero {}'.format(i))
    print('numero rossi = {}'.format(5))
    print('entropia relativa ai rossi = {}'.format(entropiarelativa(lista, 'rosso')))
    print('numero blu = {}'.format(20-i))
    print('entropia relativa ai blu = {}'.format(entropiarelativa(lista, 'blu')))
    print(media(entropiarelativa(lista, 'rosso'), entropiarelativa(lista, 'blu')))
    print()
