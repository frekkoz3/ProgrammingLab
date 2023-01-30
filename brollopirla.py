class OggettoOrdinabile:

    def valore(self):
        raise NotImplementedError

class Numero(OggettoOrdinabile):

    def __init__(self, n):
        self.n = n;

    def valore(self):
        return self.n

    def stampa(self):
        print(self.n)

class Scritta(OggettoOrdinabile):

    def __init__(self, s):
        self.s = s

    def valore(self):
        sum = 0
        for i in self.s:
            sum += ord(i)
        sum /= len(self.s)
        return sum
        
    def stampa(self):
        print(self.s)
        
def Ordina(lista):

    for i in range (0, len(lista)):
        for j in range (0, len(lista) - 1):
            if lista[j].valore() > lista[j+1].valore():
                t = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = t

    return lista

def specialPrint(lista):

    for item in lista:
        item.stampa()   


n1 = Numero(3)
n2 = Numero(980)
n3 = Numero(1)
s1 = Scritta('ciao')
s2 = Scritta('hiaaaaaaaaaaaaaaaaaaaaaa')
s3 = Scritta('AAACCCZZZAa')

lista = [n1, n2, n3, s1, s2, s3]

specialPrint(Ordina(lista))

