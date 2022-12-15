#esperimento simpatico che 
#calcola e plotta
#la complessità della ricerca binaria
#e usa solo la listcomprehension
#per creare la lista da plottare

#questo bisearch ha una variabile c
#che conta il numero di operazioni che esegue
#restituisce la posizione e anche il numero di operazioni che esegue

#nb : ci sarebbero stati 1 milioni di modi più 
#intelligenti per eseguire questo calcolo
#ma hey, così è più divertente

def bisearch(list, l, r, x, c):

    if ( l <=  r):
        m = int((l + r) / 2)
        if list[m] == x : 
            return [m, c+1]
        if list[m] > x : 
            return bisearch(list, l, m-1, x, c+1)
        return bisearch(list, m+1, r, x, c+1)
    return [-1, c+1]

print("BENVENUTO!")
print("questo è un esperimento inutile che vuole rappresentare la complessità della ricerca binaria media in funzione della dimensione della lista ordinata in cui viene ricercato un elemento")
print("ti viene ora richiesto di inserire un n. questo n è la dimensione massima che si vuole testare. (ps, test non implementati quindi non fare la testa di cazzo ed inserisci un valore positivo, di tipo intero e bho un minimo decente non troppo enorme, grazie)")
n = int(input("inserisci n:"))

#fatto tutto con la list comprehension perché siamo un po' sadici
#e al posto di andare a bere al mercoledì sera
#ci piace farci del male

#comunque quello che fanno le due righe qui sotto 
#è creare la lista contenente una ad una le complessità
#medie del bisearch all'aumentare della dimensione della lista

list = [[j*2+1 for j in range (0, i)] for i in range(1, n)]
c_tot = [sum([bisearch(item, 0, len(item)-1, i, 0)[1] for i in range (0,item[-1]+2)])/(item[-1]+2) for item in list]
    
from matplotlib import pyplot

pyplot.ylim(0,n)
pyplot.plot(c_tot, color="tab:blue")
pyplot.show()